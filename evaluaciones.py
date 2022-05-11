from pizza import Pizza

# Mostrar en pantalla los valores de los atributos de clase de la clase importada sin instanciarla
print(f'El tamaño de la pizza es {Pizza.size} y su precio es ${Pizza.price}')

# Usar el método creado en el requerimiento 2 sin crear una instancia de la clase importada
salsas = ['salsa de tomate', 'salsa bbq']
print(Pizza.validar_elemento('salsa de tomate', salsas))

# Crear una instancia de la clase importada y luego llamar al método del requerimiento 3
pizza_uno = Pizza()
pizza_uno.pedido()

# Mostrar en pantalla los ingredientes de la instancia creada en el paso anterior y si es una pizza válida o no
print(f'Su pedido:\n Vegetal 1: {pizza_uno.vegetal_uno}\n Vegetal 2: {pizza_uno.vegetal_dos}\n Proteína: {pizza_uno.proteina}\n Masa: {pizza_uno.masa}\n')
print(f'¿Pizza válida? {pizza_uno.pizza_valida}')

# Mostrar si la clase Pizza es una pizza válida o no sin crear una instancia de la clase
print(f'¿Pizza válida? {Pizza.pizza_valida}')
