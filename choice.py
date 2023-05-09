import random
def numbers():
    s = list(range(1, 10))
    x, y = random.sample(s, 2)
    return x, y
