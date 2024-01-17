
# Prompt for captioning cartoons
prompt_cartoons = """
    Character Identification:
    Please identify which comic strip and characters are depicted in the image provided.
    
    Narration(Description):
    "Craft a concise introductory narration for one sentence that captures the essence and mood of the entire comic strip e.g who are the characters, what they are doing, where they are. Make as short as possible like 'Charlie and Linus are talking about life.'”
    
    Divide the image into four equal sizes. Each one will be a scene. For each scene, do the following tasks in the order of top left, top right, bottom left, bottom right.
    
    Please identify the comic strip and characters shown in the scene, and return the answer in following JSON format:
    
    {
        characters : the list of characters showing on the comic including the narrator.
        data : 
        {
            scene #0 : this entry is only for describing overall story and narration, not describing the specific scene.
            {
                speaker : "narrator"
                overall_summary : literally the overall summary of the whole comic.
            },
            scene #1 :
            {
                speaker : the character currently speaking in this scene.
                emotion : Choose one of these six emotions to explain how characters in this picture feels: [angry, neutral, happy, neutral, surprise, sad]
                speech : the speech that the character currently speaking in this scene.
                description : Explain the situation of this scene without mentioning cartoon or comic strip or speech bubble.
            },
            scene #2 : 
            {
                ...
            },
            ...
            scene #4 :
            {
                ...
            }
        }
    }
"""
