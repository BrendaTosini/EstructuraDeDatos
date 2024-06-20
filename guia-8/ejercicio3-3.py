from lxml import etree

indice = {}
path_carpeta="Guia XML" + "/shaks200/"
path_playlist= "Guia XML" + "/shaks200/playlist"
for archivo in open(path_playlist, encoding="UTF-8"):#
    path = path_carpeta + archivo.rstrip('\n')
    tree = etree.parse(path)

    titulo = tree.xpath("//PLAY/TITLE")
    print("Título de la Obra: ", titulo[0].text)
    titulo_text = titulo[0].text
    
    personas = tree.xpath("//PERSONA")
    for persona in personas:
        if persona.text in indice:
            indice[persona.text].add(titulo_text)
        else:
            indice[persona.text] = {titulo_text}
sorted_dict = dict(sorted(indice.items()))
print(sorted_dict)