import logging
from logging.handlers import TimedRotatingFileHandler
import os

# Определяем имя файла для логов
log_file = os.path.join(os.path.dirname(__file__), 'app_log.txt')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Создание обработчика, который будет выводить логи в консоль
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Создание обработчика для файла с ротацией по времени
file_handler = TimedRotatingFileHandler(log_file, when='midnight', interval=1, backupCount=7)
file_handler.setLevel(logging.INFO)

# Создание форматтера
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# Добавление обработчиков к логгеру
logger.addHandler(console_handler)
logger.addHandler(file_handler)