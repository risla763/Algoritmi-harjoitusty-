class Node:
    def __init__(self):
        self.value = None
        self.children = [None,None]

class Node:
    def __init__(self):
        self.children = {}
        self.value = None

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, notes, value):
        node = self.root
        for i in range(len(notes) - 1):
            pair = notes[i:i+2]
            if pair not in node.children:
                node.children[pair] = Node()
            node = node.children[pair]
        node.value = value

    def search(self, notes):
        node = self.root
        for i in range(len(notes) - 1):
            pair = notes[i:i+2]
            if pair not in node.children:
                return None
            node = node.children[pair]
        return node.value if node else None

trie = Trie()
notes_list = "cbefgab" #tämä abc notaatiota..pitää muuttaa numeroiksi
for i in range(len(notes_list) - 1):
    notes_pair = notes_list[i:i+2]
    trie.insert(notes_pair, notes_list[i+2:])

print(trie.search("cb"))
print(trie.search("be"))  
print(trie.search("fg"))  
print(trie.search("ga"))  


