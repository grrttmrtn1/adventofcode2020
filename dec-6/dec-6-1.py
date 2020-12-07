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
    group = group.strip().replace('\n ','').replace('\n','')
    sum = 0
    for c in alphabet_list:
        if group.count(c):
            sum += 1
    print(group)
    print(sum)
    totalSum += sum
        

print(totalSum)
