import random
from collections import defaultdict

class MarkovChain:
    def __init__(self, order=2):
        self.order = order
        self.model = defaultdict(list)
    
    def train(self, text):
        words = text.split()
        for i in range(len(words) - self.order):
            state = tuple(words[i:i+self.order])
            next_word = words[i+self.order]
            self.model[state].append(next_word)
    
    def generate(self, length=50):
        current_state = random.choice(list(self.model.keys()))
        output = list(current_state)
        
        for _ in range(length):
            possible_words = self.model.get(current_state, [])
            if not possible_words:
                break
            next_word = random.choice(possible_words)
            output.append(next_word)
            current_state = tuple(output[-self.order:])
        
        return ' '.join(output)

# Example usage
text = "The quick brown fox jumps over the lazy dog. The quick fox is faster than the lazy dog."
markov = MarkovChain(order=2)
markov.train(text)
print(markov.generate(20))