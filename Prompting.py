class Prompter:
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "couple" : ("BOOLEAN", {"default" : False, "label_on": "Yes", "label_off": "No", "forceInput": False,
                                        "tooltip": "The couple can be XX or XY randomly, although you can specify it using your LoRAs or by concatenating prompts."}),
                "sex_gender" : ("BOOLEAN", {"default" : False, "label_on": "Female", "label_off": "Male", "forceInput": False,
                                        "tooltip": "Gender of main character."}),
                "mature" : ("BOOLEAN", {"default" : False, "label_on": "NSFW", "label_off": "SFW", "forceInput": False,
                                        "tooltip": "Mature means sexual acts. And It could BREAK field Dress/Undress"}),
                "background" : ("BOOLEAN", {"default" : False, "label_on": "Random background", "label_off": "Blank bg", "forceInput": False}),
                "undress" : ("BOOLEAN", {"default" : False, "label_on": "Random clothes", "label_off": "nude or semi nude", "forceInput": False})
                
            }
        }
        return inputs
        
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("positive_prompt",)
    OUTPUT_TOOLTIPS = ("Prompt to connect into string input in CLIP TEXT ENCODE",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Prompt/RandomPrompt"


    @staticmethod
    def generate_prompt(couple, sex_gender, mature, background, undress):
       return "score_9,score_8, score_8_up, score_7, score_7_up,  1girl, Linda_-_Rio_PonyXL"