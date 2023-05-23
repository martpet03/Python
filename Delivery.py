#boja tapeti rakavici chetki
import math
boja = 21.50
boja_broi = int(input())
tapet = 5.20
tapeti_broi = int(input())
rakavici = math.ceil((35 / 100) * tapeti_broi)
chetki = math.floor((48 / 100) * boja_broi)
rakavici_broi = float(input())
chetki_broi = float(input())
boja_cena = boja * boja_broi
tapet_cena = tapet * tapeti_broi
rakavici_cena = rakavici * rakavici_broi
chetki_cena = chetki * chetki_broi
sum = boja_cena + tapet_cena + rakavici_cena + chetki_cena
dostavka = sum / 15
print(f"The delivery will cost {dostavka:.2f}")
