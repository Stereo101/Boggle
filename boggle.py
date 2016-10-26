import sys
from copy import deepcopy
class TriNode:
	def __init__(self,char):
		self.char = char
		self.isWord = False
		self.adj = {}
		
	def insert(self,word):
		if(len(word)==0):
			self.isWord = True
		else:
			if(word[0] not in self.adj):
				self.adj[word[0]] = TriNode(word[0])
			self.adj[word[0]].insert(word[1:])
	def hasWord(self,word):
		cur = self
		for c in word:
			if(c not in cur.adj):
				return False
			cur = cur.adj[c]
		return cur.isWord

class boggle:
	def __init__(self,stringIn):
		if(len(stringIn) != 25):
			print("Boggle string must be 25 chars exactly")
			sys.exit()
		self.bog = ['.']*5
		for i in range(5):
			self.bog[i] = ['.']*5
			for k in range(5):
				self.bog[i][k] = stringIn[i*5 + k]
	def show(self):
		print()
		for a in self.bog:
			for b in a:
				print(b,end="")
			print()
	def getAllWords(self,tri):
		words = {}
		for i in range(5):
			for k in range(5):
				fingers = finger(k,i,{},tri,"").getFingers(self,tri)
				while(len(fingers) > 0):
					for f in fingers:
						fingers.remove(f)
						if(f.triPtr.isWord and f.word not in words):
							words[f.word] = True
							print(f.word)
						fingers.extend(f.getFingers(self,tri))
		return words
class finger:
	def __init__(self,x,y,path,triPtr,word):
		self.word = word
		self.x = x
		self.y = y
		self.path = deepcopy(path)
		self.path[(x,y)] = True
		self.triPtr = deepcopy(triPtr)
	def getFingers(self,bog,tri):
		fingers = []
		for i in range(-1,2):
			for k in range(-1,2):
				if((i+self.y,k+self.x) not in self.path and i+self.y < 5 and k+self.x < 5 and i+self.y > 0 and k+self.x > 0):
					if(bog.bog[i+self.y][k+self.x] in tri.adj):
						fingers.append(finger(k+self.x,i+self.y,self.path,tri.adj[bog.bog[i+self.y][k+self.x]],self.word+bog.bog[i+self.y][k+self.x]))
		return fingers
					
					

def loadTriFromDictFile(filename):
	tri = TriNode('/')
	for w in open(filename,"r").read().splitlines():
		tri.insert(w)
	return tri



tri = loadTriFromDictFile("wordlist")
b = boggle("abcdefghijklmnopqrstuvwxy")
b.show()

print(b.getAllWords(tri))
