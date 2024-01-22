from fastapi import FastAPI, UploadFile, File, HTTPException, WebSocket
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse

import os
import json
import subprocess
import shutil
from datetime import datetime

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
        # Making file name using current time
        current_time = datetime.now()
        file_name = current_time.strftime("%Y%m%d%H%M%S%f")[:-2]

        FILE_DIR = UPLOAD_DIR + file_name + '.jpeg'

        with open(FILE_DIR, "wb") as f:
            f.write(contents)

            api_key = key.api_key
            client = api.get_openai_client(api_key=api_key)

            # OpenAI API request
            image_path = FILE_DIR
            base64_image = common.encode_image(image_path)
            result = api.get_openai_api_cartoon_caption(api_key, base64_image, const.prompt_cartoons, 700)
            
            json_data = json.loads(result['choices'][0]['message']['content'])
            
            with open(f'../Emotional-TTS/json/{file_name}.json', 'w') as json_file:
                json.dump(json_data, json_file, indent=2)
            
            tts_result = subprocess.run([f"cd ../Emotional-TTS; python inference.py {file_name};"], shell=True)
                
            if tts_result:
                parent_directory = os.path.dirname(os.getcwd())
                wav_file_path = parent_directory + f"/Emotional-TTS/outputs/gen_{file_name}.wav"
                
                return FileResponse(wav_file_path, filename=file_name, media_type="audio/wav")
            

    # Error handling
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

