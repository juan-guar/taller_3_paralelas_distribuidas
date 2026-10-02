import threading
from pathlib import Path

import requests

CARPETA = Path("descargar_archivos")
CARPETA.mkdir(exist_ok=True)

# Lista de links con archivos a descargar (url, tiempo para que no se
# sobrescriban)

urls = [
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 1),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 2),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 3),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 4),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 5),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 6),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 7),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 8),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 9),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 10),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 11),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 12),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 13),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 14),
    ("https://lehre.idh.uni-koeln.de/site/assets/files/5151/romeo.txt", 15),
]


def decargar_archivo(url,i):
    print("Descargando archivo...")
    nombre = url.split("/")[-1]
    nombre = nombre + f"_{i}"

    ruta = CARPETA / nombre
    r = requests.get(url)
    with open(ruta, "wb") as f:
        f.write(r.content)
    return nombre


hilos = []

# Creacion de hilos

for link, i in urls:
    hilo = threading.Thread(target=decargar_archivo, args=(link,i))
    hilos.append(hilo)
    hilo.start()

for hilo in hilos:
    hilo.join()

print("Archivos descargados.")