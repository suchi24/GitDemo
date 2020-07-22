#example for strings
str = "suchithra.com"
str1 = " learning"
str3 = "suchi"

print(str[1])

print(str[0:5])

print(str + str1)

print(str3 in str)

var = str.split(".")
print(var)

print(var[0])

str4 = "   great   "
print(str4.strip())
print(str4.lstrip()+ "hhh")
print("kkk"+str4.rstrip())