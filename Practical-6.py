fh = open('Practical-6.txt','w')
num=6
i=1
fact=1

while i<=num:
    fact*=i
    i+=1
fh.write('Factorial is: ' + str(fact))
fh.close()
