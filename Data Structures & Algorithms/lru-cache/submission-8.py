class LRUCache:

    def __init__(self, capacity: int):
      self.size = capacity  
      self.cache = defaultdict(int)
      self.keys=[]

    def get(self, key: int) -> int:
        
        
        if key in self.cache:
            self.keys.remove(key)
            self.keys.append(key)
            return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache)==self.size:
                self.cache.pop(self.keys[0])
                self.keys.pop(0)
        self.cache[key]=value
        if key in self.keys:
            self.keys.remove(key)
        self.keys.append(key)
