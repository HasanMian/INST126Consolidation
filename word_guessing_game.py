import random

animals = [ 'monkey', 'wolf', 'tiger', 'goat', 'zebra', 'penguin', 'dinosaur', 'deer', 'frog', 'panda']

fruits = [ 'orange', 'grape', 'mango', 'apple', 'lemon', 'strawberry', 'peach', 'pear', 'watermelon', 'grapefruit']

colors = [ 'red', 'orange', 'black', 'gray', 'blue', 'green', 'purple', 'yellow', 'brown', 'white']

words = animals + fruits + colors
random_guess = random.choice(words)
print ("WORD GUESSING GAME")
if random_guess in animals:
  print('Hint: It is a mysterious Animal')
elif random_guess in fruit: 
  print('Hint: It is a mysterious Fruit')
else: 
    print('Hint: It is a mysterious Color')

user_guesses = ''
chances = 3

while chances  > 0:
    wrong_guess  = 0
    for ch in random_guess:
      
