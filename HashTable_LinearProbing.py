
class HashTable_LP(object):
    # Constructor
    def __init__(self,size, hash_form):  
        self.item = [-1 for i in range(size)]
        self.total = 0
        self.h = hash_form
        
    def insert(self,k):
        position = self.h(str(k), len(self.item))
        if self.item[position] == k: return None
        if self.item[position] < 0: 
            self.item[position] = k
            self.total += 1
            return position
        for i in range(1, len(self.item) + 1): 
            position = (position + i) % len(self.item) 
            # Found empty bucket
            if self.item[position] < 0:
                self.item[position] = k
                self.total += 1
                return position
        return -1
    
    def search(self,k):
        position = self.h(str(k), len(self.item))
        if self.item[position] == -1: return None
        if self.item[position] == k: return self.item[position]
        for i in range(1, len(self.item) + 1):
            position = (position + 1) % len(self.item) 
            if self.item[position] == k: return self.item[position]
            if self.item[position] == -1: return None
        return None
     
    def __len__(self):
        return self.total   
   
    
if __name__ == "__main__":    
    main()
    