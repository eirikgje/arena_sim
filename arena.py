import numpy as np
import dndmod
from arenacontext import context

def run_battle(chars):
    order = determine_initiative(chars)
    ctx = context(chars)
    ended = False
    numrounds = 0
    while not ended:
        ended, winner, stats = resolve_round(order, ctx)
        numrounds++
    return winner, stats, numrounds

def determine_initiative(chars):
    #For now, char 1 always starts
    return [0, 1]

def resolve_round(order, ctx):
    winner = -1
    stats = 0
    for char_num in order:
        ctx.char_round(char_num)
        if any(ctx.char_is_defeated):
            if all(ctx.char_is_defeated):
                winner = -1
            else:
                winner = np.array([0, 1])[not ctx.char_is_defeated]
            stats = 0
            break
    return any(ctx.char_is_defeated), winner, stats
