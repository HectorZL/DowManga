from playwright.sync_api import sync_playwright

class LinkExtractor:
    def __init__(self):
        self.user_data = r'C:\Users\jesuc\AppData\Local\Microsoft\Edge\User Data'
        self.chrome_path = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    
    def get_links(self, url_curso: str) -> list:
        found_links = []
        
        try:
            with sync_playwright() as p:
                # Lanza el navegador Edge en modo no headless para ver lo que sucede
                context = p.chromium.launch_persistent_context(user_data_dir=self.user_data, executable_path=self.chrome_path, headless=True)
                page = context.new_page()
                print("__" * 50)
                print("Navegando a la página...")
                page.goto(url_curso, wait_until="domcontentloaded")
                print("Esperando a que la página cargue completamente...")

                # Espera a que los elementos de imagen se carguen
                page.wait_for_selector('.reading-content img.wp-manga-chapter-img')

                print("Buscando enlaces en la página...")
                print("__" * 50)

                # Encuentra todos los enlaces con la clase especificada
                link_elements = page.query_selector_all('.reading-content img.wp-manga-chapter-img')
                
                # Extrae y almacena los href de los enlaces encontrados
                for link_element in link_elements:
                    found_links.append(link_element.get_attribute('src'))
                
        except Exception as e:
            print("Ocurrió un error al obtener los enlaces:", str(e))
                        
        return found_links


