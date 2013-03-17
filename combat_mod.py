def single_hit(hitter, opponent, ba_add=0):
    """
    
    ba_add is NOT for enchantment boni etc. It is solely for those attacks that are less than full ba because of multiple in a row etc. Thus, usually it will be negative.
    """
    attack_roll = roll(1, 20)
    if attack_roll >= hitter.critical_range:
        return hitter.resolve_critical(opponent, ba_add, attack_roll)
    attack_roll += hitter.attack_bonus + ba_add
    return attack_roll >= opponent.ac, False

def resolve_critical(hitter, opponent, ba_add, attack_roll):
    if attack_roll == 20:
        hit = True
    else:
        hit = attack_roll + hitter.attack_bonus + ba_add >= opponent.ac
    if not hit:
        return hit, False
    n_attack_roll = roll(1, 20)
    if n_attack_roll == 20:
        critical = True
    else:
        critical = n_attack_roll + hitter.attack_bonus + bad_add >= opponent.ac
