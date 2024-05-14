import logging_config
from osrs import OSRSObject

# Configura o logger ao iniciar a aplicação
logging_config.setup_logging()

def main():
  potato_seed = OSRSObject("osrs_objects/potato_seed.png", "potato seed")
  chiesel = OSRSObject("osrs_objects/chiesel.png", "chiesel")
  hammer = OSRSObject("osrs_objects/hammer.png", "hammer")
  potato_seed.click()

if __name__ == "__main__":
  main()
