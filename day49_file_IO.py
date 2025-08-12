# READING A FILE
t = open("day49_myfile.txt", "r")
text = t.read()
print(text)
t.close()

# WRITING A FILE
t = open("day49_myfile.txt", "a")
t.write(" Hlw Muhtaram! ")
