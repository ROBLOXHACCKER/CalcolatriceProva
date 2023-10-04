import time
import os
from colorama import Fore, Style

operazioni = ["somma", "sottrazione", "moltiplicazione", "divisione"]
num1 = 0
num2 = 0
operazione_num = 0

while True:
    for i, operazione in enumerate(operazioni):
        print(f"{i} - {operazione}")

    try:
        operazione_num = int(input(">"))
        if 0 <= operazione_num < len(operazioni):
            break
        else:
            print("[!] Operazione non valida")
            time.sleep(2)
            os.system("cls" if os.name == "nt" else "clear")
    except ValueError:
        print(Fore.RED + "[!] Input non valido. Inserisci un numero intero." + Style.RESET_ALL)

try:
    num1 = int(input("Primo numero: "))
    num2 = int(input("Secondo numero: "))
except ValueError:
    print(Fore.RED + "[!] Input non valido. Inserisci un numero intero." + Style.RESET_ALL)

print(f"Hai scelto l'operazione: {operazioni[operazione_num]}")
print(f"Num1: {num1}")
print(f"Num2: {num2}")

# Ora puoi eseguire l'operazione selezionata e stampare il risultato.
if operazione_num == 0:
    result = num1 + num2
elif operazione_num == 1:
    result = num1 - num2
elif operazione_num == 2:
    result = num1 * num2
elif operazione_num == 3:
    if num2 == 0:
        print(Fore.RED + "[!] Impossibile dividere per zero." + Style.RESET_ALL)
        result = None
    else:
        result = num1 / num2

if result is not None:
    print(f"Risultato: {result}")