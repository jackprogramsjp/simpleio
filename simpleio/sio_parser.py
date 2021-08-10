import re

class ParseError(Exception):
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return repr(self.value)

sio_instructions = [
    "print",
    "println",
    "flush",
    "read",
    "_g",
]

"""
Parses text into list of strings (instructions), and errors if instructions are incorrect.
:param text: The text to parse
:return: A list of correct instructions (strings)
"""
def parse(text):
    instructions = re.split(r'\s+(?=[^"]*(?:"[^"]*"[^"]*)*$)', text) # simple regex to turn them into instructions lol
    instructions = list(filter(None, instructions))

    for i in range(len(instructions)):
        instruction = instructions[i].lower()

        if "\"" in instruction:
            continue
        
        if instruction == "print":
            try:
                instructions[i + 1]
            except IndexError:
                raise ParseError(f"There must be an argument for instruction '{instruction}', at value {i}.")
        else:
            if not instruction in sio_instructions and instructions[len(instructions) - 1] != "":
                raise ParseError(f"Invalid instruction '{instruction}' at value {i}")
    
    return instructions
