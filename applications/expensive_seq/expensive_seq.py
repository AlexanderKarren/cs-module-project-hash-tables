# Your code here
my_cache = {}


def expensive_seq(x, y, z):
    string_entry = f"{x},{y},{z}"
    if my_cache.get(string_entry):
        return my_cache[string_entry]
    if x <= 0:
        return y + z
    if x > 0:
        result = expensive_seq(x - 1, y + 1, z) + expensive_seq(x - 2, y + 2, z * 2) + expensive_seq(x - 3, y + 3, z * 3)
        my_cache.update({string_entry: result})
        return result


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
