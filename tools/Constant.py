
# Prompt for captioning cartoons
prompt_cartoons = """
    Character Identification:
    Please identify which comic strip and characters are depicted in the image provided.
     
    Divide the image into four equal sizes. Each one will be a scene. For each scene, do the following tasks in the order of top left, top right, bottom left, bottom right.
    Scene Descriptions:
      
    Please identify the comic strip and characters shown in the scene, and return the answer in following JSON format, not using markdown:
    {
        "characters_list" : The list of characters showing on the comic and their gender.
        {
            Include {"Narrator" : "female"} by default and list other characters showing on the comics.
        },
        "scene_list" : 
        {
            "scene #0" : [ This entry is only for describing overall speaker and narration, not describing the specific scene.
            Make a dictionary that has speaker, description in it. 
                "speaker" : "narrator"
                "description" : Describe background of the entire comic strip in one or two sentence. It has to include the location, scenery, atmosphere, time (morning, day, night, past, present, future), season. Don't tell me what you're not sure about.
            ]
            "scene #1" : [
            Make a dictionary that has speaker, description in it.
                "speaker" : "narrator"
                "description" : Explain the situation of this scene for one sentence without mentioning cartoon or comic strip or speech bubble. Include the name of characters, actions, positions of characters. You should be objective.
            Make another dictionary that has speaker, emotion, speech in it. 
                "speaker" : The character currently speaking in this scene.
                "emotion" : Choose one of these six emotions to explain how characters in this picture feels: [angry, neutral, happy, neutral, surprise, sad]
                "speech" : The speech that the character currently speaking in this scene. If there is no punctuation mark at the end of the speech, add period.
            ]
            "scene #2" : ...
            ...
            "scene #4" : ...
        }
    }   
"""

tts_container_name = ""

script_path = ""

