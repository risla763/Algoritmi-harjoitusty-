class Node:
    def __init__(self):
        self.children = {}
        self.value = None #nuotti
        self.weight = 0


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, notes, notes_list):
        node = self.root
        print(notes_list, "notes_list")
        for note in notes_list:
            print(note, "testi")
            if note not in node.children: #onko nuotti jo solmun lapsissa
                node.children[note] = Node() #{} tänne node.children listaan nuotti
                node.children[note].weight += 1
            else:
                node.children[note].weight += 1 #paino
                print(node.children[note].weight, "painotukset")
            node = node.children[note] 
        if node.value is None: #tässä mitä tulee keyn jälkeen
            node.value = False

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
notes_list = "cbeafgcacb" 
trie.insert("c", notes_list)  
trie.print_trie()
trie.search("cbeafgcacb")
#tämä vielä isosti kesken!

