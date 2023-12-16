import os
import subprocess
from urllib.parse import urlparse, unquote
from link_extractor import LinkExtractor
from manga_d import MangaDownloader
from bs4 import BeautifulSoup
import requests

base_url = "https://www.mangaread.org" 

def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica si la solicitud fue exitosa
        return response.text  # Devuelve el contenido HTML de la respuesta
    except requests.exceptions.RequestException as e:
        print(f"Error al obtener el contenido HTML: {e}")
        return None


def extract_links(html_content):
    links_c = []

    soup = BeautifulSoup(html_content, 'html.parser')

    # Encuentra todos los elementos li con la clase wp-manga-chapter
    chapter_elements = soup.find_all('li', class_='wp-manga-chapter')

    for chapter_element in chapter_elements:
        # Encuentra el enlace dentro del elemento a
        link_element = chapter_element.find('a')
        if link_element:
            link = link_element.get('href')
            links_c.append(link)

    return links_c

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
    url ="https://www.mangaread.org/manga/dark-fantasy-paladin/"
    print(" ")
    destination_folder = r"C:\Users\jesuc\Documents\Pruebas"
    print(" ")

    

    
    links_c = extract_links(get_html_content(url))
    links_c.reverse()

    for i in range(len(links_c)):
     extractor = LinkExtractor()
     links = extractor.get_links(links_c[i])
     full_links = [base_url + link for link in links]
     nombre_cbz = generar_nombre_cbz(links_c[i])  # Define the variable "nombre_cbz"
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
