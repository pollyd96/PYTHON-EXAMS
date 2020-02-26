#EXERCISE 4

message = raw_input("Enter Your String: ")      #entoli gia eisagwgi string

print "Your String in ASCII is:"                #emfanisi minimatos
for ch in message:                              #metatropi se ASCII CODE
   print ord(ch),
   print "\n"                                   #dimiourgia kenou stis emfaniseis
   
  
num = ord(ch)                                   #elegxos gia to an o arithmos 
                                                #einai prwtos h oxi kai
if num > 1:                                     #emfanisei tou analogou minimatos
   for i in range(2, num//2): 
           print(num, "is not a prime number") 
           break
   else: 
           print(num, "is a prime number") 
     
else: 
   print(num, "is not a prime number") 
