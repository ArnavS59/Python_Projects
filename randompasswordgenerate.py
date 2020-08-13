import random

#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)


uppercaseLetter2=chr(random.randint(65,90)) 
uppercaseLetter1=chr(random.randint(65,90)) 
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
punctuationsign1=chr(random.randint(33,152))
punctuationsign2=chr(random.randint(33,152))

password = uppercaseLetter1 + uppercaseLetter2  + lowercaseLetter1+lowercaseLetter2+digit1+digit2+punctuationsign1+punctuationsign2
#shuffling
password = shuffle(password)

print(password)