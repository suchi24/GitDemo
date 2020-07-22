#example for try-except block

try:
    with open('test.txt','r') as reader:
        reader.read()
# except:
#     print('file not exists. it failed')

except Exception as e:
    print(e)
finally:
    print("this block is for clearing all resources we created during test")