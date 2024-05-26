import random
def generate_ip():
    """_summary_
    The generate_ip() function returns a random IP address
    Returns:
        _type_: _description_
    """

    return f'{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}.{random.randint(0, 255)}'
help(generate_ip)