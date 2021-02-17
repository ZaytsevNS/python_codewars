import random


class Ghost(object):
    def __init__(self):
        self.color = random.choice(["white", "yellow", "purple", "red"])
    
ghost = Ghost()