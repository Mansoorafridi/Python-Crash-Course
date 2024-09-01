# Reading the entire content of the file
with open("file.txt", "r") as f:           
    data = f.read()                    
    print(data)


# Writing to a file
with open("myfile.txt", "w") as f:         
    f.write("He is so smart.")         


# Reading a single line from a file
with open("multiline.txt", "r") as f:
    line = f.readline()                 # f.readline() reads a single line from a file.
    print(line)


# Reading all lines from a file and returning a list
with open("multiline.txt", "r") as f:
    lines = f.readlines()               # f.readlines() reads all lines from a file and returns a list.
    print(lines)


# Reading lines one by one in a loop until the end of the file
with open("multiline.txt", "r") as f:
    while line != "":
        print(line, end='')  # `end=''` avoids adding extra newline characters
        line = f.readline()
