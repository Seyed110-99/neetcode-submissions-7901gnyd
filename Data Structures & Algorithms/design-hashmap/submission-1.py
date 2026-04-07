class MyHashMap:

    def __init__(self):
        
        self.hash = []
    def put(self, key: int, value: int) -> None:
        
        if key > len(self.hash) - 1:
            for i in range(key - len(self.hash) + 1):
                self.hash.append([])
        
        self.hash[key] = [key, value]

    def get(self, key: int) -> int:
        
        if key >= len(self.hash):
            return -1
        else:
            if len(self.hash[key]) > 1:
                return self.hash[key][1]
            else:
                return -1

    def remove(self, key: int) -> None:
        if key < len(self.hash):
            self.hash.pop(key)



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)