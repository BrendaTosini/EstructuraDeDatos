import configparser
import os
import feedparser
import xml.etree.ElementTree as ET
import schedule
import time

class RecoleccionDeNoticias():

    def realizar_solicitudes_guardar_xml(archivo_config):
        try:
            # Leer el archivo de configuración
            config = configparser.ConfigParser()
            config.read(archivo_config)

            #Recorre por secciones del config que son los medios 
            for medio in config.sections():
                if medio != 'ENV':
                    url_base = config[medio]['url_base']

                    #Recorre el dicionaro de cada medio
                    for clave, valor in config.items(medio):
                        if clave != 'url_base':
                            url = url_base + valor
                            path_archivo_xml = '../data_xml/' + medio + '/' + clave + '.xml'
                            
                            try:
                                #Si el archivo ya existe genera un arbol y recopila las noticas
                                tree = ET.ElementTree(file=path_archivo_xml)
                                root = tree.getroot()
                                noticias_recopiladas = {(item.find("title").text, item.find("pubDate").text) for item in root}
                            except FileNotFoundError:
                                # Si el archivo y el directorio no exite crea el directorio y crea un root para el arbol
                                if not os.path.exists(f'../data_xml/{medio}'):
                                    os.mkdir(f'../data_xml/{medio}')
                                root = ET.Element("channel")
                                noticias_recopiladas = set()
                            
                            try:
                                #Crea un feed del xml que esta en servidor
                                feed = feedparser.parse(url)

                                #Recorre el feed por noticia
                                for noticia in feed.entries:
                                    titulo = noticia.title
                                    fecha_publicacion = noticia.published
                                    descripcion = getattr(noticia, 'summary', 'Unknown description')
                                    link = getattr(noticia, 'link', 'Unknown link')

                                    #Valida que la noticia no este recopilada y genera el arbol xml de la noticia
                                    if (titulo, fecha_publicacion) not in noticias_recopiladas:
                                        item = ET.SubElement(root, "item")
                                        titulo_element = ET.SubElement(item, "title")
                                        titulo_element.text = titulo
                                        fecha_element = ET.SubElement(item, "pubDate")
                                        fecha_element.text = fecha_publicacion
                                        descripcion_element = ET.SubElement(item, "description")
                                        descripcion_element.text = descripcion
                                        link_element = ET.SubElement(item, "link")
                                        link_element.text = link

                                        noticias_recopiladas.add((titulo, fecha_publicacion))

                                #Guarda el arbol actualizado en el archivo xml
                                tree = ET.ElementTree(root)
                                ET.indent(tree, space="\t", level=0)
                                tree.write(path_archivo_xml, encoding="utf-8")
                                print(f"Noticias agregadas correctamente de: {url}")
                            except Exception as e:
                                print(f"Error al analizar el feed RSS desde {url}: {e}")
        except Exception as e:
            print(f"Ocurrió un error: {e}")
    
    #Repite el metodo realizar_solicitudes_guardar_xml cada 10 minutos
    def repetir_recoleccion(archivo_config):
        config = configparser.ConfigParser()
        config.read(archivo_config)
        intervalo_minutos = config['ENV']['query_interval']  # Intervalo de tiempo en minutos para recoger noticias
        RecoleccionDeNoticias.realizar_solicitudes_guardar_xml(archivo_config)
        schedule.every(int(intervalo_minutos)).minutes.do(RecoleccionDeNoticias.realizar_solicitudes_guardar_xml, archivo_config)
    
        while True:
            schedule.run_pending()
            time.sleep(int(intervalo_minutos))

if __name__ == '__main__':
    RecoleccionDeNoticias.repetir_recoleccion("../config/config.ini")

