#Crappy Password Generator

fileName = 'crappy_passwords.txt'
f = open(fileName, 'a+')

base = []

print('Enter base for password; done when finished.')
while True:
    pswd = input()
    if pswd == 'done':
        break
    base.append(pswd)

months = ('january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'december')
seasons = ('spring', 'summer', 'fall', 'winter')
years = ('2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021')
leet = (('e','3'), ('l','1'), ('s','$'))

#permutations
base_perm = []
base_leet = []
base_seasons = []
base_years = []
base_all_base = []
base_master = []
#one upper
for x in range(0, len(base)):
	for y in range(0, len(base[x])):
		up = str(base[x][y]).upper()
		perm = base[x][:y]+up+base[x][y+1:]
		base_perm.append(perm)
		# print(base_perm)
        
base_all_base = base_perm
base_master = base_all_base

#one leet char		  
for x in range(0, len(base)):
	for y in range(0, len(base[x])):
		for z in range(0, len(leet)):
			if leet[z][0] == base[x][y]:
				leetMod = base[x][:y]+str(leet[z][1])+base[x][y+1:]
				# print(str(leetMod))
				base_leet.append(leetMod)
base_all_base+=base_leet
base_master+=base_all_base

#with year
for x in range(0, len(base_all_base)):
    for y in range(0, len(years)):
        base_years.append(str(base_all_base[x])+str(years[y]))

base_master+=base_years

# single digit end
base_sd_end = []
for x in range(0, len(base_master)):
    for y in range(0, 9):
        base_sd_end.append(str(base_master[x]+str(y)))

base_master+=base_sd_end

#bang
base_bang = []
for x in range(0, len(base_master)):
    base_bang.append(str(base_master[x] + '!'))
    
base_master+=base_bang

print(str(base_master))
print(str(len(base_master))+' crappy passwords.')

for password in base_master:
    f.write(password+'\n')
