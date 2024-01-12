import os

def suma():
    try:
        n1 = int(input("Ingresa el primer numero: "))
        n2 = int(input("Ingresa el segundo numero: "))
        result = n1 + n2
        print(f"La suma es: {result}")
        print("Gracias por sumar")
    except Exception as e:
        print("Algo no ha salido bien:", e)
    else:
        print("Hiciste todo bien")

# Loop to allow multiple inputs
while True:
    suma()
    
    another_sum = input("¿Quieres hacer otra suma? (s/n): ").lower()
    
    if another_sum != 's':
        break  # Exit the loop if the user doesn't want to continue
    else:
        # Clear console screen
        os.system('cls' if os.name == 'nt' else 'clear')

print("Eso fue todo")
