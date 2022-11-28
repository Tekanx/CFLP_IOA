# Install dependencies
# -- IMPORTED --
import csv
import math
import time
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# HYPERPARAMETERS
file = "cap41.txt"

# Random Bit flip generation for initial solution
def bitFlipWarehouse(K, nWarehouses, warehousesData):
    contOpened = 0
    contClosed = 0 
    warehouseDisponibility = []
    for i in range(nWarehouses):
        #Si el costo del almacen es 0, significa que debe ser el principal. 
        #Sino, cualquier otro almacen
        if(warehousesData[i][1] == 0): 
            warehouseDisponibility.append(1)
            contOpened += 1
        else:
            randBit = random.randint(0,1)
            if(randBit == 1):
                if(contOpened < K):
                    warehouseDisponibility.append(1)
                    contOpened += 1
                else: 
                    warehouseDisponibility.append(0)
                    contClosed += 1         
            else: 
                if(contClosed < (nWarehouses - K)):
                    warehouseDisponibility.append(0)
                    contClosed += 1
                else:
                    warehouseDisponibility.append(1)
                    contOpened += 1
                    
    return warehouseDisponibility

# Lectura del archivo
def readFile():
    settings = []
    with open(file) as rf:    
        rf = csv.reader(rf)    
        for row in rf:        
            settings.append(row[0])  
    return settings

def generateCountWarehousesCustomers(data):
    # Setting principal de cantidad de almacenes y clientes de la primera fila
    nWarehouses = int(data[0].split()[0])
    nCustomers = int(data[0].split()[1])
    return (nWarehouses, nCustomers)

def evaluateWarehouses(data, nWarehouses, nCustomers):
    warehouses = [] 
    # Lectura de primer y segundo valor después de la lectura de la primera fila hasta nWarehouses.
    for i in range(1, nWarehouses+1):
        capacityWarehouse= int(data[i].split()[0])
        fixedCost = data[i].split()[1]
        fixedCost = int(fixedCost.replace('.', ''))
        fixedWarehouseCost = fixedCost
        warehouses.append((capacityWarehouse, fixedCost))
    #print("Capacity of Warehouses:",capacityWarehouse)
    #print("Fixed Warehouses Cost:", fixedWarehouseCost)
    return warehouses

def evaluateCustomers(data, nWarehouses, nCustomers):
    # length: Cantidad de líneas a leer de demandas de i almacenes.
    # lines: Cantidad de líneas a leer a partir de la lectura inicial.
    length = math.ceil(nWarehouses / 7)
    lines = ((1 + length) * nCustomers) + nWarehouses + 1
    # Lectura comienza a partir de la linea (nWarehouses + 1) hasta el término del archivo con paso 
    # del largo de líneas a leer de demandas de i almacenes del cliente.
    customers = []
    count = 0
    for i in range(nWarehouses + 1, lines, length + 1):
        numCost = nWarehouses
        demand = int(data[i])
        allocatingCost = []
        count = 0
        for line in range((i + 1), (i + 1 + length)):
            if(numCost >= 7): size = 7
            else: size = numCost
            print("Costs in line", line, ":", end=' ')
            for cost in range(0, size):
                allocatingCost.append(data[line].split()[cost])
                print(allocatingCost[count], end = ' ')
                count += 1
            print('\n')
            numCost -= size
        customers.append((demand,allocatingCost))       
    return customers


def evaluateInitialSolution(X, warehouses, customers, nWarehouses, nCustomers):
    Y = np.zeros((nWarehouses, nCustomers))
    print(pd.DataFrame(customers[2]))
    costs = np.zeros(nWarehouses)
    print(pd.DataFrame(Y))
    print('Customer demand: \n', pd.DataFrame(customerDemand))
    for j in range(nCustomers):
        i = random.randint(0, (nWarehouses - 1))
        #while(x[i] != 0 and ((costs[i] + customers[][]))):
    return 0
      