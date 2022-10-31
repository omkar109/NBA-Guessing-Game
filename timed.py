import player as p
import random

class Timed:

  def __init__(self):
    self.guess = ""
    #Holds type of parameters
    self.plist = []
    #Holds actual parameters
    self.olist = []
    #Holds players
    self.playlist = []
    self.categories = int(input("How many categories? (1-3) "))
    self.types = ["Conference", "Division", "Rebounds", "Assists", "Points"]
    self.tlist = {
      "Conference": ["West", "East"],
      "Division" : ["Pacific", "Southwest", "Northwest","Southeast", "Atlantic", "Central"],
      "Rebounds": [4,6,9],
      "Assists" : [3,6,9],
      "Points" : [8,12,16,20,23]
    }
    self.glist = {
      "Conference": 0,
      "Division" : 1,
      "Rebounds": 3,
      "Assists" : 4,
      "Points" : 5
    }

  def execute(self):
    self.assign()
    self.getPlayers()
    players = len(self.playlist)
    while players > 0:
      print(players, "more players fit the criteria: ")
      self.checkValidity()
      count = self.playlist.count(self.guess)
      if count > 0:
        print("Correct! \n")
        players -= 1
      else:
        print("Nope! \n")
      count = 0


  #Defines the parameters of the player you must name
  def assign(self):
    self.plist = random.sample(self.types, self.categories)
    print(self.plist)
    for i,value in enumerate(self.plist):
      self.olist.append(random.choice(self.tlist[value]))
    print(self.olist)

  def getPlayers(self):
    while not self.playlist:
      keep = True
      count = 0
      for key in p.playerDict:
        keep = True
        for i in self.plist:
          if keep == True:
            if i == "Conference":
              if key[0] == self.olist[count]:
                keep = True
              else:
                keep = False
            elif i == "Division":
              if key[1] == self.olist[count]:
                keep = True
              else:
                keep = False
            elif i == "Rebounds":
              if p.playerDict[key][3] > self.olist[count]:
                keep = True
              else:
                keep = False
            elif i == "Assists":
              if p.playerDict[key][4] > self.olist[count]:
                keep = True
              else:
                keep = False
            elif i == "Points":
              if p.playerDict[key][5] > self.olist[count]:
                keep = True
              else:
                keep = False
            count += 1
        if keep == True:
          self.playlist.append(key)
        count = 0
  #  print(self.playlist)

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
      
      
    