#example for read a text file

file = open('test.txt')

#print(file.read()) # prints whole file contents

#print(file.read(10)) # prints first 10 chars.

# str = file.readline()
#
# while str != "":
#     print(str)
#     str = file.readline()

for line in file.readlines():
    print(line)

file.close()
