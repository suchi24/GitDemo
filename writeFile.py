# read a file
# reverse the contents and write it into file

with open('test.txt','r') as reader:
    content = reader.readlines()
    reversed(content)
    with open('test1.txt','w') as writer:

        for line in reversed(content):
            writer.write(line)

reader.close()
writer.close()

