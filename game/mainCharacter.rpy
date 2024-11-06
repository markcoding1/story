init python: 
    class MainChar:
        def __init__(self, character, name, speed):
            self.c = character
            self.name = name
            self.speed = speed

        def increase_speed (self):
            self.speed += 1