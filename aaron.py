from bots.base import Bot

class Aaron:

    def __init__(self, mode='default', wait=1):
        self.mode = mode
        Bot.wait = wait
        self.bots = []
        self.session ={}
    
    def add(self, bot_class, run_type='once'):
        bot = bot_class(run_type, self.session)
        self.bots.append(bot)

    def _prompt(self, s):
        print(s)
        print()
    
    def run(self):
        self._prompt("This is Aaron dialog system. Let's talk.")

        if self.mode == 'list':
            self._run_list_mode()
        else:
            self._run_default_mode()
    
    def _run_default_mode(self):
        for bot in self.bots:
            bot.run()
    
    def _run_list_mode(self):
        for index, bot in enumerate(self.bots):
            print(f"{index + 1}. {type(bot).__name__}")
        
        bot_index = 0
        bot_count = len(self.bots)
        input_prompt = f"Enter a number to choose your friend (1-{bot_count}): "
        while True:
            try:
                bot_index = int(input(input_prompt))
            except ValueError:
                print(f"Not a valid number. Please retry.")
                continue

            if bot_index < 1 or bot_index > bot_count:
                print(f"You can only choose between 1-{bot_count}")
                continue
            else:
                break
        
        bot = self.bots[bot_index - 1]
        bot.run()

if __name__ == '__main__':
    from bots.hello_bot import *
    from bots.greeting_bot import *
    from bots.favorite_color_bot import *
    from bots.calc_bot import *

    aaron = Aaron()
    aaron.add(HelloBot)
    aaron.add(GreetingBot)
    aaron.add(FavoriteColorBot)
    aaron.add(CalcBot, 'loop')
    aaron.run()

    aaron = Aaron(mode='list')
    aaron.add(HelloBot)
    aaron.add(GreetingBot)
    aaron.add(FavoriteColorBot)
    aaron.add(CalcBot)
    aaron.run()

