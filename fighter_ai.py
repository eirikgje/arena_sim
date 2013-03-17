from statusmod import full_attack_trigger, attack_trigger
from charmod import Character

#What needs to be here: rules for fighting a standard round, rules for aoos
#conditions for being armed

class Fighter(Character):
    def __init__(self):
        Character.__init__(self)

    def standard_round(self, context):
        if not self.mobile: return
        closest_opponent, length_to_opponent, dir_to_opponent = self.closest_opponent()
        if self.attempt_full_attack(closest_opponent, length_to_opponent, dir_to_opponent, context): return
        if attempt_attack(self, closest_opponent, length_to_opponent, dir_to_opponent, context): return
        if attempt_defensive_fighting(self, closest_opponent, length_to_opponent, dir_to_opponent, context): return
        if attempt_move(self, closest_opponent, length_to_opponent, dir_to_opponent, context): return
        return

    def attempt_full_attack(self, clop, length, direction, context):
        if not self.status.armed: return False
        if not length < 3: return False
        if length == 2: self.fivefoot(direction)
        fivefoot_trigger(self)
        clop, length, direction = self.closest_opponent()
        if any(self.feats == "Power attack"): self.activate_feat("Power attack")
        self.full_attack(clop)

    def full_attack(self, opponent):
        if self.style == "Two-handed":
