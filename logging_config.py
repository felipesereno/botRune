import logging
import os

print("setup_logging")

def setup_logging():
  # Cria uma pasta para os logs, se não existir
  if not os.path.exists('logs'):
    os.makedirs('logs')

  # Cria um logger
  logger = logging.getLogger('osrs_logger')
  logger.setLevel(logging.DEBUG)  # Captura todos os níveis de logs

  # Formato dos logs
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

  # Handler para INFO e acima
  info_handler = logging.FileHandler('logs/info.log')
  info_handler.setLevel(logging.INFO)
  info_handler.setFormatter(formatter)

  # Handler para ERROR e acima
  error_handler = logging.FileHandler('logs/error.log')
  error_handler.setLevel(logging.ERROR)
  error_handler.setFormatter(formatter)

  # Handler para escrever logs na saída do console (DEBUG e acima)
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.DEBUG)
  console_handler.setFormatter(formatter)

  # Adiciona os handlers ao logger
  logger.addHandler(info_handler)
  logger.addHandler(error_handler)
  logger.addHandler(console_handler)  # Essa linha foi adicionada
