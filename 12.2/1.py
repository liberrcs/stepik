import random
def generate_ip():
    """_summary_
An IP address consists of four numbers ranging from 
0
0 to 
255
255 (inclusive) separated by a dot.

Write a function generate_ip() that, using the random module, generates and returns a random valid IP address.
    Returns:
        _type_: _description_
    """
    return f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'
help(generate_ip)
