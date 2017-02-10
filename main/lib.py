consonantsCyrillic='бвгджзйклмнпрстфхцчшщъь'
vowelsCyrillic='аеёиоуыэюя'
# mess - text on russian language
# ind - a number ,must be 1/ind = 0.05 or 0.1 or 0.25 or 0.5 or 1 itc.
def encode(mess,ind):
    encodedStr=''
    i=1
    for symbol in mess:
        if(consonantsCyrillic.find(symbol)!=-1):
            encodedStr +=str(i/ind)+':'+str((consonantsCyrillic.find(symbol)+1)/ind)+';'
        i+=1
    i = 1
    encodedStr += '@'
    for symbol in mess:
        if (vowelsCyrillic.find(symbol) != -1):
            encodedStr += str(i / ind) + ':' + str((vowelsCyrillic.find(symbol)+1)/ ind) + ';'
        i += 1
    return encodedStr


def decode(mess,ind):
    consonants=[]
    vowels=[]
    decodeStr=''
    temp=''
    flag=False
    for symbol in mess:
        if(symbol=='@'):
            flag=True
            continue
        if(symbol==';' or symbol==':'):
            if(flag):
                vowels.append(float(temp))
                temp=''
            else:
                consonants.append(float(temp))
                temp = ''
        else:
            temp+=symbol
    for numbOfElement in range(len(consonants)):
        consonants[numbOfElement]=int(consonants[numbOfElement]*ind)
        if (numbOfElement % 2 == 1):
            consonants[numbOfElement]=consonantsCyrillic[consonants[numbOfElement]-1]
    for numbOfElement in range(len(vowels)):
        vowels[numbOfElement]=int(vowels[numbOfElement]*ind)
        if (numbOfElement % 2 == 1):
            vowels[numbOfElement]=vowelsCyrillic[vowels[numbOfElement]-1]
    sentence=consonants+vowels
    marks=0
    for numbOfElement in range(len(sentence)):
        if (numbOfElement % 2 == 0):
            if(sentence[numbOfElement]>marks):
                marks=sentence[numbOfElement]
    for temp in range(marks+1):
        for numbOfElement in range(len(sentence)):
            if(numbOfElement%2==0):
                if(sentence[numbOfElement]==(temp+1)):
                    decodeStr+=sentence[numbOfElement+1]
                    flag = True
                    break
                else:
                    flag=False
        if(flag==False):
            decodeStr+=' '
    return(decodeStr)

