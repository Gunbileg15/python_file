# Exercise 1
def write_shopping_list(items, filename):
    file = open(filename,"w")
    c=1
    for i in items:
        file.write(f"{c}. {i}\n")
        c=c+1
    file.close()

items = ["Bread", "Milk", "Eggs"]
filename = "shopping.txt"
write_shopping_list(items,filename)

# Exercise 2
def read_names(filename):
    file = open(filename,"r")
    lst=[]
    lines=file.readlines()
    for line in lines:
        if line.strip()!="":
            lst.append(line.strip())
    file.close()
    return lst

# Exercise 3
def append_entry(filename, text):
    file = open(filename,"a")
    file.write(text + "\n")
    file.close()
    file = open(filename,"r")
    lst = file.readlines()
    file.close()
    return len(lst)

# Exercise 4
def search_file(filename, word):
    file=open(filename,"r")
    lines = file.readlines()
    lst=[]
    c=1
    for line in lines:
        if word.lower() in line.strip().lower():
           lst.append(c)
        c=c+1
    file.close()
    return lst

# Exercise 5
def number_the_lines(source, destination):
    s = open(source, 'r')
    lines = s.readlines()
    s.close()

    d = open(destination, 'w')
    c = 0

    for line in lines:
        c += 1
        d.write(f"{c}: {line}")

    d.close()
    return c
