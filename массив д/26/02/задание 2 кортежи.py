punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str = input('введите строку: ')
no_punct = ""
for char in str:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)