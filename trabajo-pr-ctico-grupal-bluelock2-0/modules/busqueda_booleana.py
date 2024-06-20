import json
import re
import string
import os
from nltk.stem import SnowballStemmer

class BusquedaBooleana():

    #Realiza la consulta que pasa el usuario por el menu
    def consulta_booleana(self,parte1, condicional,parte2):
        consulta_check= re.compile(r'^\((\w+)\s(\d)\s(\w+)\)$')
        consulta_match= consulta_check.match(parte2) #si cumple con el patern es una subconsulta

        #Subconsulta
        if consulta_match:
            grupos= consulta_match.groups() # grupos es una lista -> [palabra1,digit_condicional,palabra2]
            if grupos[1] == "1":
                subconsulta = (self.buscar(grupos[0]) & self.buscar(grupos[2]))
            elif grupos[1] == "2":
                subconsulta = (self.buscar(grupos[0]) | self.buscar(grupos[2]))
            else:
                subconsulta = (self.buscar(grupos[0]) - self.buscar(grupos[2]))
        else:
            subconsulta = self.buscar(parte2)

        #Consulta general
        if condicional == "1" :
            resultado = self.buscar(parte1) & subconsulta
        elif condicional == "2":
            resultado = self.buscar(parte1) | subconsulta
        else:
            resultado = self.buscar(parte1) - subconsulta

        return resultado

    #Lematiza la palabra
    def lematizar(self, palabra):
        stemmer = SnowballStemmer("spanish", ignore_stopwords=False)
        palabra = palabra.strip(string.punctuation + "»" + "\x97" + "¿" + "¡" + "\u201c" + \
                               "\u201d" + "\u2014" + "\u2014l" + "\u00bf")
        palabra_lematizada = stemmer.stem(palabra)
        
        return palabra_lematizada

    #Busca la palabra en postings.json
    def buscar(self,palabra):
        lista_de_doc=[]
        palabra_lematizada = self.lematizar(palabra)
        path_terminos = os.path.join("../salida", "diccionario_terminos.json")
        with open(path_terminos, encoding = "utf-8") as palabras:
            dict_palabras = json.load(palabras)
            if palabra_lematizada in dict_palabras.keys():
                #obtenemos el id de la palabra
                id_palabra = dict_palabras[palabra_lematizada]
                path_posting = os.path.join("../salida", "postings.json")
                with open(path_posting, encoding="utf-8") as indice:
                    dict_indice = json.load(indice)
                    lista_de_doc=dict_indice[str(id_palabra)]
        return set(lista_de_doc)     


