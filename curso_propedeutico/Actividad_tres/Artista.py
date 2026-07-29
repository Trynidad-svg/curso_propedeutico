consulta = input("Ingresa nombre de artista, serie o pelicula: ").lower()
match consulta:
    case "cibernetico":
        info = "Luchador mexicano reconocido por ser maniaco."
    case "sucecion m":
        info = "Banda de regional mexicano."
    case "Hachita Ludueña": 
        info = "Ex futbolista profeesional del futbol mexicano."
    case "Norbit":
        info = "Pelicula estadounidense de comedia."
    case "Stranogo":
        info = "Productor independiente de la escena del hiphop"
    case "Ludovico Peluche":
        info = "Personaje principal de serie mexicana de comedia."
    case _:
        info = "ERROR, no existe informacion sobre el artista, pelicula o serie que ingresaste. Intenta con otro nombre."

print(f"Informacion: {info}")