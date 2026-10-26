class LRUCache:

    def __init__(self, capacity: int):
      self.size = capacity  
      self.cache = OrderedDict()
     

    def get(self, key: int) -> int:
        
        
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1
        
    def put(self, key: int, value: int) -> None:
        


        if key in self.cache:
            self.cache.pop(key)
        
        if len(self.cache)==self.size:
            self.cache.popitem(last=False)
        self.cache[key]=value