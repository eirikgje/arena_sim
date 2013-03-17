import numpy as np

def distance_to_object(origin, obj):
    return np.abs(origin.status.position - obj.status.position)

def direction_to_object(origin, obj):
    return (obj.status.position - origin.status.position) / distance_to_object(origin, obj)
