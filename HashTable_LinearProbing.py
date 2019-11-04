
class HashTable_LP(object):
    # Constructor
    def __init__(self,size, hash_form):  
        self.item = [-1 for i in range(size)]
        self.n = 0
        self.h = hash_form
        
    def insert(self,k):
        pos = self.h(str(k), len(self.item))
        if self.item[pos] == k: return None
        if self.item[pos] < 0: 
            self.item[pos] = k
            self.n += 1
            return pos
        for i in range(1, len(self.item) + 1): 
            pos = (pos + i) % len(self.item) 
            # Found empty bucket
            if self.item[pos] < 0:
                self.item[pos] = k
                self.n += 1
                return pos
        return -1
    
    def find(self,k):
        pos = self.h(str(k), len(self.item))
        if self.item[pos] == -1: return None
        if self.item[pos] == k: return self.item[pos]
        for i in range(1, len(self.item) + 1):
            pos = (pos + 1) % len(self.item) 
            if self.item[pos] == k: return self.item[pos]
            if self.item[pos] == -1: return None
        return None
     
    def __len__(self):
        return self.n   
   

    
if __name__ == "__main__":    
    main()
    