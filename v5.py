#!/usr/bin/python3
# This needs to be documented!!!!
from tkinter import *
from rectver1 import veriffield
import string
#import pdb

def checkString(astring):
  if len(astring) !=10:
      return False
  if not astring[0] in string.digits:
      return False
  if not astring[1] in string.digits:
      return False
  if not astring[2] in string.ascii_uppercase:
      return False
  if not astring[3] in string.digits:
      return False
  if not astring[4] =='?':
      return False
  if not astring[5] =='(':
      return False
  if not astring[6] in string.ascii_uppercase:
      return False
  if not astring[7] in string.ascii_uppercase:
      return False
  if not astring[8] == ')':
      return False
  if not astring[9] in string.digits:
      return False
  return True


##-------------------------------------
class veriffield():
   
   def __init__(self, code, weight, votes, colour,val,ages):#all the code must be here
      self.code = code
      self.weight = weight
      self.votes = votes
      self.colour = colour
      self.val =   val
      self.ages = ages
      
     
   def getCode(self):
     return self.code
   
   def getWeight(self):
     return self.weight

   def getVotes(self):
     return self.votes

   def getColour(self):
     return self.colour

   def getVal(self):
     return self.val

   def getAges(self):
     return self.ages

   def __str__(self):
       return ("[%d,%d]:%d - %s"&(self.code,self.weight,self.votes,self.getcolour(),self.getval,self.ages,self.getinvalidcode()))


##------------------------------------
                            
class RecCounter():
   def __init__(self):
      self.reset()
      
   def reset(self):#all counters for each question 
      self.count  = 0
      self.countinvalidcode=0
      self.countq2=0
      self.countvotes=0
      self.countcolour=0
      self.countq5=0
      self.countq6=0
      self.total=0
      self.average=0
      self.countq7=0
      self.total1=0


   def add(self, veriffield):
## displays all the answers in GUIs
     
      #Q1- count number of invalid codes in field
       if not checkString(veriffield.getCode()):
           self.countinvalidcode +=1

       #q2-Calculate percentage of numbers in weight that lie between 1544.505 and 1795.023
       self.count +=1
       if veriffield.getWeight() >= 1544.505 and veriffield.getWeight() <= 1795.023:
           self.countq2 +=1
       #q3- Calculating total votes
       #self.count+=1
       if veriffield.getVotes() >= 1125:
           self.countvotes+=1

       #q4-Count the number of strings in the field [colour] that are more than 3 characters long
       if len(veriffield.getColour())>3:
           self.countcolour +=1

       #q5-count number of colds in the field
       if veriffield.getVal()== 'Cold':
           self.countq5+=1

       #q6-count number of ages between 38 and 74
       if veriffield.getAges()>= 38 and veriffield.getAges()<= 74:
           self.countq6 +=1
           self.total = self.total + veriffield.getAges()

        #q7-count the lines where val's have the value [hot] or votes is less than 1508
           #self.count+=1
       if veriffield.getVal()=='Hot' or veriffield.getVotes() <1508:
           self.countq7 +=1

        
           
   def numberofinvalidcodes(self):
       return self.countinvalidcode

   def percentageofweight(self):
       return"%.2f" %((self.countq2/self.count)*100)

   def percentageofvotes(self):
       return"%.2f" % ((self.countvotes/self.count)*100)

   def lengthofcolours(self):
       return"%.2f" % self.countcolour

   def numberofcoldvals(self):
       return"%.2f" % self.countq5
           
   def numberofages(self):
       return"%.2f" % ((self.total/self.countq6))

   def countnumberofvalandvotes(self):
       return"%.2f" % ((self.countq7))
      
 #def nuumberofinvalidcodes(self): return self.countinvalidcode
   
##------------------------------------
class RecReader():
   def __init__(self, filename, counter, recgui):
     
      self.gui = recgui
      self.counter = counter
      self.infile = open(filename, 'r')
      if not self.infile:
         self.gui.fileNotFound()    # this leads to studying exceptions
      else:
         self.run()
       
         
   def run(self):
      
      firstline = True
      for line in self.infile:
         if firstline:
            firstline = False
            continue
         fields = line.split(',')
         code=fields[0]
         weight=float(fields[1])
         votes=int(fields[2])
         colour=fields[3]
         val= fields[4]
         ages= int(fields[5])                   
         self.counter.add( veriffield(code, weight, votes, colour, val, ages))
         
         
      self.infile.close()
      self.gui.notify()
      
