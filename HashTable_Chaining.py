
class HashTable_Chain(object):
    # Constructor
    def __init__(self, size, hash_form):  
        self.bucket = [[] for i in range(size)]
        self.n = 0
        self.h = hash_form
                      
    def insert(self,k):
        b = self.h(str(k), len(self.bucket))
        if k not in self.bucket[b]:
            self.bucket[b].append(k)
            self.n += 1
            
    def search(self,k):
        b = self.h(str(k), len(self.bucket))
        try:
            i = self.bucket[b].index(str(k))
        except:
            i = -1
        return None if i == -1 else self.bucket[b][i]
	
    def __len__(self):
        return self.n
    
    

if __name__ == "__main__":    
    main()
    
    
    