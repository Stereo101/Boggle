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
	def getAllWordsFromNode(self,tri,words,i,k):
		fingers = finger(k,i,{},tri,"").getFingers(self)
		while(len(fingers) > 0):
			f = fingers.pop()
			if(f.triPtr.isWord and f.word not in words):
				words[f.word] = True
				print(f.word)
			fingers.extend(f.getFingers(self))
		return words
	def getAllWords(self,tri,words):
		for i in range(5):
			for k in range(5):
				self.getAllWordsFromNode(tri,words,i,k)
class finger:
	def __init__(self,x,y,path,triPtr,word):
		self.word = word
		self.x = x
		self.y = y
		self.path = deepcopy(path)
		self.path[(x,y)] = True
		self.triPtr = triPtr
	def getFingers(self,bog):
		fingers = []
		for i in [-1,0,1]:
			for k in [-1,0,1]:
				xcord = k+self.x
				ycord = i+self.y
				if((xcord,ycord) not in self.path and ycord < 5 and xcord < 5 and ycord >= 0 and xcord >= 0):
					c = bog.bog[i+self.y][k+self.x]
					if(c in self.triPtr.adj):
						fingers.append(finger(xcord, ycord, self.path, self.triPtr.adj[c],self.word+c))
		return fingers
					
					

def loadTriFromDictFile(filename):
	tri = TriNode('/')
	for w in open(filename,"r").read().splitlines():
		tri.insert(w)
	return tri


wordDict = {}
for w in open("wordlist","r").read().splitlines():
	wordDict[w] = True
tri = loadTriFromDictFile("wordlist")
b = boggle("abcdefghijklmnopqrstuvwxy")
print("Is 'g' a word?",tri.hasWord('g'))
b.show()
words = {}
b.getAllWords(tri,words)
for i in words.keys():
	print(i,"in tri?",tri.hasWord(i),". is in Dict?",i in wordDict)
