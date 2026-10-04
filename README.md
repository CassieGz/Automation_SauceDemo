# Proyecto de Automatización de Pruebas - Pre-Entrega

Este proyecto contiene un conjunto de pruebas automatizadas utilizando **Python**, **Selenium WebDriver** y **Pytest** para validar el flujo de inicio de sesión y la interfaz de inventario en la plataforma **SauceLabs (Swag Labs)**.

## Requisitos Previos

Antes de ejecutar las pruebas, asegúrate de tener instalado:

- **Python 3.12** o superior
- Navegador **Google Chrome** actualizado

## Configuración del Entorno

Para evitar conflictos de permisos o dependencias globales, el proyecto utiliza un entorno virtual aislado (`venv`).
Pasos para configurarlo en **PowerShell**:

1. **Clonar o abrir la carpeta del proyecto** en tu terminal.
2. **Crear el entorno virtual** (si no está creado):
   ```powershell
   python -m venv venv
   ```
3. **Activar el entorno virtual**:
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   _(Nota: el prefijo `(venv)` aparecerá al inicio de la línea de comandos en la terminal)._
4. **Instalar las dependencias requeridas**:
   ```powershell
   pip install pytest pytest-html selenium
   ```

## Ejecución de las Pruebas

Para correr todas las pruebas del proyecto de forma simultánea, simplemente ejecuta el siguiente comando en la terminal con el entorno activo:

```powershell
pytest
```

### Reporte de Resultados

El proyecto está configurado mediante el archivo `pytest.ini` para generar un reporte visual interactivo de manera automática tras cada ejecución.

Al finalizar los tests, encontrarás un archivo llamado **`reporte.html`** dentro de la carpeta `reports/`. Este reporte incluye:

- Estado final de cada caso de prueba (Passed/Failed).
- Tiempos de ejecución detallados.
- Configuración del sistema y metadata del entorno.

## Estructura del Proyecto

```text
pre_entrega/
│
├── venv/                  # Entorno virtual con librerías aisladas
├── tests/                 # Carpeta con los scripts de prueba
│   ├── test_login.py      # Casos de prueba para el flujo de autenticación
│   └── test_inventory.py  # Casos de prueba para la vista de
productos
│   └── test_cart.py  # Casos de prueba para el flujo del carrito
│
├── reports/               # Reportes HTML generados automáticamente
│   └── reporte.html
│
├── pytest.ini             # Configuración global y argumentos de Pytest
└── README.md              # Documentación del proyecto (este archivo)
```
