import re
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
        if int(keyList['byr']) >= 1920 and int(keyList['byr']) <=2002:
            if int(keyList['iyr']) >= 2010 and int(keyList['iyr']) <=2020:
                    if int(keyList['eyr']) >= 2020 and int(keyList['eyr']) <= 2030:
                        if '#' in keyList['hcl']:
                            if len(keyList['hcl']) == 7 and re.search('[a-z0-9]', keyList['hcl']):
                                if keyList['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
                                    if len(keyList['pid']) == 9 and re.search('[0-9]',keyList['pid']):
                                        if 'cm' in keyList['hgt'] or 'in' in keyList['hgt']:
                                            if 'cm' in keyList['hgt']:
                                                hgt = keyList['hgt'].split('cm')[0] 
                                                if int(hgt) >= 150 and int(hgt) <= 193:
                                                    valid += 1
                                            if 'in' in keyList['hgt']:
                                                hgt = keyList['hgt'].split('in')[0] 
                                                if int(hgt) >= 59 and int(hgt) <= 76:
                                                    valid += 1
    else:
        print('invalid')
        print(keyList)
