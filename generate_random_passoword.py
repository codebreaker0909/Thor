###Generate 100 Random Passwords with a prime number and export it to an excel file####
###Author: Codebreaker999####
import random
import string
def prime(num):
    flag = 0
    for i in range(2,num):
        if num%i == 0:
            flag = 1
            break
    if flag == 0:
        return num
    else:
        return False

def generate():
    while True:
        num = random.randint(1000,100000)
        prime(num)
        if prime(num) == False:
            continue
        else:
            return num
            break

def password():
    letters =  string.letters
    code = []
    for i in range(5):
        code.append(random.choice(letters))
    generate()
    digit = str(generate())
    #print code
    #code.append(digit)
    pass_code = []
    #print code
    #print len(code)
    for n in range(2):
        pass_code.append(code[random.randint(0,len(code)-1)])
    pass_code.append(digit)
    for n in range(2):
        pass_code.append(code[random.randint(0,len(code)-1)])
    return "".join(pass_code)

#print prime(89)
file = open("List of Passowrds.xls","w")
for i in range(100):
    num = i+1
    file.write("Your password number "+str(num)+" is "+ password()+"\n")

file.close()




