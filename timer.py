from threading import Timer

class Controle:
   def __init__(self):
       self.morreu = False
   def acabou(self):
       self.morreu = True
   def main(self):
       while not self.morreu:
           print raw_input('Digite algo:')

controle = Controle()
t = Timer(10.0, Controle.acabou, [ controle ])
t.start()
controle.main()
