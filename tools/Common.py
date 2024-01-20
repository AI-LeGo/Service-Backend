
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

# Run TTS model with python script
def run_tts_model(tts_input, tts_container_name, script_path):

    command = ['python3', script_path]

    result = subprocess.run(["docker", "exec", tts_container_name] + command, capture_output=True, text=True)

    return result
