# regular expression
# introduction to regex
# simple characters matches
# character classes
# special characters
#quantifiers
# substituting
# compiling regular expression
# split function

import re
# 2- SIMPLE CHARACTERS MATCHES
text = "cat bat mat rat cat"
pattern = "cat " #for extracting 
# re.findall(pattern, text)
output = re.findall(pattern, text)
print(output)

text_1 = "cat bat mat cat rat"
output_1 = re.findall(pattern, text_1)
print(output_1)

my_text= " the dog bark loudly"
pattern= "dog"
print(pattern)


# 3- CHARACTER CLASSES
text= 'a583762635bc 123'
pattern= r'\d'# formular to extract numbers from text
print(re.findall(pattern,text))

text= 'abc def ghi jkl'
# pattern=r'[def]'#to be in list 
pattern= 'def'
print(re.findall(pattern,text))

text= 'Hello World! abc DEF 123'
# pattern=r'[a-z]'# for extracting lowercase letter
pattern=r'[A-Z]'# for extracting uppercase letter
# pattern=r'[a-zA-Z]'# for extracting both upper and lower case
print(re.findall(pattern, text))

text= 'abc def ghi jkl'
pattern=r"[^def]"# for extracting everything except def
print(re.findall(pattern,text))

# \t means a large space
text= "abc \t def \t"
pattern=r"[^def]"
print(re.findall(pattern,text))

text='Hello World 1234 ^&**%$'
pattern=r'[a-zA-Z0-9]'# for extracting for num,lower and upoper case
print(re.findall(pattern,text))

text= 'Hello World 1234 ^&**%$'
pattern=r'\s'# to extract spaces
print(re.findall(pattern, text))

text='Hello World 1234 ^&**%$'
pattern=r'[^a-zA-Z0-9]'# try not to extracting for num,lower and upoper case
print(re.findall(pattern,text))

text='Hello World 1234 ^&**%$'
pattern=r'[^a-zA-Z0-9\s]'# try not to extract everything except symbols
print(re.findall(pattern,text))

text='Hello World 1234 ^&**%$'
pattern=r'[^A-Z0-9\s]'# to extract symbols and lowercase
print(re.findall(pattern,text))


#4- SPECIAL CHARACTER
text ='hello world'
pattern=r'h.llo'# to print wold start from h and end with llo
print(re.findall(pattern,text))

text ='hello world hallo heeello'
pattern=r'h.*llo'# to print everything 
print(re.findall(pattern,text))

text ='dello hello world fallo heeello'
pattern=r'h.*llo'
print(re.findall(pattern,text))

text= 'dello world falld heeello'
pattern= '.*ld'
print(re.findall(pattern,text)) 


#5-QUANTIFIERS
text= 'a aa aaa aaaa aaaaa '
pattern=r'a*'# extract for matches of 0 or more
print(re.findall(pattern,text)) 

text= 'a aa aaa aaaa aaaaa '
pattern=r'a+'# extract for matches of 1 or more
print(re.findall(pattern,text)) 

text= 'a aa aaa aaaa aaaaa '
pattern=r'a{2}'# pulling out for 2 occurence
print(re.findall(pattern,text)) 

text= 'a aa aaa aaaa aaaaa '
pattern=r'a{2,}'# extracting  for 2 occurence
print(re.findall(pattern,text)) 

text= 'a aa aaa aaaa aaaaa '
pattern=r'a{3}'# extract for 3 occurence
print(re.findall(pattern,text)) 

text= 'a aa aaa aaaa aaaaa '
pattern=r'a{4}'# extract for 4 occurence
print(re.findall(pattern,text)) 

text= 'a aa aaa aaaa aaaaa '
pattern=r'a{3,}'# extract for 3 occurence
print(re.findall(pattern,text)) 

text= 'a aa aaa aaaa aaaaa '
pattern=r'a{3}'# pulling out for 3 occurence
print(re.findall(pattern,text)) 

text= 'a aa aaa aaaa aaaaa '
pattern=r'a{2,4}'# extract for 2 and 4occurence
print(re.findall(pattern,text)) 


# 6- SUBSTITUTING
text= 'daniels and marvelous are friends'
pattern='friends'# word we are trying to substitute
output=re.sub(pattern,'opps',text)
print(output)

# 7- COMPILING REGULAR EXPRESSION

text= 'There are 10 apples and 20 oranges'
pattern= r'[\d]+'# TO EXTRACT NUMBERS 
print(re.findall(pattern,text))

pattern=re.compile(r'\d+') # STANDARD WAY TO EXTARCT NUM
deniel_text= 'There are 10 apples,30 mangos and 20 oranges'
output=pattern.findall(deniel_text)
print(output)

text= 'There are 10 apples and 20 oranges'
pattern= '[a-zA-Z]+' # TO EXTRACT WORDS
print(re.findall(pattern,text))

text= 'There are 10 apples and 20 oranges'
pattern= r'[\w]+' # to extract words/letters  and number or  #\w ==A-Za-z0-9
print(re.findall(pattern,text))


# 8- SPLIT FUNCTION

text = 'split this text for me right away'
pattern=r'\s+'#split with respect to white spaces found
output=(re.split(pattern, text))
print(output)

# print(text.split())












