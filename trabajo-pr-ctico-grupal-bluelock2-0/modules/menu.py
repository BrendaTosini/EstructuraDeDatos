

from busqueda_booleana import BusquedaBooleana

class Menu():

    def menu_consulta(self):
        print("Elija cual va a ser la primer parte de la consulta: ")
        print("Escriba una palabra a buscar: ")
        parte1= input()
        print("Elija el condicional: ")
        print("1-AND\n2-OR\n3-AND NOT")
        condicional=input()
        print("Elija cual va a ser la segunda parte de la consulta: ")
        print("1-Palabra\n2-Subconsulta")
        opcion= input()
        if opcion == "1":
            print("Escriba una palabra a buscar: ")
            parte2= input()
        else:
            print("Escriba la primera palabra de la subconsulta: ")
            palabra = input()  
            print("Elija el condicional: ")
            print("1-AND\n2-OR\n3-NOT")
            condicional_sub=input()
            print("Escriba la segunda palabra de la subconsulta: ")
            palabra2=input()
            parte2="("+ palabra + " " + condicional_sub + " " + palabra2 + ")"

        busqueda = BusquedaBooleana()
        set_de_documentos = busqueda.consulta_booleana(parte1,condicional,parte2)
        print(f"Estos son los documentos asociados: {list(set_de_documentos)}")

if __name__ == '__main__':
    menu = Menu()
    menu.menu_consulta()