#this is gui the interface for which the questions       
class RecGUI():
   def __init__(self, root):
      self.ok = False # indicate if there has been a valid read
      self.counter = RecCounter()
      
      Label(root,font="mono -24 bold", justify="center", 
      text="Welcome Natasha Owusu-Amankrah Rectangles").grid(row=0, column=0, columnspan=2, sticky=N)
           
      Label(root,text="Filename", width=10).grid(row=1, column=0, sticky=E)
      self.flname = Entry(root, width=10, bg="light blue")
      self.flname.grid(row=1, column=1, sticky=W)
      
      Button(root,text="Go", command=self.process_file).grid(row=1,column=1)
     
       
      Label(root, text="Q1-No of invalid codes",font=12, width=30).grid(row=2, column=0, sticky=E)
      self.countinvalidcode= Label(root,font=12 ,width=10)
      self.countinvalidcode.grid(row=2,column=2, sticky=W)
      
      Label(root, text=" Q2- The percentage of weight",font=12, width=30).grid(row=3, column=0, sticky=E)
      self.mypercentageofweight=Label(root, width=10)
      self.mypercentageofweight.grid(row=3,column=2, sticky=W)
      
      Label(root, text="Q3-Percentage_votes",font=12,width=30).grid(row=4, column=0, sticky=E)
      self.mypercentageofvotes=Label(root, font=12 ,width=10)
      self.mypercentageofvotes.grid(row=4,column=2, sticky=W)

      Label(root, text="Q4- length of colours ",font=12, width=30).grid(row=5, column=0, sticky=E)
      self.mylengthofcolours=Label(root,font=12 ,width=10)
      self.mylengthofcolours.grid(row=5,column=2, sticky=W)

      Label(root, text="Q5-number of cold values",font=12, width=30).grid(row=6, column=0, sticky=E)
      self.mynumberofcoldvals=Label(root,font=12, width=10)
      self.mynumberofcoldvals.grid(row=6,column=2, sticky=W)

      Label(root, text="Q6-number of ages",font=12, width=30).grid(row=6, column=0, sticky=E)
      self.mynumberofages=Label(root,font=12 ,width=10)
      self.mynumberofages.grid(row=6,column=2, sticky=W)


      Label(root, text="Q7-Number of values and votes",         font=12, width=30).grid(row=7, column=0, sticky=E)
      self.mycountnumberofvalandvotes=Label(root,font=12 ,width=10)
      self.mycountnumberofvalandvotes.grid(row=7,column=2, sticky=W)      
   def process_file(self, ev=None):
      filename =self.flname.get() #self.flname.get()
      
      if len(filename) > 8:    #chance it may be ok
         self.ok = True
         self.counter.reset()
         self.reader=RecReader(filename, self.counter, self)
      
   def fileNotFound(self):
      self.ok = False
      
   def message(self, amssg):
      self.mssg['text']=amssg
      
   def notify(self):
      if self.ok:
         self.countinvalidcode['text']  = str(self.counter.numberofinvalidcodes())
         self.mypercentageofweight['text'] = str (self.counter.percentageofweight())
         self.mypercentageofvotes['text'] = str (self.counter.percentageofvotes())
         self.mylengthofcolours['text'] = str (self.counter.lengthofcolours())
         self.mynumberofcoldvals['text'] = str (self.counter.numberofcoldvals())
         self.mynumberofages['text'] = str (self.counter.numberofages())
         self.mycountnumberofvalandvotes['text'] = str (self.counter.countnumberofvalandvotes())
         
  

   ##########################
   ### It all starts here ###
   ##########################
      
if __name__ == "__main__":
   top = Tk()
   top.geometry("800x500")
   top.title("Welcome Natasha Owusu-Amankrah Rectangles")
   top.grid()
   
   app = RecGUI(top)
   
   top.mainloop()
      

