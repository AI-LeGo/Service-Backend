
import base64
import json
import subprocess

# Encode images into Base64 format
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

# Parse target text into TTS model capable format
def parse_result_text(text):

    output = json.dumps(dict())
    return output

# Run TTS model with shell script
def run_tts_model(tts_input):
    # # Run the shell script
    # script_path = const.script_path
    # result = subprocess.run(["bash", script_path], capture_output=True, text=True)
    #
    # # Exit function if the script ended with error
    # if result == 1:
    #     return {"response" : 500, "path" : None}
    #
    # # Return the generated wav file path
    # tts_output_path = const.tts_output_path
    # file_name = ""
    # return {"response" : 200, "path" : tts_output_path + file_name}

    pass
