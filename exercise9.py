#EXERCISE 9

num = int(input("Enter a Number: ")) #gia prosthiki arithmou
print "\n"                           #dimiourgia kenou gia tin emfanisi

result = 0
y = (num * 3 )+ 1                    #arxiki praxi pou theloume
z = y
print('Result after Multiplication and Addition of:',num,'is:',y)

while z > 0:                         #while loop gia athrisma psifiwn
    rem = z % 10
    result = result + rem
    z= int(z/10)
print('Sum of all Digits of', y , 'is:', result )


length=len(str(result)) 
# while loop gia elegxo monopsifiou kai epanalipsi diadikasias 
while length > 1:
    z=(result * 3) +1
    y=result
    result=0
    while z > 0:
        rem = z % 10
        result = result + rem
        z= int(z/10)
    length=len(str(result))
    print('Result of the repeated Operation of', y , 'is:', result )
#exw epilexei na emfanizei to apotelesma se  
#kathe stadio twn praxewn gia elegxo




