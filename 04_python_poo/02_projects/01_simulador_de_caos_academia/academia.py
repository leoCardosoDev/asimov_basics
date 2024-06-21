import random

class Academia:
  def __init__(self):
    self.halteres = [i for i in range(10,36) if i % 2 == 0]
    self.porta_halteres = {}
    self.reiniciar_o_dia()
  
  def reiniciar_o_dia(self):
    self.porta_halteres = {i: i for i in self.halteres}
  
