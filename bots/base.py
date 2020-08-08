import time
from termcolor import colored

class Bot:
    wait = 1

    def __init__(self, runtype='once', session=None):
        self.runtype = runtype
        self.session = session
    
    def _q(self):
        return ''
        
    def _think(self, s):
        return s

    def _format(self, s):
        return colored(s, 'blue')
    
    def _say(self, s):
        time.sleep(Bot.wait)
        print(self._format(s))

    def _run_once(self):
        a = input()
        self._say(self._think(a))
    
    def _run_loop(self):
        while True:
            a = input()
            if a.lower() in ['x', 'q', 'exit', 'quit']:
                    break
            self._say(self._think(a)) 
  
    def run(self):
        self._say(self._q())
        
        if self.runtype == 'once':
            self._run_once()
        elif self.runtype == 'loop':
            self._run_loop()