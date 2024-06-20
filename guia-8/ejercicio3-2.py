from lxml import etree

for archivo in open("./shaks200/playlist", encoding="UTF-8"):#
    path = "./shaks200/" + archivo.rstrip('\n')
    tree = etree.parse(path)

    titulo = tree.xpath("//PLAY/TITLE")
    print("Título de la Obra: ", titulo[0].text)

    grupos = tree.xpath("//PGROUP")
    for grupo in grupos:
        print(" Descripción del grupo: ", grupo.find("GRPDESCR").text)
        for persona in grupo.iter("PERSONA"):
            print("  Persona: ", persona.text)
