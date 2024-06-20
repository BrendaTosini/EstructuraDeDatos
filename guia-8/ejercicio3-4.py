from lxml import etree

tree = etree.parse("./shaks200/r_and_j.xml")

lineas_romeo = len(tree.xpath('//SPEECH[SPEAKER = "ROMEO"]/LINE'))
print(lineas_romeo)

lineas_juliet = len(tree.xpath('//SPEECH[SPEAKER = "JULIET"]/LINE'))
print(lineas_juliet)

if lineas_romeo > lineas_juliet:
    print("Romeo tiene mas lineas")
else:
    print("Juliet tiene mas lineas")
