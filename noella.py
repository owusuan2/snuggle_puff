#!/usr/bin/python3
# This needs to be documented!!!!
from tkinter import *
from math import sqrt
#import pdb
##-------------------------------------
class Rectangle():
   
   def __init__(self, age, amount, code, channels, myplant, direct):#all the code must be there
      self.age = age
      self.amount= amount
      self.code= code
      self.channels= channels
      self.myplant= myplant
      self.direct= direct
     
   def getAge(self): return self.age
   def getAmount(self): return self.amount
   def getCode(self): return self.code
   def getChannels(self): return self.channels
   def getMyplant(self): return self.myplant
   def getDirect(self): return self.direct

##------------------------------------
                            
class RecCounter():
   def __init__(self):
      self.reset()
      
   def reset(self):
      self.totalage  = 0
##      self.myamount = 0
##      self.count = 0
##      self.countinvalidcode = 0
##      self.percentage = 0 
##      self.mychannel = 0
##      self.myminplant = ''
##      self.counts = {}
##      self.mymin = 9999999
##      self.upscount = 0
##      self.downcount = 0
##      self.direction = 0
##      self.mynum = 0
##      self.mycount = 0 # for q7
      
   def add(self, rectangle):
      #Q1- Total ofn age < 108
      if rectangle.getAge() < 108:
         self.totalage = self.totalage + rectangle.getAge()
         
   #def get_max_diag(self): return self.max_diag
   def get_age(self): return self.totalage
   

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
         age = int(fields[0])
         amount = float(fields[1])
         code = fields[2]
         channels = int(fields[3])
         myplant= fields[4]
         direct = fields[5]
         self.counter.add( Rectangle(age, amount, code, channels, myplant, direct))
         
      self.infile.close()
      self.gui.notify(=)
      
      
class RecGUI():
   def __init__(self, root):
      self.ok = False # indicate if there has been a valid read
      self.counter = RecCounter()
      
      Label(root,font="mono -36 bold", justify="center", 
             text="Welldone Noella Amani Rectangles").grid(row=0, column=0, columnspan=3, sticky=N)
           
      Label(root, text="filename", width=10).grid(row=1, column=0, sticky=E)
      self.flname = Entry(root, width=10, bg="cornsilk")
      self.flname.grid(row=1, column=1, stick=W)
      
      Button(root,text="Go", command=self.process_file).grid(row=1,column=2)
      
      Label(root, text="Total Age", width=10).grid(row=2, column=1, sticky=E)
      self.totalage= Label(root, width=7)
      self.totalage.grid(row=2,column=2, sticky=W)
      
##      Label(root, text="Total Area", width=10).grid(row=3, column=1, sticky=E)
##      self.areaLbl=Label(root, width=7)
##      self.areaLbl.grid(row=3,column=2, sticky=W)
      
##      Label(root, text="Max Diag", width=10).grid(row=4, column=1, sticky=E)
##      self.maxDgLbl=Label(root, width=7)
##      self.maxDgLbl.grid(row=4,column=2, sticky=W)
##
##      Label(root, text="Max Diag extra", width=10).grid(row=5, column=1, sticky=E)
##      self.maxDgLble=Label(root, width=7)
##      self.maxDgLble.grid(row=5,column=2, sticky=W)
##
##      Label(root, text="New extra ", width=10).grid(row=6, column=1, sticky=E)
##      self.maxDgLbles=Label(root, width=7)
##      self.maxDgLbles.grid(row=6,column=2, sticky=W)
##
##      Label(root, text="Last line extra ", width=10).grid(row=7, column=1, sticky=E)
##      self.maxDgLbless=Label(root, width=7)
##      self.maxDgLbless.grid(row=7,column=2, sticky=W)
      
      
   def process_file(self, ev=None):
      filename = self.flname.get()
      
      if len(filename) > 4:    #chance it may be ok
         self.ok = True
         self.counter.reset()
         self.reader=RecReader(filename, self.counter, self)
      
   def fileNotFound(self):
      self.ok = False
      
   def message(self, amssg):
      self.mssg['text']=amssg
      
   def notify(self):
      if self.ok:
         self.totalage['text']  = str(self.counter.get_age())
         #self.areaLbl['text'] = str(self.counter.get_area())
         #self.maxDgLbl['text']= "%6.2f" % self.counter.get_max_diag()

##         self.maxDgLble['text']= "%6.2f" % self.counter.get_max_diag()
##         self.maxDgLbles['text']= "%6.2f" % self.counter.get_max_diag()
##         self.maxDgLbless['text']= "%6.2f" % self.counter.get_max_diag()
   ##########################
   ### It all starts here ###
   ##########################
      
if __name__ == "__main__":
   top = Tk()
   top.geometry("800x500")
   top.title("Welldone Noella Amani Rectangles")
   top.grid()
   
   app = RecGUI(top)
   
   top.mainloop()
      
