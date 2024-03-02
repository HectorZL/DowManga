import os
import subprocess
from urllib.parse import urlparse, unquote
from link_extractor import LinkExtractor
from manga_download import MangaDownloader
from create_archive_cbz import CreateArchive
from bs4 import BeautifulSoup
from utils import utilidades
import requests

base_url = "https://www.mangaread.org" 

def main():
    
    print(" ")
    
    #url=input("Ingrese el link del manga a descargar : ")
    url ="https://www.mangaread.org/manga/solo-leveling-manhwa/"
    
    #destination_folder = input(" Ingrese el link del manga a descargar : ")
    destination_folder = r"C:\Users\HectorZL\Documents\test"

    
    obj = utilidades() 
    all_links = obj.extract_links(obj.get_html_content(url))
    all_links.reverse()
    
    
    print(" ")
    
   
    
    print(" ")

    
    

    
    print(f"Total de links encontrados: {len(all_links)}")
    
    print(" ")
    
    start_index = int(input("Desde qué número de enlace deseas reanudar la descarga: "))
    
    print(" ")
    
    for i in range(start_index - 1, len(all_links)):
        
        extractor = LinkExtractor()
        link = extractor.get_links(all_links[i])
        
        
        
        
        full_links = [base_url + link for link in link]

        

        downloader = MangaDownloader(link, destination_folder, i+1)
        archive = CreateArchive(all_links, destination_folder,downloader.download_images)
        nombre_cbz = archive.generar_nombre_cbz(all_links[i]) 
        
        
        # Verificar si el archivo ya existe
        cbz_path = os.path.join(destination_folder, nombre_cbz)
        if os.path.exists(cbz_path):
            print(f"El archivo {nombre_cbz} ya existe. Pasando al siguiente enlace.")
            continue
                
        retry_count = 0
        while retry_count < 3:
            try:
                archive.create_cbz(os.path.join(destination_folder, nombre_cbz))
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

        archive.delete_images()

if __name__ == "__main__":
     main()
