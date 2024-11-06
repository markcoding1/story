init python: 
    class OtherChar:
        def __init__(self, character, name, like):
            self.c = character
            self.name = name
            self.like = like

        def increase_like (self):
            self.like += 1