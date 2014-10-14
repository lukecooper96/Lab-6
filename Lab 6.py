#total = 0

#print "How many numbers do you wish to add?"
#userInput = int(raw_input())
#for x in range(userInput):
    #print "enter number"
    #userINput = int(raw_input())
    #total = total + userInput
#print total

#total = []
#print "how many numbers do you wish to add?"
#userINPut = int(raw_input())
#for y in range(userINPut):
    #print "enter number"
    #userINPUt = int(raw_input())
    #total.append(userINPUt)
#print sum(total)

#print "What number do you want to take the factorial of"
#num = int(raw_input())
#factorial = 1
#for z in range(1,num + 1):
    #factorial = factorial*z
#print "The factorial for" + str(num) + "is" + str(factorial) 

factors = []
print "what numbers factors do you want to know?"
number = int(raw_input())
group = 1
while (group < number):
    if number%group == 0:
        factors.append(group)     
group = group + 1
print factors

