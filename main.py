from fastapi import FastAPI, UploadFile, File, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

import os
import json

import tools.OpenAI_APIs as api
import tools.Constant as const
import tools.Common as common
from tools import API_KEY as key

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "photo/"

@app.get("/")
async def root():
    root_path = os.getcwd()
    return FileResponse(os.path.join(root_path, "template", "index.html"))

@app.get("/caption")
async def cartoon_caption():
    api_key = key.api_key
    client = api.get_openai_client(api_key=api_key)

    image_path = "./photo/test.jpeg"
    base64_image = common.encode_image(image_path)
    result = api.get_openai_api_cartoon_caption(api_key, base64_image, const.prompt_cartoons, 300)
    return result


@app.post("/upload/photo")
async def upload_photo(file: UploadFile = File(...)):
    try:
        # Reading uploaded local file
        contents = await file.read()
        FILE_DIR = UPLOAD_DIR + file.filename

        with open(UPLOAD_DIR + file.filename, "wb") as f:
            f.write(contents)

            api_key = key.api_key
            client = api.get_openai_client(api_key=api_key)

            # OpenAI API request
            image_path = FILE_DIR
            base64_image = common.encode_image(image_path)
            result = api.get_openai_api_cartoon_caption(api_key, base64_image, const.prompt_cartoons, 500)

            return result

            # Parsing data for TTS model input
            result_json = json.loads(result)
            tts_container_name = const.tts_container_name
            script_path = const.script_path

            tts_result = common.run_tts_model(result_json, tts_container_name, script_path)

            # # Preparing data for TTS input
            # result_text = result.choices[0].message.content
            # tts_input = common.parse_result_text(result_text)
            #
            # # Getting TTS result WAV file
            # result_wav = common.run_tts_model(tts_input)
            #
            # return result_wav

    # Error handling
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

