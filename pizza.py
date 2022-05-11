import ingredientes

class Pizza():
    size = 'familiar'
    price = 10000

    @staticmethod
    def validar_elemento(elemento: str, lista):
        if elemento in lista:
            return True
        else:
            return False

    def pedido(self):
        self.proteina = input('''Ingrese alguna de las proteinas a continuación:
            -Pollo
            -Vacuno
            -Carne vegetal
            >''').lower()

        self.vegetal_uno = input('''(1)Ingrese alguno de los vegetales a continuación:
            -Tomate
            -Aceitunas
            -Champiñones
            >''').lower()

        self.vegetal_dos = input('''(2)Ingrese alguno de los vegetales a continuación:
            -Tomate
            -Aceitunas
            -Champiñones
            >''').lower()

        self.masa = input('''Ingrese alguno de los tipos de masa a continuación:
            -Tradicional
            -Delgada
            >''').lower()

        proteina_valida = self.validar_elemento(self.proteina, ingredientes.proteinas)
        vegetal_uno_valido = self.validar_elemento(self.vegetal_uno, ingredientes.vegetales)
        vegetal_dos_valido = self.validar_elemento(self.vegetal_dos, ingredientes.vegetales)
        masa_valida = self.validar_elemento(self.masa, ingredientes.masa)

        if proteina_valida and vegetal_uno_valido and vegetal_dos_valido and masa_valida:
            self.pizza_valida = True
        else:
            self.pizza_valida = False
