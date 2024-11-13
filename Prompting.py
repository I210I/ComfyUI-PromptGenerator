import os
import random
import datetime

class Prompter:
    BASE_PROMT = "score_9,score_8, score_8_up, score_7, score_7_up, BREAK, "
    
    @classmethod
    def INPUT_TYPES(cls):
        inputs = {
            "required": {
                "runner": ("INT", {"default": 1, "min": 1, "max": 999999, "step": 1, "tooltip": "to run always input a random number"}),
                "couple" : ("BOOLEAN", {"default" : False, "label_on": "Yes", "label_off": "No", "forceInput": False,
                                        "tooltip": "The couple can be XX or XY randomly, although you can specify it using your LoRAs or by concatenating prompts."}),
                "sex_gender" : ("BOOLEAN", {"default" : False, "label_on": "Male", "label_off": "Female", "forceInput": False,
                                        "tooltip": "Gender of main character."}),
                "mature" : ("BOOLEAN", {"default" : False, "label_on": "NSFW", "label_off": "SFW", "forceInput": False,
                                        "tooltip": "Mature means sexual acts. And It could BREAK field Dress/Undress"}),
                "wings" : ("BOOLEAN", {"default" : False, "label_on": "Yes", "label_off": "No", "forceInput": False}),
                "tail" : ("BOOLEAN", {"default" : False, "label_on": "Yes", "label_off": "No", "forceInput": False}),
                "background" : ("BOOLEAN", {"default" : False, "label_on": "Random background", "label_off": "Blank bg", "forceInput": False}),
                "undress" : ("BOOLEAN", {"default" : False, "label_on": "Random clothes", "label_off": "nude or semi nude", "forceInput": False})                
            }
        } 
        return inputs
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("positive_prompt",
    )
    OUTPUT_TOOLTIPS = ("Prompt to connect into string input in CLIP TEXT ENCODE",)
    FUNCTION = "generate_prompt"
    CATEGORY = "Prompt/RandomPrompt"
 
    @staticmethod
    def __read_or_create_file(file_name):
        """
        This function reads the file if it exists, otherwise, it creates the file.
        It returns the content of the file as a list of words.
        """
        data_dir = "DataWords"
        if not os.path.exists(data_dir):
            os.makedirs(data_dir)

        file_path = os.path.join(data_dir, file_name)

        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass

        with open(file_path, 'r') as f:
            content = f.readlines()

        words = [word.strip() for line in content for word in line.split(',') if word.strip()]
        return words

    @staticmethod
    def generate_prompt(runner, couple, sex_gender, mature, wings, tail, background, undress):
        """
        Reads the specified files based on the boolean values received as parameters.
        If the file does not exist, it creates it. If the file is empty, it continues.
        Selects a random word from each specified file and concatenates them into a single string.
        """
          # Determine file flags
        sexual_acts = couple and mature
        sexual_position = mature and couple

        # Randomly choose one to be true and the other to be false if both are initially true
        if sexual_acts and sexual_position:
            current_millisecond = datetime.datetime.now().microsecond // 1000

            if current_millisecond % 2 == 0:
                sexual_acts = True
                sexual_position = False
            else:
                sexual_acts = False
                sexual_position = True
                
        file_flags = {
            "background": background,
            "clothes": undress,
            "face_expresion": True,
            "position": not couple,
            "sexual_acts": sexual_acts,
            "sexual_acts_solo": not couple and mature,
            "sexual_position": sexual_position,
            "sexual_clothes": mature and undress,
            "tail": tail,
            "wings": wings,
            "view": True
        }


        prompt_string = ""
        if mature:
            prompt_string += random.choice(["rating_explicit, ","rating_cuestionable, "])

        else:
            prompt_string += "rating_safe, "

        if not background:
            prompt_string += "blank background, mate background, empty background, "
        if couple:
            prompt_string += "1man, black hair, BREAK, 1girl, "
        else:
            if sex_gender:
                prompt_string += "solo, 1man, "
            else:
                prompt_string += "solo, 1girl, hourglass body, "

        distance = ["medium shot", "close up shot, eye level", "full body shot, full body", "cowboy shot"]
        selected_words = []
    
        for file_name, should_read in file_flags.items():
            if should_read:
                words = Prompter.__read_or_create_file(file_name)
                if words:
                    selected_word = random.choice(words) + ", "
                    selected_words.append(selected_word)
        full_prompt =  Prompter.BASE_PROMT + " " + prompt_string + " ".join(selected_words) + random.choice(distance)
        print(full_prompt)
        return full_prompt


