print("Hola, este es un programa de gestion de tareas")
print("Ingresa el numero de la tarea a realizar")
print("1. Agregar tarea")
print("2. Ver tareas")
print("3. Marcar como completada")
print("4. Eliminar la ultima tarea")
print("5. Salir")
file = open("Tasks.txt", "r")
if (file == None):
    file = open("Tasks.txt", "w")
    file.close()
    file = open("Tasks.txt", "r")
Tasks = []
for task in file:
    Tasks.append(task.strip())
file.close()
option = int(input())
def addTask(Tasks):
    print("Ingresa la tarea")
    task = input()
    Tasks.append(task)
    print("Tarea agregada")
def showTasks(Tasks):
    print("Tareas")
    i = 0
    for task in Tasks:
        print(str(i) + ". " + task)
        i += 1
def completedTask(Tasks):
    print("Ingresa el numero de la tarea completada")
    showTasks(Tasks)
    task = int(input())
    Tasks.pop(task)
    print("Tarea completada")
def deleteTasks(Tasks):
    Tasks.pop()
    print("Tarea eliminada")
def saveTasks(Tasks):
    with open("Tasks.txt", "w") as file:
        for task in Tasks:
            file.write(task + "\n")
    print("Tareas guardadas")
while option !=5:
    if option ==1:
        addTask(Tasks)
    elif option ==2:
        showTasks(Tasks)
    elif option ==3:
        completedTask(Tasks)
    elif option ==4:
        deleteTasks(Tasks)
    print("Ingresa el numero de la tarea a realizar")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar como completada")
    print("4. Eliminar la ultima tarea")
    print("5. Salir")
    option = int(input())
saveTasks(Tasks)