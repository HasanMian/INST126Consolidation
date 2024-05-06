import random

animals = [ 'monkey', 'wolf', 'tiger', 'goat', 'zebra', 'penguin', 'dinosaur', 'deer', 'frog', 'panda']

fruits = [ 'orange', 'grape', 'mango', 'apple', 'lemon', 'strawberry', 'peach', 'pear', 'watermelon', 'grapefruit']

colors = [ 'red', 'orange', 'black', 'gray', 'blue', 'green', 'purple', 'yellow', 'brown', 'white']

words = animals + fruits + colors
random_guess = random.choice(words)
print ("WORD GUESSING GAME")
if random_guess in animals:
  print('Hint: It is a mysterious Animal')
elif random_guess in fruits: 
  print('Hint: It is a mysterious Fruit')
else: 
    print('Hint: It is a mysterious Color')

user_guesses = ''
chances = 3

while chances  > 0:
    wrong_guess  = 0
    for ch in random_guess:
        if ch in user_guesses:
            print(ch, end=" ")
        else: 
            print('*', end=" ") # placeholder for letters not guessed
            wrong_guess += 1
    if wrong_guess == 0:
            print('\nCongratulations you guessed correctly:', random_guess)
            break
    guess  = input('\nGuess a letter or the entire word: ') # user can either enter a single character or guess the entire word
    user_guesses += guess

    if guess not in random_guess:
        chances -= 1
        print(f'Wrong! You have {chances} more chances')
        if chances == 0:
          print('Game Over! You Guessed inncorectly, You Lost. The correct word is: ', random_guess)
      
      
