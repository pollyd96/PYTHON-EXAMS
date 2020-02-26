#EXERCISE 2

fname = open("test.txt")                    #anoigma arxeiou txt gia epexergasia
lst = list()                                #dimiourgia listas gia kathe lexi tou arxeiou
for line in fname:
    line = line.rstrip()       
    words = line.split(' ')
    for word in words:
        if word in lst: continue
        lst = lst + words

def list_to_string(lst):                    #dimiourgoume string gia na afairesoyme ta fonienta
    string = ", "               
    return (string.join(lst))
lst2 =list_to_string(lst)
print lst2                                  #emfanizoume to keimeno se string gia na mporoume
                                            
lst2=lst2.replace('.', '')                  #afairoume tis teleies 
lst2 = lst2.translate(None,'aeiouyAEIOUY')  #apaloifoume na fonienta
def back_to_list(x):                        #dimiourgoume pali lista gia sigrisi sti sinexeia
        y = list(x.split(', '))
        return y
lst2 = back_to_list(lst2)

lstcount=[]                                 #metrame gia kathe lexi to athrisma twn f,c,k,r
count=0
for i in range(0, len(lst2)):
    temp = lst2[i]
    for j in range(0, len(temp)):
        if temp[j]== 'f' or temp[j]=='c' or temp[j]=='k' or temp[j]=='r': 
            count=count+1
    lstcount.append(count)
    count=0

lstlength=map(len,lst2)                     #sigrinoume ta simfwna metaxi tous se sxesi me f,c,k,r
for i in range(0, len(lst2)):               #epilegoume na emfanizei to apotelesma se sxesi me tin arxiki lexi
    if lstcount[i] > lstlength[i]/2:        #sxoliazoume ws GOOD h BAD tin kathe lexi 
        print('The word ', lst[i], 'is a BAD word')
    else:
        print('The word ', lst[i], 'is a GOOD word')
