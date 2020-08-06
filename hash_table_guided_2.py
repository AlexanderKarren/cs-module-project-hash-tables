# DJB


# choose some big, random number, usually prime
# loop over the bytes of our string and do something weird
# return the weird result

# "something weird" mean with the bits, which you'll learn
# in computer architecture.
def djb2(s):
    hash_var = 5381

    # creates an array of bytes
    string_bytes = s.encode()

    for b in string_bytes:
        # << operator shifts bytes over to the left by specified number
        # creates random, arbitrary number when added to itself, plus a byte
        hash_var = ((hash_var << 5) + hash_var) + b

    return hash_var


print(djb2("test") % 8)


def fnv(s):
    FNV_offset_basis = 14695981039346656037
    FNV_prime = 1099511628211

    hashed_var = FNV_offset_basis

    string_bytes = s.encode()

    for b in string_bytes:
        hashed_var = hashed_var * FNV_prime
        hashed_var = hashed_var ^ b

    return hashed_var


print(fnv("test") % 8)

# Initializing our hash table

new_list = [None] * 8


def put(key, value):
    hashed_key = djb2(key)

    idx = hashed_key % len(new_list)
    if new_list[idx] is not None:
        print(f"COLLISION: you are overwriting at {idx}")

    new_list[idx] = value


put("hello", "world")
put("world", "howdy world")


def get(key):
    hashed_key = djb2(key)

    idx = hashed_key % len(new_list)

    return new_list[idx]


print(get("hello"))


def delete(key):
    # hash it
    # modulo to get the index

    # go into the list and set to None
    hashed_key = djb2(key)

    idx = hashed_key % len(new_list)

    new_list[idx] = None


# delete("hello")
# print(get("hello"))
# print(get("world"))

# What happens if two keys hash to the same index?
# This is called a collision.
# We are currently overwriting "hello" with "foo."

put("foo", "foo monkey")
print(get("foo"))
print(get("hello"))

# Detection: check if there's a value

# How to handle?
# Linked list! Put a chain there
# Open addressing: move to the next available slot and
# put your value there instead

# put with no collision: add a node, start of LL
# put with a collision: add a node to head or tail of the LL

# How to resize to a larger hash table?
# Doubel the size of the array

# (remember if a regular array runs out of memory,
# we just double size by creating a new array and copying
# the old one over)

# Step 1: make a new array, double the size of the old one
# Step 2: iterate through old array, and old linked lists
# rehash
# Step 3: insert into new array, same way we did in the old array

# len(new_array) is bigger --> used with modulo, gives a
# different index

# Today's part of the project:
# Collision resolution with chaining --> aka make a LL work with
# the hash table
# Resizing up
# Resizing down is a stretch goal
