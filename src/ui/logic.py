from algorithms.markov_chain import MarkovChain

class Logic:
    def __init__(self, markov_chain):
        self.lista = []
        self.markov_chain = MarkovChain() #YKSI AINOA MARKOV CHAINN

    def generate_music(self):
        print("HALOOOOOO")
        self.markov_chain.choose_key() #kutsuu markovin ketjua
