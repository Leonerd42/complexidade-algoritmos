import sys
import csv
import time 

limites = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 50000, 100000]

def seletion_sort(A): 
    for i in range(len(A)):   
        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j 
        aux = A[i]       
        A[i] = A[min_idx]
        A[min_idx] = aux
        #A[i], A[min_idx] = A[min_idx], A[i] 
    return A

def merge(llist, rlist): 
    final = []
    while llist or rlist: 
        if len(llist) and len(rlist): 
            if llist[0] < rlist[0]: 
                final.append(llist.pop(0))
            else: 
                final.append(rlist.pop(0))

        if not len(llist): 
            if len(rlist): 
                final.append(rlist.pop(0))
        if not len(rlist): 
            if len(llist):
                final.append(llist.pop(0))
    return final 

def merge_sort(list): 
    if len(list) < 2: 
        return list
    mid = int(len(list) / 2)
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]))

def BubbleSort(A): 
    trocado = True 
    while trocado: 
        trocado = False 
        for i in range(len(A) - 2):
            if A[i] > A[i+1]: 
                A[i], A[i+1] = A[i+1], A[i]
                trocado = True
    return A
    
with open('performance-bubble.csv', mode='w') as data_file:
        data_writer = csv.writer(data_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        data_writer.writerow(['quant', 'tempo', 'inicial_vetor'])
    
        for limite in limites: 
            with open('data_set-'+str(limite)+'.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                line_count = 0
                for row in csv_reader:
                    row[:] = list(map(int, row))
                    start = time.time()
                    ordenado = BubbleSort(row)
                    end = time.time()
                    tempo = end - start

                    tipo_vetor = ''
                    if line_count == 0: 
                        tipo_vetor = 'ordenado'
                    elif line_count == 1: 
                        tipo_vetor = 'invertido_ordenado'
                    else: tipo_vetor = 'aleatorio'
                    
                    data_writer.writerow([limite, tempo, tipo_vetor])
                    line_count = line_count + 1
                print('done ' + str(limite))
                
                    # executa o selecion sort 





