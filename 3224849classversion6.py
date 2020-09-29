#!/usr/bin/python3
import string
from rectver1 import Rectangle

 
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
##---------------------
## Counter class
##---------------------
class Counter():
   def __init__(self):
        self.count  = 0
        self.countinvalidcode=0
        self.countq2 =0
        self.countvotes=0
        self.countcolour=0
        self.countq5=0
        self.countq6=0
        self.total=0
        self.average=0
        self.countq7=0
        self.total1=0
##      self.height = 0#variable for calculating the largest width
##      self.totalh = 0#variable for calculating the total height

   
   def add(self, rectangle):
##      self.count += 1  # every time I add a Rectangle I add 1


      # Q1-To calculate number of values in this field that match the format given

        if not checkString(rectangle.getCode()):
           self.countinvalidcode+=1
           
      #q2-Calculate percentage of numbers in weight that lie between 1544.505 and 1795.023
        self.count +=1
        if rectangle.getWeight() >= 1544.505 and rectangle.getWeight() <= 1795.023:
            self.countq2 +=1
         
##         #q3- Calculating total votes
        self.count+=1
        if rectangle.getVotes() >= 1125:
            self.countvotes+=1
##          #self.totalh=self.totalh + rectangle.getHeight()
##
##      #q4-Count the number of strings in the field [colour] that are more than 3 characters long
        if len(rectangle.getColour())>3:
           self.countcolour +=1

        #q5-count number of colds in the field
        if rectangle.getVal()== 'Cold':
           self.countq5+=1

        #q6-count number of ages between 38 and 74
        if rectangle.getAges()>= 38 and rectangle.getAges()<= 74:
           self.countq6 +=1
           self.total = self.total + rectangle.getAges()

        #q7-count the lines where val's have the value [hot] or votes is less than 1508
           self.count+=1
        if rectangle.getVal()=='Hot' and rectangle.getVotes() <1508:
           self.countq7 +=1
           #self.total1=self.total1 +rectangle.getVotes()


   def numberofinvalidcodes(self):
      return ("Number of codes that do not match format: %d"%(self.countinvalidcode))


   def percentageofweight(self):
      return ("Percentage of weight between 1544.505 and 19795.023: %.2f" % ((self.countq2/self.count)*100))

   def percentageofvotes(self):
      return ("Percentage of votes more than or equal to 1125: %.2f" %((self.countvotes/self.count)*100))

   def lengthofcolours(self):
      return("Length of colours that are more than 3:",(self.countcolour))

   def numberofcoldvals(self):
      return("Number of cold values in this field:",(self.countq5))

   def numberofages(self):
      return("Average of ages between 38 and 74:%.2f" %((self.total/self.countq6)))

   def countnumberofvalandvotes(self):
      return("count value is hot and votes are %d less than 1508:%.2f" %((self.total1/self.countq7)))



   def reset(self):#resets the value back to the beginning
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

   
##--------------------
## FileReader class
##--------------------
class FileReader():
   
   def __init__(self, filename, counter):
      self.counter = counter
      self.filename = filename

   def run(self):
      theFile = open( self.filename,'r')
      firstLine = True
         # looking at each line in the file in turn
      for line in theFile:
          if firstLine: # I do not want to read the field names
              firstLine = False   # so I skip them.
              continue
          line= line.strip()
          fields=line.split(',')

          code=fields[0]
          weight=float(fields[1])
          votes=int(fields[2])
          colour=fields[3]
          val= fields[4]
          ages= int(fields[5])
                    
          
             # then I pass a complete Rectangle to the counter object
          self.counter.add( Rectangle(code,weight,votes, colour, val, ages))
         
      theFile.close() 

##--------------------
## Demonstrator class
##   this will later be replaced by our GUI class
##--------------------
class Demonstrator():
   
   def __init__(self,filename):
      self.counter = Counter()
      self.reader = FileReader(filename, self.counter)
      self.reader.run()
      

   def displaynumberofinvalidcodes(self):
      print("Q1-",self.counter.numberofinvalidcodes())#number of codes that do not match the format given

      
   def displaypercentageofWeight(self):#print percentage of numbers between 1544.505 and 1795.023
      print ("Q2-", self.counter.percentageofweight())
##
##
   def displaypercentageofVotes(self):#percentage of votes for Q3
      print ("Q3-",self.counter.percentageofvotes())
##
##
   def displaylengthofcolours(self):
      print("Q4-",self.counter.lengthofcolours())

   def displaynumberofcoldvals(self):
      print("Q5-",self.counter.numberofcoldvals())

   def displaynumberofages(self):
      print("Q6-",self.counter.numberofages())

   def displaycountnumberofvalandvotes(self):#display number of values that are Hot and votes tht are less than 1508
      print("Q7-",self.counter.countnumberofvalandvotes())
          
   def newFile(self, filename):
      self.counter.reset() # throw away any old results
      self.reader = FileReader( filename, self.counter)
      self.reader.run()
      
#----------------------------
# now show how we use these classes
# it is increadibly simple
#----------------------------
print("\n\t class object oriented programming\n\t","+"*30)
print("\nFirst calculating with the file 3224849a.csv")
d= Demonstrator("3224849a.csv")
d.displaynumberofinvalidcodes()#q1
d.displaypercentageofWeight()#q2
d.displaypercentageofVotes()#q3
d.displaylengthofcolours()#q4
d.displaynumberofcoldvals()#q5
d.displaynumberofages()#q6
d.displaycountnumberofvalandvotes()#q7

print("\n The second file 3224849b.csv")
d.newFile("3224849b.csv")
d.displaynumberofinvalidcodes()#q1
d.displaypercentageofWeight()#q2
d.displaypercentageofVotes()#q3
d.displaylengthofcolours()#q4
d.displaynumberofcoldvals()#q5
d.displaynumberofages()#q6
d.displaycountnumberofvalandvotes()#q7
  

print("\n Finally calculating the file 3224849c.csv")
d = Demonstrator("3224849c.csv")
d.displaynumberofinvalidcodes()#q1
d.displaypercentageofWeight()#q2
d.displaypercentageofVotes()#q3
d.displaylengthofcolours()#q4
d.displaynumberofcoldvals()#q5
d.displaynumberofages()#q6
d.displaycountnumberofvalandvotes()#q7

