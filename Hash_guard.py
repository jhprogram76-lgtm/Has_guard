import hashlib
import os
import json

DB_FILE = "file_hashes.json"
CARPETA_AUDITAR = "./critical_files"

def calcular_hash(ruta_archivo):
    """Genera el hash SHA-256 de un archivo."""
    sha256_hash = hashlib.sha256()
    with open(ruta_archivo, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def inicializar_auditoria():
    """Crea una base de datos con los hashes actuales."""
    hashes = {}
    if not os.path.exists(CARPETA_AUDITAR):
        os.makedirs(CARPETA_AUDITAR)
        with open(os.path.join(CARPETA_AUDITAR, "test.txt"), "w") as f:
            f.write("Archivo de prueba seguro")

    for root, _, files in os.walk(CARPETA_AUDITAR):
        for f in files:
            path = os.path.join(root, f)
            hashes[path] = calcular_hash(path)
    
    with open(DB_FILE, "w") as f:
        json.dump(hashes, f, indent=4)
    print(f"[+] Base de datos de integridad generada en {DB_FILE}")

def verificar_integridad():
    """Compara los archivos actuales con la base de datos."""
    if not os.path.exists(DB_FILE):
        print("[!] No hay base de datos. Ejecuta primero la inicialización.")
        return

    with open(DB_FILE, "r") as f:
        hashes_viejos = json.load(f)
    
    print("[*] Verificando integridad de archivos...")
    cambios_detectados = 0

    for path, hash_grabado in hashes_viejos.items():
        if not os.path.exists(path):
            print(f"🚨 ELIMINADO: {path}")
            cambios_detectados += 1
            continue
        
        hash_actual = calcular_hash(path)
        if hash_actual != hash_grabado:
            print(f"🚨 MODIFICADO: {path}")
            cambios_detectados += 1

    if cambios_detectados == 0:
        print("[✓] Integridad verificada. No se detectaron intrusiones en los archivos.")

if __name__ == "__main__":
    opcion = input("1. Inicializar/Actualizar DB\n2. Verificar Integridad\nSelecciona: ")
    if opcion == "1":
        inicializar_auditoria()
    else:
        verificar_integridad()
