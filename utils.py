from bs4 import BeautifulSoup
import requests
from urllib.parse import urlparse, unquote


class utilidades:


    
 def get_html_content(self,url):
     
     try:         
         response = requests.get(url)
         response.raise_for_status()  # Verifica si la solicitud fue exitosa
         return response.text  # Devuelve el contenido HTML de la respuesta
     
     except requests.exceptions.RequestException as e:
         
         print(f"Error al obtener el contenido HTML: {e}")
         return None
 
 
 def extract_links(self,html_content):
     
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
 
 def generar_nombre_cbz(self,url):
     
     parsed_url = urlparse(url)
     path_segments = parsed_url.path.split("/")
 
     # Obtener el nombre del manga y del capítulo
     nombre_manga = path_segments[-3]
     numero_capitulo = path_segments[-2]  # Se asume que el número del capítulo está en la penúltima posición
 
     # Generar el nombre del archivo CBZ
     nombre_cbz = f"{nombre_manga}_{numero_capitulo}.cbz"
 
     return nombre_cbz