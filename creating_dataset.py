import csv
import random
print('iniciando programa')

# criando um data set grande 
limites = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 50000, 100000]

for limite in limites: 
    # Executar o codigo 
    ordenado = []

    for i in range(limite): 
        ordenado.append(i)

    inverso_ordenado = list(ordenado)
    inverso_ordenado.reverse() 

    aleatorio = []
    for i in range(limite): 
        aleatorio.append(random.randint(-limite, limite))

    with open('data_set-' + str(limite) + '.csv', mode='w') as employee_file:
        print('abrindo')
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        employee_writer.writerow(ordenado)
        employee_writer.writerow(inverso_ordenado)
        employee_writer.writerow(aleatorio)