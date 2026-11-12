# ==========================================================
# modelos.py - Sistema de inventario tecnológico (Avance 3 Final)
# La clase Laptop representa un equipo electrónico dentro de un
# inventario de tecnología. Aquí se definen las clases Procesador y
# Bateria (composición), Laptop (clase base) y LaptopGamer (subclase).
# Autor: Omar Rafael Rodríguez Ochoa
# ==========================================================


# --- Clases auxiliares para Composición ---
class Procesador:
    # Componente independiente: existe por sí solo, sin necesitar una Laptop
    def __init__(self, modelo, nucleos, frecuencia_ghz):
        self.modelo = modelo
        self.nucleos = nucleos
        self.frecuencia_ghz = frecuencia_ghz

    def iniciar(self):
        print(f"  -> Procesador {self.modelo} ({self.nucleos} núcleos, "
              f"{self.frecuencia_ghz} GHz) iniciado.")

    def info(self):
        return f"{self.modelo} ({self.nucleos} núcleos, {self.frecuencia_ghz} GHz)"


class Bateria:
    # Segundo componente: controla el porcentaje de carga
    def __init__(self, capacidad_wh, carga=100):
        self.capacidad_wh = capacidad_wh
        self._carga = carga  # Atributo protegido

    @property
    def carga(self):
        return self._carga

    def consumir(self, porcentaje):
        self._carga = max(0, self._carga - porcentaje)  # nunca baja de 0
        print(f"  -> Batería de {self.capacidad_wh} Wh al {self._carga}%.")

    def cargar(self):
        self._carga = 100
        print(f"  -> Batería de {self.capacidad_wh} Wh cargada al 100%.")


# --- Clase base (Avance 1 + Encapsulamiento + Composición) ---
class Laptop:
    def __init__(self, marca, modelo, GBRAM, procesador, bateria, encendida=False):
        self.marca = marca
        self.modelo = modelo
        self.__GBRAM = 0           # Atributo privado (Encapsulamiento)
        self.GBRAM = GBRAM         # Pasa por el setter para validar
        self.encendida = encendida
        # Composición: una Laptop "tiene-un" Procesador y "tiene-una" Bateria
        self.procesador = procesador
        self.bateria = bateria

    # Getter y setter con @property para la RAM
    @property
    def GBRAM(self):
        return self.__GBRAM

    @GBRAM.setter
    def GBRAM(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError("La RAM debe ser un número entero mayor que 0.")
        self.__GBRAM = valor

    def encender(self):
        if not self.encendida:
            self.encendida = True
            print(f"La laptop {self.marca} {self.modelo} se encendió.")
            self.procesador.iniciar()  # Delegación al componente
        else:
            print(f"La laptop {self.marca} {self.modelo} ya está prendida.")

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print(f"La laptop {self.marca} {self.modelo} se apagó.")
        else:
            print(f"La laptop {self.marca} {self.modelo} ya está apagada.")

    def aumentar_ram(self, extra):
        self.GBRAM = self.GBRAM + extra  # Usa el setter (valida)
        print(f"Se le agregaron {extra}GB de RAM a la {self.marca}. "
              f"Ahora tiene {self.GBRAM}GB.")

    def usar(self, porcentaje):
        print(f"La laptop {self.marca} {self.modelo} está en uso.")
        self.bateria.consumir(porcentaje)  # Delegación al componente

    def ver_info(self):
        print(f"Laptop: {self.marca} {self.modelo} | RAM: {self.GBRAM}GB | "
              f"Encendida: {self.encendida} | CPU: {self.procesador.info()} | "
              f"Batería: {self.bateria.carga}%")


# --- Subclase (Herencia) ---
class LaptopGamer(Laptop):
    def __init__(self, marca, modelo, GBRAM, procesador, bateria,
                 tarjeta_grafica, tasa_refresco_hz, encendida=False, modo_turbo=False):
        # Uso de super() para reutilizar el constructor de la clase base
        super().__init__(marca, modelo, GBRAM, procesador, bateria, encendida)
        self.tarjeta_grafica = tarjeta_grafica
        self.tasa_refresco_hz = tasa_refresco_hz
        self._modo_turbo = modo_turbo  # Atributo protegido

    # Método propio de la subclase
    def activar_turbo(self):
        self._modo_turbo = True
        print(f"¡TURBO ACTIVADO en {self.marca} {self.modelo}! "
              f"{self.tarjeta_grafica} a {self.tasa_refresco_hz} Hz.")

    # Sobrescritura (Polimorfismo): con turbo gasta el doble de batería
    def usar(self, porcentaje):
        if self._modo_turbo:
            porcentaje *= 2
        print(f"La laptop gamer {self.marca} {self.modelo} está en uso.")
        self.bateria.consumir(porcentaje)

    # Sobrescritura (Polimorfismo): añade datos propios de la subclase
    def ver_info(self):
        turbo = "ON" if self._modo_turbo else "OFF"
        print(f"Laptop Gamer: {self.marca} {self.modelo} | RAM: {self.GBRAM}GB | "
              f"Encendida: {self.encendida} | CPU: {self.procesador.info()} | "
              f"GPU: {self.tarjeta_grafica} | {self.tasa_refresco_hz} Hz | "
              f"Turbo: {turbo} | Batería: {self.bateria.carga}%")
