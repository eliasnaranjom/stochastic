from graphviz import Digraph

# Lista de actividades - Punto 1
# actividades = [
#     {'name':'A', 'time': 0, 'pre': [], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'B', 'time': 8, 'pre': ['A'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'C', 'time': 0.1, 'pre': ['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'D', 'time': 1, 'pre': ['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'E', 'time': 1, 'pre': ['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'F', 'time': 1, 'pre': ['D'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'G', 'time': 2, 'pre': ['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'H', 'time': 3, 'pre': ['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'I', 'time': 1, 'pre': ['G', 'E'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'J', 'time': 4, 'pre': ['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'K', 'time': 2, 'pre': ['J'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'L', 'time': 1, 'pre': ['F', 'H', 'K'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'M', 'time': 0.5, 'pre': ['L'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'N', 'time': 2, 'pre': ['I'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'O', 'time': 1, 'pre': ['N'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'P', 'time': 1.5, 'pre': ['N'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'Q', 'time': 5, 'pre': ['C'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'R', 'time': 1, 'pre': ['M', 'O', 'P', 'Q'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'S', 'time': 0.5, 'pre': ['R'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'T', 'time': 1, 'pre': ['S'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name':'U', 'time': 0, 'pre': ['T'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
# ]

# Lista de actividades - Punto 2
# actividades = [
#     {'name': 'A', 'time': 3, 'pre': [], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name': 'B', 'time': 4, 'pre': ['A'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name': 'C', 'time': 6, 'pre': ['A'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name': 'D', 'time': 6, 'pre': ['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name': 'E', 'time': 4, 'pre': ['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name': 'F', 'time': 4, 'pre': ['C'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name': 'G', 'time': 6, 'pre': ['D'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
#     {'name': 'H', 'time': 8, 'pre': ['E', 'F'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
# ]

# Lista de actividades - Punto 3
actividades = [
    {'name':'A', 'time':5, 'pre':[], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
    {'name':'B', 'time':2, 'pre':['A'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
    {'name':'C', 'time':4, 'pre':['A'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
    {'name':'D', 'time':5, 'pre':['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
    {'name':'E', 'time':5, 'pre':['B'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
    {'name':'F', 'time':5, 'pre':['C'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
    {'name':'G', 'time':2, 'pre':['E', 'F'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
    {'name':'H', 'time':3, 'pre':['D'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
    {'name':'I', 'time':5, 'pre':['G', 'H'], 'ip': 0, 'tp': 0, 'it': 0, 'tt': 0, 'h': 0},
]

# Crear el grafo
g = Digraph('pert2')


def searchTp(name):
    for actividad in actividades:
        if actividad['name'] == name:
            return actividad['tp']

def searchIl(name):
    for actividad in actividades:
        if actividad['name'] == name:
            return actividad['it']

    # Si no se encuentra la actividad, retornar -1 como indicador de error
    return -1

# Crear los nodos
for actividad in actividades:
    ip=0
    it=0
    tt=0

    # Crear las aristas
    # Calcular el tiempo más temprano de inicio (IP) de la actividad
    for predecesor in actividad['pre']:
        g.edge(predecesor, actividad['name'])
        if predecesor is not []:
            ip = max(ip, searchTp(predecesor))
            actividad['ip'] = ip
    
    actividad['tp'] = ip + actividad['time']

ultimo=actividades[-1]
tt=ultimo["tp"]
ultimo["tt"]=tt
it=ultimo["tt"]-ultimo["time"]
ultimo["it"]=it

for actividad in reversed(actividades):
    # Calcular el tiempo más tardío de terminación (TT) de la actividad
    for sucesor in actividades:
        if actividad is not actividades[-1] and actividad['name'] is not sucesor['pre'] and actividad['name'] in sucesor['pre']:
            actividad['tt'] = min(tt, searchIl(sucesor['name']))
            actividad['it'] = actividad['tt'] - actividad['time']

    #Horgura
    actividad['h'] = actividad['tt'] - actividad['tp']


    # Crear el label del nodo con los valores de la actividad
    label = f'{actividad["name"]}\nDuración={actividad["time"]}\nInicio pronto={actividad["ip"]}\nTerminación pronta={actividad["tp"]}\nInicio lejano={actividad["it"]}\nTerminación lejana={actividad["tt"]}\nHolgura={actividad["h"]}'

    # Crear el nodo con el label
    g.node(actividad['name'], label=label)

criticalRouter=[]
for actividad in actividades:
    if actividad['h']==0:
        criticalRouter.append(actividad['name'])

# Agregar nodo final con texto
g.node('Z', label=f'\n\nRuta critica: {criticalRouter}')

# Renderizar y mostrar en una ventana emergente
g.render('export/punto3', view=True, format='pdf')

print("¡Diagrama y ruta critica generada con exito!")