import string
f = open("/Users/garrettmartin/Downloads/advent.txt", "r")
totalSum = 0
groups = []
group = ""
alphabet_string = string.ascii_lowercase
alphabet_list = list(alphabet_string)
for line in f:
    if line != "\n":
        #print(line)
        group += " " + line
    if line == "\n":
        groups.append(group)
        group = ""

groups.append(group)


for group in groups:
    group = group.strip().replace('\n ',',').replace('\n',',').replace('\s',',')
    group = group.split(',')
    people = len(group)
    sum = 0
    for c in alphabet_list:
        charCount = 0
        for person in group:
            if person.count(c):
                charCount +=1
        if charCount == people:
            totalSum += 1


print(totalSum)
