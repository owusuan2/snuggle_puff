#!/usr/bin/python3
import string#This imports the method string 
from rectver1 import veriffield

#this function is for checking the number of invalid codes in file." 
 
def checkString(astring):#this is the beginning of a function
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
class Counter():#this class contains all the counters with the constuctor including the self
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
        self.countq7=0#This variablee is counting all the lines in 
        self.total1=0# variable for calculating the total of lines of vals and votes


   
   def add(self, veriffield):
##      self.count += 1  # every time I add a veriffield I add 1


## Q1-To calculate number of values in this field that match the format given

        if not checkString(veriffield.getCode()):
           self.countinvalidcode+=1
           
      #q2-Calculate percentage of numbers in weight that lie between 1544.505 and 1795.023
        self.count +=1
        if veriffield.getWeight() >= 1544.505 and veriffield.getWeight() <= 1795.023:
            self.countq2 +=1
##         
##         #q3- Calculating total votes
        #self.count+=1
        if veriffield.getVotes() >= 1125:
            self.countvotes+=1
##          #self.totalh=self.totalh + rectangle.getHeight()
##
##      #q4-Count the number of strings in the field [colour] that are morthan 3 characters long
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
        if veriffield.getVal()=='Hot' or veriffield.getVotes() < 1508:
           self.countq7 +=1
           #self.total1=self.total1 +rectangle.getVotes()


   def numberofinvalidcodes(self):#this function is for returning the number of files 
      return ("Number of codes that do not match format: %d"%(self.countinvalidcode))


   def percentageofweight(self):
      return ("Percentage of weight between 1544.505 and 19795.023: %d" % ((self.countq2/self.count)*100))

   def percentageofvotes(self):
      return ("Percentage of votes more than or equal to 1125: %d" %((self.countvotes/self.count)*100))

   def lengthofcolours(self):
      return("Length of colours that are more than 3:",(self.countcolour))

   def numberofcoldvals(self):
      return("Number of cold values in this field:",(self.countq5))

   def numberofages(self):
      return("Average of ages between 38 and 74:%.2f" %((self.total/self.countq6)))

   def countnumberofvalandvotes(self):
      return("count value is hot and votes are %d less than 1508: " %(self.countq7))



   def reset(self):#resets the value back to the beginning
       self.count  = 0#count is set back to the beginning 
       self.countinvalidcode=0#countinvalidcode is set back to the beginning
       self.countq2=0#countq2 is set back to the beginning
       self.countvotes=0#countvotes is set back to the beginning
       self.countcolour=0#countcolour is set back to the beginning
       self.countq5=0
       self.countq6=0
       self.total=0
       self.average=0
       self.countq7=0
       self.total1=0

   
##--------------------
## FileReader class
##--------------------
class FileReader():#class for filereader, in order for the program to read the contents of the file.
   
   def __init__(self, filename, counter):
      self.counter = counter
      self.filename = filename

   def run(self):
      theFile 
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

          code=fields[0]#this is the first field in the file called code which will be called into the program
          weight=float(fields[1])#this is the second field called weight, this 
          votes=int(fields[2])
          colour=fields[3]
          val= fields[4]
          ages= int(fields[5])
                    
          
             # then I pass a complete Rectangle to the counter object
          self.counter.add( veriffield(code,weight,votes, colour, val, ages))
         
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
d.displaynumberofinvalidcodes()#q1# this is how all the classes will be displayed for example
d.displaypercentageofWeight()#q2 this line displays the class for the weight questions
d.displaypercentageofVotes()#q3
d.displaylengthofcolours()#q4
d.displaynumberofcoldvals()#q5
d.displaynumberofages()#q6
d.displaycountnumberofvalandvotes()#q7

print("\n The second file 3224849b.csv")
d.newFile("3224849b.csv")#this display is for the second file (b)
d.displaynumberofinvalidcodes()#q1
d.displaypercentageofWeight()#q2
d.displaypercentageofVotes()#q3
d.displaylengthofcolours()#q4
d.displaynumberofcoldvals()#q5
d.displaynumberofages()#q6
d.displaycountnumberofvalandvotes()#q7
  

print("\n Finally calculating the file 3224849c.csv")
d = Demonstrator("3224849c.csv")#this is the third file
d.displaynumberofinvalidcodes()#q1
d.displaypercentageofWeight()#q2
d.displaypercentageofVotes()#q3
d.displaylengthofcolours()#q4
d.displaynumberofcoldvals()#q5
d.displaynumberofages()#q6
d.displaycountnumberofvalandvotes()#q7

