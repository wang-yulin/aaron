from bots.base import Bot
from simpleeval import simple_eval

class CalcBot(Bot):
    def _q(self):
        s = "Input some expression"
        if self.runtype == 'loop':
            s += " (type x, q, exit or quit to quit)"
        return s
    
    def _think(self, s):
        try:
            result = f"Done. Result = {simple_eval(s)}"
        except:
            result = "Sorry I can't understand"

        return result


if __name__ == '__main__':
    c = CalcBot()
    c.run()

    c = CalcBot('loop')
    c.run()