import numpy as np
from dndmod import roll
from combat_mod import single_hit
from util_mod import distance_to_object, direction_to_object

class Character(object):
    def __init__(self):
        self.opponents = None

    def round_act(self, context):
        self.opponents = self.get_opponents(context) 
        self.standard_round(context)

    def get_opponents(self, context):
        opponents = []
        for i in range(context.char_num):
            if context.chars[i] != self:
                opponents.append(context.chars[i])
    
    def closest_opponent(self):
        closest_length = 50000
        closest_opponent = None
        dir_to_opponent = None
        for opponent in self.opponents:
            if distance_to_object(self, opponent) < closest_length:
                closest_length = distance_to_object(self, opponent)
                dir_to_opponent = direction_to_object(self, opponent)
                closest_opponent = opponent
        return closest_opponent, closest_length
