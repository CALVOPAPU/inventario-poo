# Sistema de inventario tecnológico (POO en Python)

Avance 3 Final: Composición y Módulos.

- `modelos.py`: clases `Procesador`, `Bateria`, `Laptop` y `LaptopGamer`.
- `main.py`: instanciación de objetos y pruebas.
- `assets/diagrama_uml.png`: diagrama UML.

Ejecutar: `python main.py`

## Diagrama UML

```mermaid
classDiagram
    class Procesador {
        +modelo
        +nucleos
        +frecuencia_ghz
        +iniciar()
        +info()
    }
    class Bateria {
        +capacidad_wh
        #_carga
        +carga()
        +consumir(porcentaje)
        +cargar()
    }
    class Laptop {
        +marca
        +modelo
        -__GBRAM
        +encendida
        +procesador
        +bateria
        +GBRAM()
        +encender()
        +apagar()
        +aumentar_ram(extra)
        +usar(porcentaje)
        +ver_info()
    }
    class LaptopGamer {
        +tarjeta_grafica
        +tasa_refresco_hz
        #_modo_turbo
        +activar_turbo()
        +usar(porcentaje)
        +ver_info()
    }
    Laptop <|-- LaptopGamer
    Laptop *-- Procesador
    Laptop *-- Bateria
```
