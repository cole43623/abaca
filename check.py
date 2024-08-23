from par import tutte, cof
import random


for k in range(20):
	p=input().upper()
	if len(p)>2 and p not in cof and p in tutte:
		print('"'+p+'"\n')
		cof.append(p)

cof.sort()

with open("nuova.txt", "w") as file:
    file.write("cof = "+str(cof))


'''
for k in range(50):
	sol = random.choice(tutte)
	if sol not in cof:
		gg=input(sol)
		if gg=='ù':
			cof.append(sol)
print(cof,len(cof))'''