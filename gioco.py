from par import tutte, cof
import random

parola = ""
tent = 0

#sol = random.choice(tutte[1:-1])
sol = random.choice(cof)

a = tutte[0]
b = tutte[-1]

while 1:
	print("\n\n\n\n",a,"\n",b)
	tent += 1
	parola = input("Inserisci parola: ").upper()
	while (parola not in tutte or parola<a or parola>b) and parola!='999':
		parola = input("Errore parola non esistente. Inserisci parola: ").upper()
	if parola == "999":
		print("la parola era:",sol,"\nhai usato tentativi:", tent)
		exit()
	if parola == sol:
		break
	if parola > sol:
		b = parola
	else:
		a = parola

print("esatto, numero tentativi:", tent);