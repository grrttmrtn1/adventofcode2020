import re
f = open("/Users/garrettmartin/Downloads/advent.txt", "r")
lines = f.read().split('\n')
bags = []

def getParsedBag(line):
    return line.split('contain')[0].strip().replace('bags','').replace('bag','').strip()

def checkBags(bag,line):
    if re.search(bag, line):
        return True

def checkGold(parse):
    if parse != 'shiny gold':
        return True

def newBag(parse):
    if parse not in bags:
        return True

for line in lines:
    if checkBags('shiny gold', line):
        parse = getParsedBag(line)
        if checkGold(parse):
            bags.append(parse)

for bag in bags:
    for line in lines:
        if checkBags(bag, line):
            parse = getParsedBag(line)
            if checkGold(parse) and newBag(parse):
                bags.append(parse)
