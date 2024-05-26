import random as r
import string

def generate_index():
    """_summary_
Write a function generate_index() that, using the random module, generates and returns a random valid postal code for Latveria.
    Returns:
        _type_: _description_
    """
    S = string.ascii_uppercase
    ind = (''.join(r.sample(S, 2)) + str(r.randrange(100))
    + "_" + str(r.randrange(100)) + ''.join(r.sample(S, 2)))
    return ind
help(generate_index)