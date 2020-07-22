# while loop example
# i = 4
# while i > 1:
#     if i != 3:
#         print(i)
#     i = i -1
# print('while loop is done')

j = 10
while j > 1:
    if j == 9 :
        j = j - 1
        continue
    if j == 3:
        break
    print(j)
    j = j - 1
print('while loop is done')