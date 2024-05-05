import random

animals = [ 'monkey', 'wolf', 'tiger', 'goat', 'zebra', 'penguin', 'dinosaur', 'deer', 'frog', 'panda']

fruits = [ 'orange', 'grape', 'mango', 'apple', 'lemon', 'strawberry', 'peach', 'pear', 'watermelon', 'grapefruit']

colors = [ 'red', 'orange', 'black', 'gray', 'blue', 'green', 'purple', 'yellow', 'brown', 'white']

words = animals + fruits + colors
random_guess = random.choice(words)
