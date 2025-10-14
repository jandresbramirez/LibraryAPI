import logging

# Configuración básica del formato de logs
LOG_FORMAT = "%(asctime)s - %(levelname)s - [%(name)s] - %(message)s"

# Configura el logging global
logging.basicConfig(
    level=logging.INFO,              # Nivel mínimo de log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format=LOG_FORMAT,               # Formato de salida
    datefmt="%Y-%m-%d %H:%M:%S",     # Formato de fecha
)

# Obtén el logger principal
logger = logging.getLogger("LibraryAPI")

# Ejemplo: para desactivar logs de librerías externas ruidosas
logging.getLogger("werkzeug").setLevel(logging.WARNING)
logging.getLogger("sqlalchemy").setLevel(logging.WARNING)