values = [1, 3, "suchi", 5, 7]

print(values[-1])
print(values[1:3])

values.insert(3, "thoppay")

print(values)
print("Length = ", len(values))

values.append("end") # add at the end

values[2] = "suchithra"  # update
print(values)

del values[0]

print(values)

a = {1 : "first name", 2 : "last name", "c" : "hello world"}

print(a[2])
print(a["c"])

dict = {}
dict["firstname"] = "suchithra"
dict["lastname"] = "thoppay"
dict["gender"] = "female"
print(dict)
