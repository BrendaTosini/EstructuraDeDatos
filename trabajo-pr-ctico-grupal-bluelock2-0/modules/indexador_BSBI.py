from nltk.stem import SnowballStemmer
from nltk.corpus import stopwords
import json
import os
import string
import re
from lxml import etree

class IndexadorBSBI():
    def __init__(self, documentos, salida, temp="../temp", language='spanish'):
        self.documentos = documentos
        self.salida = salida
        self._temp = temp
        self._stop_words = frozenset(stopwords.words(language))
        self._stemmer = SnowballStemmer(language, ignore_stopwords=False)
        self._term_to_termID = {}
        self._lista_documentos_path = []
        self._lista_directorios = os.listdir(self.documentos)

        self._generar_lista()
        self.__generar_docID()
        self.__indexar()
    
    #Genera la lista de los paths de los documentos
    def _generar_lista(self):
        for root, dirs, files in os.walk(self.documentos):
            for filename in files:
                file_path = os.path.join(root, filename)
                self._lista_documentos_path.append(file_path)

    #Genera el dicionario de los paths de los documentos con su respectivo ID 
    def __generar_docID(self):
        doc_path_to_docID = {}
       
        for i in range(len(self._lista_documentos_path)):
            doc_path_to_docID[self._lista_documentos_path[i]] = i
        self._doc_path_to_docID = doc_path_to_docID

    #Lematiza la palabra
    def __lematizar(self, palabra):
        palabra = palabra.strip(string.punctuation + "»" + "\x97" + "¿" + "¡" + "\u201c" + \
                               "\u201d" + "\u2014" + "\u2014l" + "\u00bf")
        palabra_lematizada = self._stemmer.stem(palabra)
        return palabra_lematizada

    #Genera el indice completo por cada bloque
    def __indexar(self):
        lista_bloques = []
        for bloque, nombre_bloque in self.__parse_next_block():
            bloque_invertido = self.__invertir_bloque(bloque)
            lista_bloques.append(self.__guardar_bloque_intermedio(bloque_invertido, nombre_bloque))
        self.__intercalar_bloques(lista_bloques)
        self.__guardar_diccionario_terminos()
        self.__guardar_diccionario_documentos()

    #Genera el indice invertido por cada bloque
    def __invertir_bloque(self, bloque):
        bloque_invertido = {}
        bloque_ordenado = sorted(bloque, key=lambda tupla: (tupla[0], tupla[1]))
        for par in bloque_ordenado:
            posting = bloque_invertido.setdefault(par[0], set())
            posting.add(par[1])
        return bloque_invertido

    #Guarda cada indice invertido por bloque en un archivo json
    def __guardar_bloque_intermedio(self, bloque, nombre_bloque):
        archivo_salida = nombre_bloque + ".json"
        archivo_salida = os.path.join(self._temp, archivo_salida)
        for clave in bloque:
            bloque[clave] = list(bloque[clave])
        with open(archivo_salida, "w") as contenedor:
            json.dump(bloque, contenedor)
        return archivo_salida

    #Une los bloques formando el indice completo y lo guarda en postings.json 
    def __intercalar_bloques(self, lista_bloques):
        lista_termID = [str(i) for i in range(len(self._term_to_termID))]
        posting_file = os.path.join(self.salida, "postings.json")

        with open(posting_file, "w") as salida:
            postings = {}
            for bloque in lista_bloques:
                with open(bloque, "r", encoding="utf-8") as data:
                    bloque_data = json.load(data)
                    for termID in lista_termID:
                        try:
                            posting = postings.get(termID, list())
                            postings[termID] = list(set(posting + bloque_data[termID]))
                        except:
                            pass

            json.dump(postings, salida)

    #Guarda el diccionario term_to_termID en diccionario_terminos.json
    def __guardar_diccionario_terminos(self):
        path = os.path.join(self.salida, "diccionario_terminos.json")
        with open(path, "w") as contenedor:
            json.dump(self._term_to_termID, contenedor)
    
    #Guarda el diccionario doc_path_to_docID en diccionario_documentos.json
    def __guardar_diccionario_documentos(self):
        path = os.path.join(self.salida, "diccionario_documentos.json")
        with open(path, "w") as contenedor:
            json.dump(self._doc_path_to_docID, contenedor)

    #Genera el bloque de pares por cada medio
    def __parse_next_block(self):
        termID = 0
        bloque = []

        for direct in self._lista_directorios:
            dir_path = os.path.join(self.documentos, direct)
            for nombre_doc in os.listdir(dir_path):
                doc_path = os.path.join(dir_path, nombre_doc)
                tree = etree.parse(doc_path)
                lineas = tree.xpath("//title/text() | //description/text()")
                for linea in lineas:
                    linea = self.strip_tags(linea)
                    palabras = linea.split()
                    for pal in palabras:
                        if pal not in self._stop_words:
                            pal = self.__lematizar(pal)
                            if pal not in self._term_to_termID:
                                self._term_to_termID[pal] = termID
                                termID += 1
                            bloque.append((self._term_to_termID[pal], self._doc_path_to_docID[doc_path]))
        
            yield bloque, direct
            bloque = []

    # Utiliza una expresión regular para eliminar las etiquetas HTML
    @staticmethod
    def strip_tags(linea): 
        return re.sub(r'&lt;/?[ul|i]&gt;', '', linea)        

if __name__ == '__main__':
    indexador_BSBI = IndexadorBSBI("../data_xml/", "../salida")
    print("Longitud de la lista de documentos: ", len(indexador_BSBI._lista_documentos_path))
    print(f"Archivo cargados correctamente")
