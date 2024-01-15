import os
import subprocess
from urllib.parse import urlparse, unquote
from link_extractor import LinkExtractor
from manga_d import MangaDownloader
from bs4 import BeautifulSoup
from utils import utilidades
import requests

base_url = "https://www.mangaread.org" 

def main():
    
    print(" ")
    
    #url=input("Ingrese el link del manga a descargar : ")
    url ="https://www.mangaread.org/manga/solo-leveling-manhwa/"
    
    obj = utilidades() 
    links = obj.extract_links(obj.get_html_content(url))

    
    print(" ")
    
    #destination_folder = input(" Ingrese el link del manga a descargar : ")
    destination_folder = r"C:\Users\jesuc\Documents\test_dow_sololeveling"
    
    print(" ")

    
    links.reverse()

    
    print(f"Total de links encontrados: {len(links)}")
    start_index = int(input("Desde qué número de enlace deseas reanudar la descarga: "))

    for i in range(start_index - 1, len(links)):
        
        extractor = LinkExtractor()
        links = extractor.get_links(links[i])
        full_links = [base_url + link for link in links]
        nombre_cbz = obj.generar_nombre_cbz(links[i])  # Define the variable "nombre_cbz"
        downloader = MangaDownloader(links, destination_folder, i+1)
        
        retry_count = 0
        while retry_count < 3:
            try:
                downloader.create_cbz(os.path.join(destination_folder, nombre_cbz))
                break  # Si la descarga es exitosa, salir del bucle while
            
            except Exception as e:
                
                print(f"Error al descargar el capítulo {i+1}: {e}")
                retry_count += 1
                print(f"Reintentando... (Intento {retry_count})")
                
            except internetdisconnected.err_internet_disconnected as e:
                print(f"Error de conexión a Internet detectado: {e}. Verificar conexión.")
                break;
            
        if retry_count == 3:
            
            print(f"No se pudo descargar el capítulo {i+1} después de 3 intentos. Deteniendo el programa")
            break;

        downloader.delete_images()

if __name__ == "__main__":
     main()
