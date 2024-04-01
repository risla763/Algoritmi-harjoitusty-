class Node:
    def __init__(self):
        self.children = {}
        self.note = None #nuotti
        self.weight = 0
        self.value = False


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, notes_list):
        node = self.root
        print(node, "self_root")
        print(notes_list, "notes_list")
        for note in notes_list:
            print(note, "testi")
            if note not in node.children: #onko nuotti jo eka root.noden lapsissa
                node.children[note] = Node() 

                print(node.children[note] ,"uusi lapsi")
            node = node.children[note]
            node.weight += 1
            print(node.weight,"uuden lapsen paino")

        node.value = True

    def print_trie(self, node=None, depth=0):
        if node is None:
            node = self.root
        for pair, child_node in node.children.items():
            print("  " * depth + str(pair) + " -> " + str(child_node.value) + " (Weight: " + str(child_node.weight) + ")")
            self.print_trie(child_node, depth + 1)

    def search(self, notes): #ehkä turha
        #print(notes) #cb mitä syötetään
        node = self.root
        for note in notes:
            print(note)
            if note not in node.children:
                return None
            node = node.children[note]
            print(node.children, "tässä lapsi")
        return node.value if node else None

trie = Trie()
notes_list = "cbeaf" 
trie.insert(notes_list)  
trie.print_trie()
notes_list2 = "cbeafaa"
trie.insert(notes_list2) 
trie.print_trie()
trie.search("cbeafgcacb")
#tämä vielä isosti kesken!

