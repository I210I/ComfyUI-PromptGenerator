from .Prompting import Prompter

NODE_CLASS_MAPPINGS = {
    "prompterText" : Prompter
}

NODE_DISPLAY_NAMES_MAPPINGS = {
    "prompterText": "Prompter random node"
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAMES_MAPPINGS']