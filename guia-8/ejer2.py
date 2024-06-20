from lxml import etree as ET
import os


def recorrerObras():
    
    path_carpeta= "Guia XML" + "/shaks200/"

    path_playlist = "Guia XML" + "/shaks200/playlist"

    with open(path_playlist, encoding="utf-8") as playlist:
        lista_xml= playlist.readlines()

    for xml in lista_xml:
        path_xml= path_carpeta + xml.rstrip("\n")
        with open(path_xml, encoding="utf-8") as archivo:
            tree = ET.parse(path_xml)

            titulos= tree.xpath("//PLAY/TITLE")
            print("TITULO: ", titulos[0].text)

            grupos = tree.xpath("//PGROUP")
            for grupo in grupos:
                descripcion= grupo.find("GRPDESCR").text
                print("DESCRIPCION: ", descripcion)

                for child in grupo:
                    if child.tag == "PERSONA":
                        print("PERSONA: ", child.text)
                    

               
                


            

            
    
    
    

recorrerObras()
