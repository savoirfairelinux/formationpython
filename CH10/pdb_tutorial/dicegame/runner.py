from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.roll()
        self.reset()

    def roll(self):
        self.dice = Die.create_dice(5)

    def reset(self):
        self.round = 0
        self.wins = 0
        self.loses = 0
        self.consequtive_wins = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(self):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        # c = 0
        runner = self()
        while True:
            runner.roll()
            runner.round += 1
            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = 0
            while guess == 0:
                print ('Cheat:', runner.answer())
                guess = input("Sigh. What is your guess?: ")
                try:
                    guess = int(guess)
                except:
                    guess = 0
                finally:
                    if guess == 0:
                        print ('Enter a valid guess...')

            # import ipdb; ipdb.set_trace()

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                runner.wins += 1
                runner.consequtive_wins += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                runner.loses += 1
                runner.consequtive_wins = 0
            print("Wins: {}, Consequtive {}, Loses {}".format(runner.wins, runner.consequtive_wins, runner.loses))

            # import ipdb; ipdb.set_trace()

            if runner.consequtive_wins == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt.lower() != 'n':
                continue
            else:
                break
            #    i_just_throw_an_exception()
