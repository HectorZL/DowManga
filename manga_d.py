import os
import requests
from zipfile import ZipFile

class MangaDownloader:
    def __init__(self, links, destination_folder):
        self.links = links
        self.destination_folder = destination_folder

    def download_images(self):
        if not os.path.exists(self.destination_folder):
            os.makedirs(self.destination_folder)

        for i, link in enumerate(self.links, 1):
            response = requests.get(link, stream=True)
            image_path = os.path.join(self.destination_folder, f"page_{i}.jpg")

            with open(image_path, 'wb') as image_file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        image_file.write(chunk)

                response.close()  # Cierra la respuesta después de cada descarga

    def create_cbz(self, cbz_filename):
        self.download_images()  # Asegura que las imágenes estén descargadas

        with ZipFile(cbz_filename, 'w') as zip_file:
            for i, link in enumerate(self.links, 1):
                image_path = os.path.join(self.destination_folder, f"page_{i}.jpg")

                if os.path.exists(image_path):
                    zip_file.write(image_path, os.path.relpath(image_path, self.destination_folder))
                else:
                    print(f"Advertencia: No se encontró el archivo {image_path}")
                    
    def delete_images(self):
        for i in range(1, len(self.links) + 1):
            image_path = os.path.join(self.destination_folder, f"page_{i}.jpg")
            if os.path.exists(image_path):
                os.remove(image_path)