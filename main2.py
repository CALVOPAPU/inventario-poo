# ==========================================================
# main.py - Pruebas del sistema de inventario tecnológico
# Solo contiene importaciones, instanciación y pruebas.
# ==========================================================
from modelos import Procesador, Bateria, Laptop, LaptopGamer

# --- Instanciación de objetos (1 de la clase base y 2 de la subclase) ---
laptop1 = Laptop("HP", "Pavilion", 8,
                 Procesador("Intel Core i5-1235U", 10, 4.4), Bateria(45))
gamer1 = LaptopGamer("ASUS", "TUF A15", 16,
                     Procesador("AMD Ryzen 7 7840HS", 8, 5.1), Bateria(90),
                     "RTX 4060", 144)
gamer2 = LaptopGamer("MSI", "Raider GE78", 32,
                     Procesador("Intel Core i9-13900H", 14, 5.4), Bateria(99),
                     "RTX 4080", 240, True)

print("=== 1. COMPOSICIÓN: la laptop delega en sus componentes ===")
laptop1.ver_info()
laptop1.encender()   # llama a procesador.iniciar()
laptop1.usar(15)     # llama a bateria.consumir()

print("\n=== 2. HERENCIA Y POLIMORFISMO (ver_info y usar sobrescritos) ===")
gamer1.ver_info()
gamer1.encender()    # método heredado
gamer1.activar_turbo()
gamer1.usar(10)      # con turbo gasta el doble
laptop1.usar(10)     # sin turbo gasta lo normal
gamer1.ver_info()

print("\n=== 3. ENCAPSULAMIENTO: validación de la RAM ===")
print(f"RAM actual (getter): {laptop1.GBRAM}GB")
laptop1.aumentar_ram(8)
try:
    laptop1.GBRAM = -4
except ValueError as error:
    print(f"Error controlado: {error}")
print(f"RAM final: {laptop1.GBRAM}GB")

print("\n=== 4. INDEPENDENCIA DE DATOS ENTRE INSTANCIAS ===")
gamer2.ver_info()
print(f"RAM -> laptop1: {laptop1.GBRAM}GB | gamer1: {gamer1.GBRAM}GB | gamer2: {gamer2.GBRAM}GB")
print(f"Encendida -> laptop1: {laptop1.encendida} | gamer1: {gamer1.encendida} | gamer2: {gamer2.encendida}")
gamer2.apagar()
print(f"Tras apagar gamer2 -> gamer1: {gamer1.encendida} | gamer2: {gamer2.encendida}")
