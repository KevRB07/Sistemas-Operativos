import threading
import time

#Crear un semaforo con un contador inicial de 2 
semaphore = threading.Semaphore(1)

def tarea(id):
    print(f"Tarea {id} intentando acceder al recurso")
    with semaphore:
         print(f"Tarea {id} ha adquirido el semaforo")
         time.sleep(2)
         print(f"Tarea {id} ha liberado el semaforo")

#Crear multiples hilos que ejecuten la funcion 'tarea'
threads = []
for i in range(5):
    thread = threading.Thread(target=tarea, args=(i,))
    threads.append(thread)
    thread.start()

#Esperar a que todos los hilos terminen
for thread in threads:
    thread.join()	 
