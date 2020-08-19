import random

random.seed()
def nameGenerator():
    lines = open("C:\\Users\\Shubh Singh Garg\\Desktop\\New folder\\Python Stuff\\Petition signer\\first_names.txt").readlines()

    rand_num = random.randint(0, len(lines))
    line = lines[rand_num]

    words = line.split()
    firstName = random.choice(words)

    lines = open("C:\\Users\\Shubh Singh Garg\\Desktop\\New folder\\Python Stuff\\Petition signer\\Last_names.txt").readlines()

    rand_num = random.randint(0, len(lines))
    line = lines[rand_num]

    words = line.split()
    lastName = words[0]

    return(firstName + " " + lastName)


for i in range(20):
    print(nameGenerator())   