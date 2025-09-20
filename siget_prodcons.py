import threading
import time
import random

# Buffer compartido
buffer = []
buffer_size = 5

# Lock para sincronizar acceso al buffer
lock = threading.Lock()

def productor():
    for i in range(10):
        item = random.randint(1, 100)
        with lock:  # sección crítica
            if len(buffer) < buffer_size:
                buffer.append(item)
                print(f"🛠️ Productor produjo: {item} | Buffer: {buffer}")
        time.sleep(random.uniform(0.5, 1.5))

def consumidor():
    for i in range(10):
        with lock:  # sección crítica
            if buffer:
                item = buffer.pop(0)
                print(f"👤 Consumidor consumió: {item} | Buffer: {buffer}")
        time.sleep(random.uniform(1, 2))

# Crear hilos
t1 = threading.Thread(target=productor)
t2 = threading.Thread(target=consumidor)

# Iniciar hilos
t1.start()
t2.start()

# Esperar a que terminen
t1.join()
t2.join()

print("✅ Simulación completada")
