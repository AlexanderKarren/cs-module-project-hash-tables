import random
import math

my_cache = {}


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    string_key = f"{x},{y}"

    if my_cache.get(string_key):
        return my_cache[string_key]

    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653
    my_cache.update({string_key: v})

    return v


print("Pre-populating cache...")

for i in range(2, 14):
    for j in range(3, 6):
        slowfun(i, j)


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    # print(f'{i}: {x},{y}: {slowfun_too_slow(x, y)}')
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
