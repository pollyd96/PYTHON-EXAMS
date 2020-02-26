#EXERCISE 1

fname = open("test.txt")     #anoigma arxeiou txt gia epexergasia

from itertools import count 
  
def longest_word(lst, K): 
    cnt = count() 
    return sorted(lst, key = lambda w : (len(w), next(cnt)),  
                                        reverse = True)[:5]
   
lst = list()                  #dimiourgia listas gia kathe lexi tou arxeiou
for line in fname:
    line = line.rstrip()       
    words = line.split(' ')
    for word in words:
        if word in lst: continue
        lst = lst + words   
print('These are the five LONGEST words of this text :')
print(longest_word(lst, 5))    #emfanisi twn 5 mwgaliterwn lexewn
print "\n"                     #dimiourgia kenou stis emfaniseis

new = longest_word(lst, 5)
def reverse_word(new):          #antistrofi twn lexewn
    return word[::-1]
new =[reverse_word(new) for word in new]


def list_to_string(new):        #dimiourgoume string gia epexergasia
    string = ", "               
    return (string.join(new))
rev = list_to_string(new)
rev = rev.replace(".", "")      #epilegoume na afairesei tis teleies
rev = rev.replace(",", " ")     #kai ta kommata apo tin emfanisi
print('These are the words REVERSED:')
print rev
print "\n"                      #dimiourgia kenou stis emfaniseis

#epilegoume na emfanisei tis lexeis pou exoume antistepsei xwris fwnienta
consonants = rev
print('These are the CONSONANTS of the reversed words:')
print(consonants.translate(None,'aeiouyAEIOUY')) 
