
import codecs
import time
import numpy as np


from HashTable_Chaining import HashTable_Chain
from HashTable_LinearProbing import HashTable_LP
from WordEmbedding import WordEmbedding


def readFile(filename):
    empty = []
    with open(filename) as txt:
        for line in txt:
            piece = line.split()
            word = piece[0] 
            embedding = np.array([float(value) for value in piece[1:]])
            empty.append(WordEmbedding(word, embedding))            
    return empty

def readPairs(filename):
    empty = []
    with open(filename) as txt:
        for line in txt:
            empty.append(list(map(lambda x: x.strip(), line.split(","))))
    return empty

def CalSimilarity(e1, e2):
    return np.dot(e1, e2) / (np.linalg.norm(e1) * np.linalg.norm(e2))    



def function1(k, n): 
    return len(k) % n
def function2(k, n): 
    return ord(k[0]) % n
def function3(k, n): 
    return (ord(k[0]) * ord(k[-1]) ) % n
def function4(k, n): 
    return sum(list(map(lambda x: ord(x), k))) % n
def function5(k, n):
	 return 1 if (k == "") or (len(k) == 0) else (ord(k[0]) + 255 * function5(k[1:], n)) % n
def function6(k, n):
	 return 1 if (k == "") or (len(k) == 0) else (ord(k[0])*5 + ord(k[0]) + function1(k[1:], n)) % n


modelFile =  "glove.6B.50d.txt"
pairsFile =  "pairs.txt"

ArrOfHashFunc = [function1, function2, function3, function4, function5, function6]

print("Choose table implementation")
print("Type 1 for chaining or 2 linear probing")
choice = int(input("Choice: "))
TypeTable = None 
Hash_Function = None 
elapsed = 0

print("Choose hash function: \n")

print("1. The length of the string % n")
print("2. The ascii value (ord(c)) of the first character in the string % n")
print("3. The product of the ascii values of the first and last characters in the string % n")
print("4. The sum of the ascii values of the characters in the string % n")
print("5. The recursive formulation h("",n) = 1; h(S,n) = (ord(s[0]) + 255*h(s[1:],n))% n")
print("6. Another function of your choice")

Hash_Function = int(input("Hash Function: ")) - 1

if choice == 1:
	TypeTable = "chaining"
	print("\nBuilding hashtable with chaining using option",Hash_Function+1,"\n")
	temp = readFile(modelFile)
	table = HashTable_Chain(len(temp), ArrOfHashFunc[Hash_Function])
	start = time.time()
	for x in temp:table.insert(x)
	end = time.time()
	elapsed = (end - start)
	print("Chaining hashtable stats: ")
elif choice == 2:
	TypeTable = "linear probing"
	print("\nBuilding hashtable with linear probing\n")
	temp = readFile(modelFile)
	table = HashTable_LP(len(temp), ArrOfHashFunc[Hash_Function])
	start = time.time()
	for x in temp:table.insert(x)
	end = time.time()
	elapsed = (end - start)
	print("Linear probing hashtable stats: ")
    
    
print("Number of nodes:",(len(table)))
print("Running time for",TypeTable,elapsed,"\n")



pairs = readPairs(pairsFile)
print("Word similarities found: ")
total = 0
for (x1, x2) in pairs:
	start = time.time()
	e1 = table.find(x1)
	e2 = table.find(x2)
	end = time.time()
	total += (end - start)
	if e1 == None or e2 == None: 
		print(table.find(x1),"and",table.find(x2))
		continue
	emb= CalSimilarity(e1.emb, e2.emb)
	print("Similarity between",x1,"and",x2,"=",emb)

