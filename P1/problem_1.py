
class LRU_Cache(object):

    def __init__(self, capacity):
        # Initialize class variables
        self.cache_struct = {}
        self.initalized_items = []
        self.capacity = capacity

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        return self.cache_struct.get(key, -1)

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item.
        if self.capacity is None or self.capacity <= 0:
            return -1

        if len(self.cache_struct) >= self.capacity:
            self.cache_struct.pop(self.initalized_items[0])
            self.initalized_items = self.initalized_items[1:]

        if self.cache_struct.get(key) is None:
            self.cache_struct[key] = value
            self.initalized_items.append(key)


# Test Cases
# 1. Test set with mix values
case_1 = LRU_Cache(3)
print(case_1.set("test_case_1", "key_case"))  
# None
print(case_1.set("test_case_2", 2000))  
# None
print(case_1.set(33, "test_key"))  
# None

# 2. Test set will nulls and zeros
case_2 = LRU_Cache(0)
print(case_2.set("key", "value"))  
# -1
print(case_2.set(0, 0))  
# -1

case_2 = LRU_Cache(4)
print(case_2.set(None, None))  
# None
print(case_2.set(0, None))  
# None
print(case_2.get(4))  
# -1
print(case_2.get(None))  
# -1

# 3. Test get
case_3 = LRU_Cache(3)
print(case_3.set(1, 1)) 
# None
print(case_3.set(2, 2))  
# None
print(case_3.set("three", "three"))  
# None
print(case_3.set(4, 4))  
# None

print(case_3.get(1))  
# -1
print(case_3.get(2))  
# 2
print(case_3.get("three"))  
# "three"

case_3 = LRU_Cache(4)
print(case_3.set("three", "three")) 
# None
print(case_3.set("three", 3))  
# None
print(case_3.get("three"))  
# three


# 4. Test with negative value
case_4 = LRU_Cache(-3)
print(case_4.set(1, 1)) # -1

print(case_4.set(0, 0)) # -1

# 5. Test with null capacity
case_5 = LRU_Cache(None)
print(case_5.set(1, 1)) # -1

print(case_5.set(0, 0)) # -1