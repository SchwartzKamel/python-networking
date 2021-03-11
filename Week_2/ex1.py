# assigning variables to open, read, and close the file
f = open("show_version.txt")
show_ver = f.read()

print(show_ver)
print(type(show_ver))
f.close()

# using with open to open in read mode
with open("show_version.txt") as f:
    show_ver = f.readlines()

print(show_ver)
print(type(show_ver))
