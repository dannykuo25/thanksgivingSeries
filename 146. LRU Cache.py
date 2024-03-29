# Approach 1: Ordered dictionary
# time: O(1), space: O(capacity)
from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity):
        self.capacity = capacity
        print('self =', self)
        print('self type =', type(self))
    
    def get(self, key):
        if key not in self:
            return -1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            self.popitem(last = False)

# Approach 2: Hashmap + DoubleLinkedList



# Your LRUCache object will be instantiated and called as such:
capacity = 2
key, value = 2, 4
obj = LRUCache(capacity)
param_1 = obj.get(key)
print(param_1)
obj.put(key,value)
    