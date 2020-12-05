f = open("/Users/garrettmartin/Downloads/advent.txt", "r")
valid = 0
passports = []
passport = ""
for line in f:
    if line != "\n":
        print(line)
        passport += " " + line
    if line == "\n":
        passports.append(passport)
        passport = ""

passports.append(passport)


for passport in passports:
    passport = passport.strip().replace('\n ',',').replace('\n',',').replace(' ',',')
    passportsplit = passport.split(',')
    keyList = {}
    for eachKey in passportsplit:
        key = eachKey.split(':')
        keyList[key[0]] = key[1]
    if 'byr' in keyList and 'iyr' in keyList and 'eyr' in keyList and 'hgt' in keyList and 'hcl' in keyList and 'ecl' in keyList and 'pid' in keyList:
        valid += 1
        print('valid')
    else:
        print('invalid')
        print(keyList)
        
print(valid)
