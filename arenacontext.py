import numpy as np
from statusmod import init_stati, new_round_trigger, end_round_trigger

class context(object): 
    def __init__(self, chars):
        self._chars = chars
        #Initialize stati
        self.num_chars = len(chars)
        for char in range(self.num_chars):
            self.chars[i].init_status()
        self.char_is_defated = [False] * self.num_chars
        self.stati = []
        for char in range(self.num_chars):
            self.stati.append(self.chars[i].status)

    def char_round(self, char_num):
        new_round_trigger(self, self.chars[char_num])
        self.char_is_defated = self.check_defeat()
        self.chars[char_num].act(self)
        self.char_is_defated = self.check_defeat()
        end_round_trigger(self, self.chars[char_num])
        self.char_is_defated = self.check_defeat()

    def check_defeat(self):
        for i in range(num_chars):
            self.char_is_defated[i] = self.char_is_defeated[i] or self.chars[i].status.hp < 0
