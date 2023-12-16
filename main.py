import os
import subprocess
from urllib.parse import urlparse, unquote
from link_extractor import LinkExtractor
from manga_d import MangaDownloader


base_url = "https://www.mangaread.org" 

def generar_nombre_cbz(url):
    parsed_url = urlparse(url)
    path_segments = parsed_url.path.split("/")

    # Obtener el nombre del manga y del capítulo
    nombre_manga = path_segments[-3]
    numero_capitulo = path_segments[-2]  # Se asume que el número del capítulo está en la penúltima posición

    # Generar el nombre del archivo CBZ
    nombre_cbz = f"{nombre_manga}_c{numero_capitulo}.cbz"

    return nombre_cbz

def main():

    kill_edge_processes()

    # Solicita al usuario que introduzca un enlace
    print(" ")
    url = input("Por favor, introduzca el enlace del manga ")
    print(" ")
    destination_folder = input("Por favor, introduzca la carpeta de destino para la descarga ")
    print(" ")

    extractor = LinkExtractor()
    links = extractor.get_links(url)

    full_links = [base_url + link for link in links]

    nombre_cbz = generar_nombre_cbz(url)  # Define the variable "nombre_cbz"

    downloader = MangaDownloader(links, destination_folder)
    downloader.create_cbz(os.path.join(destination_folder, nombre_cbz))
    downloader.delete_images()



def kill_edge_processes():

    try:
        print(" ")
        subprocess.run(["taskkill", "/F", "/IM", "msedge.exe", "/T"], check=True)
        print(" ")
    except subprocess.CalledProcessError:
        print(" ")
        print("No se encontraron procesos de Microsoft Edge en ejecución.")
        print(" ")

if __name__ == "__main__":
     main()
