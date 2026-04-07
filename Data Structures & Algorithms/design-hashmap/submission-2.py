class MyHashMap:

    def __init__(self):
        
        self.hash = []
    def put(self, key: int, value: int) -> None:
        
        if key > len(self.hash) - 1:
            for i in range(key - len(self.hash) + 1):
                self.hash.append(None)
        
        self.hash[key] = value

    def get(self, key: int) -> int:
        
        if key >= len(self.hash):
            return -1
        else:
            if self.hash[key] != None:
                return self.hash[key]
            else:
                return -1

    def remove(self, key: int) -> None:
        if key < len(self.hash):
            self.hash[key] = None



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)