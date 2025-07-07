# Solicita al usuario el número de VLAN
vlan_input = input("Ingresa el número de VLAN: ")

# Verifica si el valor ingresado es un número entero
try:
    vlan = int(vlan_input)

    # Validación del rango de VLAN
    if 1 <= vlan <= 1005:
        print(f"La VLAN {vlan} pertenece al rango NORMAL.")
    elif 1006 <= vlan <= 4094:
        print(f"La VLAN {vlan} pertenece al rango EXTENDIDO.")
    elif vlan == 0 or vlan == 4095:
        print(f"La VLAN {vlan} está reservada.")
    else:
        print("Número de VLAN fuera de rango válido (1–4094).")
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
    
# rango normal (1–1005)
# rango extendido (1006–4094)