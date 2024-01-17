from openai import OpenAI
import requests

def get_openai_client(api_key: str) -> OpenAI:
    return OpenAI(api_key=api_key)

# Obsolete function
def get_openai_api_vision_response(prompt: str, uri: str, max_tokens: int, client: OpenAI) -> str:
    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt,
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": uri,
                        }
                    }
                ]
            }
        ],
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content

def get_openai_api_cartoon_caption(api_key: str, base64_image, prompt, max_tokens):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": prompt
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": max_tokens
    }

    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    return response.json()


def get_openai_assistant(name: str, instructions: str, type: str, client: OpenAI):
    assistant = client.beta.assistants.create(
        name=name,
        instructions=instructions,
        tools=[{"type": type}],
        model="gpt-4-vision-preview"
    )
    return assistant

