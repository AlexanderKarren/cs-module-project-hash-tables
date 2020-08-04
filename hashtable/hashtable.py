class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def find(self, key):
        current = self
        while (current.next is not None):
            if current.key == key:
                return current.value
            current = current.next
        return -1


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        if (capacity >= 8):
            self.capacity = capacity
        else:
            self.capacity = 8
        self.storage = [None] * capacity
        self.num_elements = 0
        pass

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        return self.num_elements / self.get_num_slots()

    def fnv1(self, key):
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211

        hashed_var = FNV_offset_basis

        string_bytes = key.encode()

        for b in string_bytes:
            hashed_var = hashed_var * FNV_prime
            hashed_var = hashed_var ^ b

        return hashed_var

    def djb2(self, key):
        hash_var = 5381

        # creates an array of bytes
        string_bytes = key.encode()

        for b in string_bytes:
            # << operator shifts bytes over to the left by specified number
            # creates random, arbitrary number when added to itself
            hash_var = ((hash_var << 5) + hash_var) + b

        return hash_var

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        idx = self.hash_index(key) % self.get_num_slots()
        self.storage[idx] = HashTableEntry(key, value)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key) % self.get_num_slots()
        self.storage[idx] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        idx = self.hash_index(key) % self.get_num_slots()
        if self.storage[idx] is None:
            return None
        return self.storage[idx].value

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        pass


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
