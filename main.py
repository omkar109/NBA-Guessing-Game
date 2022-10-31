from game import Game
from timed import Timed
type = input("Which Game, Normal or Timed? ")

if type == "Normal":
  game = Game()
  
  game.checkGuess()
  game.printResult()
  
  while game.stillRunning():
    game.checkGuess()
    game.printResult()

if type == "Timed":
  time = Timed()
  time.execute()
  