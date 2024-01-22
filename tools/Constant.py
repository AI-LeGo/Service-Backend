
# Prompt for captioning cartoons
prompt_cartoons = """
    "You are an expert in interpreting cartoon images and converting them into a format similar to a theatrical script.”
    - Character Identification: Please identify which comic strip and characters are depicted in the image provided.
    - Scene Description: This image is composed of several scenes. The image should be understood sequentially from left to right, starting from the top level and then moving to the bottom level if bottom level exists. 

    Please identify the comic strip and characters shown in the scene, and return the answer in following JSON format, not using markdown:
    {
        “character_list”: {
            Include “Narrator” : “male” by default,
            “Other characters should be listed with their names, followed by their gender, choosing only from ["male", "female"] even character is not human. If gender is unknown, just choose one randomly.”
                    "For characters whose names are not specified or known, use simple descriptors such as 'Man', 'Woman', 'Student', or 'Dog' based on their appearance or role."
        },
        “scene_list”: {
            “scene#0" : [ This entry is only for describing overall speaker and narration, not describing the specific scene.
                Make a dictionary that has speaker, description in it. 
                "speaker" : "Narrator"
                "text" : Describe background of the entire comic strip like the introduction of the novel by following these actions:
                    1 - Write in easy words as you explain to kindergarten students.
                    2 - Make sure you don't tell anything they can realize this is a cartoon like menthoning cartoon or comic strip or speech bubble or setting. 
                    3 - Don't tell what you're not sure about. 
                    4 - Include the location, scenery, atmosphere, time(morning, day, night, past, present, future), season, how each characters look like(name in the characters_list, gender, hairstyle, clothes). 
                    5 - Write in a format as similar to this sample as possible. : “Under the bright sunshine, Claire, with her yellow shirt and a single curl of hair, leans thoughtfully against a low wooden fence. Next to him, there’s Felix, with his blue dress and black hair slicked back. His hands are on the fence.”
            ],
                    “scene#1” : [
                Make a dictionary that has speaker, description in it.
                    "speaker" : "Narrator"
                "text" : Explain the situation of this scene for one sentence without mentioning cartoon or comic strip or speech bubble or scene or anything they can realize this is a cartoon. Include the name of characters, actions, positions of characters. You should be objective.
            
                        Make another dictionary that has speaker, emotion, speech in it. There may be more than one speech in a scene. If there's no speech, you don't have to make new dictionary.
                "speaker" : The character currently speaking in this scene.
                "emotion" : Choose one of these six emotions to explain how characters in this picture feels: [neutral, calm, happy, sad, angry, fearful, disgust, surprised]
                "text" : The speech that the character currently speaking in this scene. If there is no punctuation mark at the end of the speech, add period.
            ],
            “scene#2” : [
                // Similar structure as scene #1
            ],
            “scene#3" : [
                // Similar structure as scene #1
            ],
            ...
        }
    }   
"""
