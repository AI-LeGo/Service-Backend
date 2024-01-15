from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse, JSONResponse
import os

import tools.OpenAI_APIs as api
import tools.Constant as const
import tools.Common as common
import tools.API_KEY as key

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
        contents = await file.read()
        FILE_DIR = UPLOAD_DIR + file.filename

        with open(UPLOAD_DIR + file.filename, "wb") as f:
            f.write(contents)

            api_key = key.api_key
            client = api.get_openai_client(api_key=api_key)

            image_path = FILE_DIR
            base64_image = common.encode_image(image_path)
            result = api.get_openai_api_cartoon_caption(api_key, base64_image, const.prompt_cartoons, 300)

            return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))