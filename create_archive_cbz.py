from urllib.parse import urlparse
from zipfile import ZipFile
import os

class CreateArchive:
    
    def __init__(self, links, destination_folder,download_images):
        
        self.links = links
        self.destination_folder = destination_folder
        self.download_images = download_images
        
    def generar_nombre_cbz(self,url):
         
         parsed_url = urlparse(url)
         path_segments = parsed_url.path.split("/")
     
         # Obtener el nombre del manga y del capítulo
         nombre_manga = path_segments[-3]
         numero_capitulo = path_segments[-2]  # Se asume que el número del capítulo está en la penúltima posición
     
         # Generar el nombre del archivo CBZ
         nombre_cbz = f"{nombre_manga}_{numero_capitulo}.cbz"
     
         return nombre_cbz
 
    def create_cbz(self, cbz_filename):
            
            self.download_images()  # Asegura que las imágenes estén descargadas
            with ZipFile(cbz_filename, 'w') as zip_file:
                
                for i, link in enumerate(self.links, 1):
                    image_path = os.path.join(self.destination_folder, f"page_{i}.jpg")
    
                    if os.path.exists(image_path):
                        zip_file.write(image_path, os.path.relpath(image_path, self.destination_folder))
                    
    
    def delete_images(self):
            
            for i in range(1, len(self.links) + 1):
                image_path = os.path.join(self.destination_folder, f"page_{i}.jpg")
                if os.path.exists(image_path):
                    os.remove(image_path)