from par import tutte, cof
import random


for k in cof:
	if k not in tutte:
		print(k)


'''
for k in range(50):
	sol = random.choice(tutte)
	if sol not in cof:
		gg=input(sol)
		if gg=='ù':
			cof.append(sol)
print(cof,len(cof))'''