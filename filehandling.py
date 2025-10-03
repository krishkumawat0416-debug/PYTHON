## ----> FILE HANDLING <---- ##

# ---> OPENING FILE <---- #

# f = open("sample.txt", "r")
# f.read()
# f.close()

## ---> READING THE FILE <--- ##
# file = open('sample.txt', 'r')
# print(file.read())
# file.close()

## ---> WRITING SOMETHING INTO A FILE <---- ##
# file = open('sample .txt', 'w')
# file.write('this is the line from the writing file(write mode)')
# file.close()

##  ---> if any text is already present into the fioelthen how can we add the next line <-- ##
## ---> for this we use append mode('a')
# file = open('sample.txt', 'a')
# file.write("\nthis is the text append mode!")
# file.write("\nthis is the new line")
# file.close()
## ---> close not use return last line lenght in int value <-- ##

## ---> if any file doesn't exicst <--- ##
# file = open('hello.txt', 'w')
# file.write('This is the new file')
# file.close()

## ---> read the same file <-- ##
# file = open('hello.txt', 'r')
# print(file.read())
# file.close()

## ---> file read write <--- ##
# sentences = ["\nthis is the first line from the list", "\nThis is the second line from the list", "\nThis is third line from the list"]
# file = open('hello.txt', 'w')
# for sent in sentences:
#     file.write(sent)
# file.close()    

## (1). read, readline, readlines <--- ##

# file = open('hello.txt', 'r')  
# file.readlines()
## ---> read all line in list 
# file.readline()
## ---> read line to line 1 to 1
# print(type(file.read()))

## ---> indexing in lines <--- ##

# file = open('hello.txt', 'r')
# text = file.readlines()
# print(text[2])
# file.close

## ---> with is used to close the opened file after I/O opration
## ---> It automatically close the file <--- ##

# with open('sample.txt', 'r') as file:
#     print(file.read())
