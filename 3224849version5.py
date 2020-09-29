print('\n\t\tStructured programming functions part 2\n\t')
#!C:/Users/owusuan2/Downloads/functionsfilereaderversion1
#Filename: functionsfilereaderversion1.py
#Author  : Natasha Owusu-Amankrah
#Date    : 2014.03.11
#Version : 0.0- First version
#purpose : This file opens a simple data file in the format
#        : code, weight, votes, colour, val, ages <string,float,int, string,string,int>
#        : this version shows the use of functions.
#        : This program answers the following questions:
#        : - How many values in the 'code' field do not match the format 99X9?(XX)9 ?
#        : - What percentage of the numbers in [kg] lie between (1544.505) and (1795.023) inclusive 
#        : - What percentage of the numbers in [votes] are greater than or equal to (1125)
#        : - Count the number of strings in the field [colour] that are more than 3 characters long
#        : - Count the number of (Cold's) in the field [val]
#        : - What is the average value of the numbers in the field [age] in the range (38) and (74) inclusive
#        : - count the lines where val's have the value (Hot) *or* votes is less than 1508

#f= open('3224849a.csv','r')

def getFile():
    filename= input('Filename: ') # user must input the name of the file
    afile=open(filename, 'r') #
    
    return afile

f= getFile()

#counters set up
count=0 # This counter is for counting each line in the file 
countinvalidcode=0# This counter for for counting the amount of invalid codes in the file for question
countq2=0# this counter is for adding the total number of votes that are more than or greater than 1125 together and working out the percentage.
per4q2=0#the percentage of the field votes 
countvotes=0# this count is for counting the number of votes
countcolour=0#counts the number of colours in the field called colour   
countq5=0#counts the temperature in the field Val, according to the question given.
countq6=0#count the average of values in the field age.
total=0#call the total count if the value is inclusive from the line read from
average=0# this divides countq6 from total to give the average number of values.
countq7=0#counts the lines in the val field and the votes fields.
total1=0#calculates the integers in value hot or if available the votes.

for line in f:# this looks at each line in the file called f
    line= line.strip()#this takes only one line into the program at a time
    fields=line.split(',')#this splits the fields into columns in the program.
    code=fields[0]#sends the code from this field into the program
    weight=float(fields[1])# using the float method it converts the string in this field into float.
    votes=int(fields[2])#using the int it converts the votes field from string into integers, for it to be used as whole numbers.
    colour=fields[3]#this field calls the field 'colour' into the program.
    val= fields[4]#this calls the field val from the file 3224849a.csv etc.
    ages= int(fields[5])#this field using int calls the ages into the program in whole numbers.
    

#q1
    import string#This imports the method string 
    def checkString(astring):#this is the beginning of a function
        if len(astring) !=10:
            return False
        if not astring[0] in string.digits:#this checks if the digits of this line is correct
            return False
        if not astring[1] in string.digits:
            return False
        if not astring[2] in string.ascii_uppercase:
            return False
        if not astring[3] in string.digits:#this returns false if the character is strong 
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


    if not checkString(code):#this function is checking for number of invalid codes 
        countinvalidcode +=1# if the countinvalidcode is invalid then 
            
#q2
    count +=1
    if weight >= 1544.505 and weight <= 1795.023:#
        countq2 +=1

##q3
    #count+=1
    if votes >= 1125: #this counts the value if the value is more than 1125
        countvotes+=1
        

#q4
        
    if len(colour) >3:
        countcolour +=1
        
#q5
    #count+=1
    if  val == 'Cold':# everytime the count finds the value cold it should add one to the counting, so 
        countq5 +=1

##q6

    if ages>= 38 and ages<= 74:# This is counting all the ages between the 38 and 74, then average///zero/zero is invalid operation
        total += ages
        countq6+=1
       
## q7 count the lines where val's have the value [hot] or votes is less than 1508 
    #count+=1
    if val == 'Hot' or votes <1508:# this prints the value if the temperature is hot and under 1508
        countq7+=1 

f.close()
print('Q1.number of codes that doesnt match: ' , countinvalidcode)#this prints the answer to number of invalid codes.
per4q2=(countq2/count)*100# calculates the percentage of weight 
print('Q2.Percentage of numbers in KG:%.2f'% per4q2)# prints the percentage of weight
per_votes=(countvotes/count)*100# this calculates the percentage of votes
print('Q3.percentage of numbers in votes equal to 1125', per_votes)#prints the percentage of votes 
print ('Q4.colour of length is 3:',countcolour)# this prints the length of colour if length is 3
print ('Q5.There are %d Cold' % countq5)# this prints the amount of 'cold' values available
average = total/countq6# this calculate the average of ages in the field 
print('Q6.average of ages:%.2f'% (average))#This prints the average of ages
print('Q7. count value is hot and votes are %d less than 1508'%(countq7))#this counts the value of the 


    
    
