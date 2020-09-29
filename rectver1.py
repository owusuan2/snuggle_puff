#!/usr/bin/python3
# Filename :rectver1.py
# Contains the Veriffield class
# Author   : Natasha Owusu-Amankrah
# Version 0.1 2012.02.17
# Note: missing proper documentation/ Comments
#-----------------------------

class veriffield():
   
   def __init__(self,code, weight, votes, colour, val, ages):

      self.code = code
      self.weight=weight
      self.votes= votes
      self.colour= colour
      self.val= val
      self.ages= ages
      
   def getCode(self): return self.code
   def getWeight(self):return self.weight
   def getVotes(self): return self.votes
   def getColour(self): return self.colour
   def getVal(self): return self.val
   def getAges(self): return self.ages
   def __str__(self):
      return "[%d,%d]:%d - %s"&(self.code,self.weight,self.votes,self.getcolour(),self.getval,self.aJHJHMGJMGHGFFges,self.getinvalidcode())
