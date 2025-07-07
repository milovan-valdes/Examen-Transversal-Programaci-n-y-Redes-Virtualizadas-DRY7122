import requests

API_KEY = "ef6b0d1e-c166-4705-adf4-0221eb4eb934"            # Reemplaza con tu API Key de GraphHopper
GRAPHOPPER_URL = "https://graphhopper.com/api/1/route"

def solicitar_ciudad(mensaje):
    while True:
        ciudad = input(mensaje).strip()
        if ciudad.lower() == "s":
            return None
        if ciudad:
            return ciudad
        print("Entrada inválida. Intente de nuevo.")

def solicitar_medio_transporte():
    medios = {
        "1": "car",
        "2": "bike",
        "3": "foot"
    }
    print("\nSeleccione el medio de transporte:")
    print("1. Auto")
    print("2. Bicicleta")
    print("3. A pie")
    
    while True:
        opcion = input("Opción: ").strip()
        if opcion.lower() == "s":
            return None
        if opcion in medios:
            return medios[opcion]
        print("Opción inválida. Intente de nuevo.")

def obtener_coordenadas(ciudad):
    url = f"https://graphhopper.com/api/1/geocode?q={ciudad}&locale=es&key={API_KEY}"
    resp = requests.get(url)
    data = resp.json()
    if data.get("hits"):
        punto = data["hits"][0]["point"]
        return punto["lat"], punto["lng"]
    return None

def calcular_ruta(origen, destino, vehiculo):
    lat_from, lng_from = obtener_coordenadas(origen)
    lat_to, lng_to = obtener_coordenadas(destino)

    params = {
        "point": [f"{lat_from},{lng_from}", f"{lat_to},{lng_to}"],
        "vehicle": vehiculo,
        "locale": "es",
        "instructions": "true",
        "calc_points": "true",
        "key": API_KEY
    }

    response = requests.get(GRAPHOPPER_URL, params=params)
    if response.status_code != 200:
        print("Error en la solicitud:", response.text)
        return

    data = response.json()
    path = data['paths'][0]

    distancia_km = path['distance'] / 1000
    distancia_millas = distancia_km * 0.621371
    duracion_segundos = path['time'] / 1000
    minutos = int(duracion_segundos // 60)
    segundos = int(duracion_segundos % 60)

    print("\n🧭 Resultado del viaje:")
    print(f"Distancia: {distancia_km:.2f} km")
    print(f"Distancia: {distancia_millas:.2f} millas")
    print(f"Duración estimada: {minutos} minutos y {segundos} segundos")


    print("\n📍 Instrucciones del viaje:")
    for i, instruccion in enumerate(path["instructions"]):
        print(f"{i+1}. {instruccion['text']} ({instruccion['distance']:.0f} m)")

def main():
    print("Bienvenido al calculador de rutas entre Chile y Argentina.\n(Escriba 's' en cualquier momento para salir)")

    while True:
        origen = solicitar_ciudad("Ingrese la ciudad de origen (Chile): ")
        if origen is None:
            break

        destino = solicitar_ciudad("Ingrese la ciudad de destino (Argentina): ")
        if destino is None:
            break

        vehiculo = solicitar_medio_transporte()
        if vehiculo is None:
            break

        calcular_ruta(origen, destino, vehiculo)

if __name__ == "__main__":
    main()
