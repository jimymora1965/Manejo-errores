try:
    # Código que podría generar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Se ejecuta si ocurre una excepción del tipo ZeroDivisionError
    print("¡No se puede dividir por cero!")
except Exception as e:
    # Se ejecuta para cualquier otra excepción no manejada
    print(f"Se produjo una excepción: {e}")
else:
    # Se ejecuta si no hay ninguna excepción
    print("La operación se realizó con éxito.")
finally:
    # Se ejecuta siempre, haya o no haya excepción
    print("Este bloque siempre se ejecuta.")
