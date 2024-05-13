import pyautogui
import logging

# Acessa o logger configurado
logger = logging.getLogger('osrs_logger')

class OSRS:
  def __init__():
    pass

  def find_position(self, confidence=0.8):
    """Encontra a posição do objeto na tela."""
    location = pyautogui.locateOnScreen(self.image_path, confidence)
    if location:
      logger.info(f"Objeto {self.id} encontrado em {location}")
      return pyautogui.center(location)
    logger.info(f"Objeto {self.id} não foi encontrado...")
    return None

  def click(self, speed=0):
    """Move o mouse até o objeto e clica."""
    position = self.find_position()
    if position:
      pyautogui.moveTo(position, duration=speed)
      pyautogui.click()
      logger.info(f"Clique realizado em: {position}")
      return True
    else:
      logger.info(f"Objeto {self.id} não encontrado na tela.")
      return False

class OSRSInterface(OSRS):
  def __init__(self):
    self.inventory = OSRSObject("osrs_interface/inventory.png", "inventory")
    self.worn_equipment = OSRSObject("osrs_interface/worn_equipment.png", "worn_equipment")

class OSRSObject(OSRS):
  def __init__(self, image_path, identificador : str='sem_nome'):
    self.image_path = image_path
    self.id = identificador

    logger.info(f"Criado objeto {self.id}!")  
    
  def click_in_inventory(self, game_interface : OSRSInterface):
    logger.info(f"Clicando no botão da mochila para garantir que esteja aberta")  
    game_interface.inventory.click()
    logger.info(f"Clicando no objeto {self.id}")  
    self.click()
    
  def check_inventory(self, game_interface : OSRSInterface):
    game_interface.inventory.click()
    return self.find_position()
  
  def check_worn_equipment(self, game_interface : OSRSInterface):
    logger.info(f"Clicando no botão do equipamento para garantir que esteja aberto")  
    game_interface.worn_equipment.click()
    return self.find_position()

