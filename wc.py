#Cortar arvore
#requisitos
#1 faca na mochila
#1 machado na mão

#execução
#caminho feliz
#1.Clica na árvore
#2.Aguarda a mochila encher
#3.Clica na faca
#4.Clica na madeira
#5.Clica na opção "arrow shafts"
#6.Espera esvaziar a mochila
import logging_config
from osrs import OSRSObject, OSRSInterface
from time import sleep

logging_config.setup_logging()

def check_requirements():
  
  pass

def main():
  yew_log = OSRSObject("osrs_objects/yew_log.png", "yew log")
  knife = OSRSObject("osrs_objects/knife.png", "knife")
  rune_axe = OSRSObject("osrs_objects/rune_axe.png", "rune axe")

  game_interface = OSRSInterface()
  # Confere se ta com a faca e o machado na mão
  if not (knife.check_inventory(game_interface) and\
    rune_axe.check_worn_equipment(game_interface)):
    return
  
  while True:
    pass


main()