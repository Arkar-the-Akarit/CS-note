'''
Glossary: A Python dictionary can be used to model an actual dictionary. 
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous 
chapters. Use these words as the keys in your glossary, and store their 
meanings as values.
• Print each word and its meaning as neatly formatted output. You might 
print the word followed by a colon and then its meaning, or print the word 
on one line and then print its meaning indented on a second line. Use the 
newline character (\n) to insert a blank line between each word-meaning 
pair in your output.
'''

gloosary = {
    'variable' : 'a thing used to store values',
    'data type' : 'the type of data we want to use',
    'string' : 'a type of data, representing arrays of characters',
    'index' : 'reprensenting the number for elements from a collection of data, starts from zero',
    'function' : 'a block of code usable anywhere within the program'
    }

print(f"Variable : {gloosary.get('variable').title()}\n")
print(f"Data Type : {gloosary.get('data type').title()}\n")
print(f"String : f{gloosary.get('string').title()}\n")
print(f"Index : f{gloosary.get('index').title()}\n")
print(f"Function : f{gloosary.get('function').title()}\n")
