import player as p
import random

class Game:

  def __init__(self):
    #Var for number of guesses made
    self.guesses = 0
    #Var for mystery player
    self.targetplayer = random.choice(list(p.playerDict))
    #Var for current guess
    self.guess = ""
    #Holds possibly results
    self.checklist = ["❌", "❌", "❌", "↑↑", "↑↑", "↑↑"]
    print("Game notes: Only players who are in the top five of minutes per game on their team can be guessed. Names must also be typed exactly including spelling and apostrophes. Also capitalization must be right \n")

  def checkValidity(self):
    check = True
    while check:
      check = False
      self.guess = input("Guess a player: ")
      try:
        p.playerDict[self.guess]
      except:
        print("Not a valid player\n")
        self.similarity()
        check = True

  def similarity(self):
    slist = []
    count = 0
    repeat = False
    guess = self.guess
    for key in p.playerDict:
      guess.lower()
      key.lower()
      guess.strip(" ")
      key.strip(" ")
      for (a,b) in zip(guess, key):
        if a == b:
          count += 1
      if(count > 4):
        slist.append(key)
      count = 0
      for(a,b) in zip(reversed(guess),reversed(key)):
        if a == b:
          count += 1 
      if(count > 4):
        for j in slist:
          if key == j:
            repeat = True
        if repeat == False:
          slist.append(key)
        repeat = False
      count = 0

    print("Did you mean: ")
    for i in slist:
      print(i,end = " | ")
    print("\n")
    
  
  def checkGuess(self):
    self.checkValidity()
    #Checks if conf, div, team are same and if so, leaves green mark
    self.guesses += 1
    i = 0
    while i<3 :
      if(p.playerDict[self.targetplayer][i] == p.playerDict[self.guess][i]):
        self.checklist[i] = "✅"
      else:
        self.checklist[i] = "❌"
      i += 1
    #Checks rebounds, assists, points and sets to according mark  
    while i < 6:
      if(p.playerDict[self.targetplayer][i] > p.playerDict[self.guess][i]):
        self.checklist[i] = "↑↑"
      elif(p.playerDict[self.targetplayer][i] < p.playerDict[self.guess][i]):
        self.checklist[i] = "↓↓"
      elif(p.playerDict[self.targetplayer][i] == p.playerDict[self.guess][i]):
        self.checklist[i] = "✅"
      i += 1
      

  def printResult(self):
    print("Conference | Division | Team | Rebounds | Assists | Points")
    print("   "+self.checklist[0] + "      |    "+self.checklist[1]+"    |  "+self.checklist[2]+"  |    "+self.checklist[3]+"    |    "+self.checklist[4]+"   |   "+self.checklist[5]+"      \n")

  def stillRunning(self):
    if self.guess == self.targetplayer:
      print("That's correct!")
      return False
    elif self.guesses < 8:
      return True
    else:
      print("You ran out of guesses. The player was ", self.targetplayer)
      return False
    