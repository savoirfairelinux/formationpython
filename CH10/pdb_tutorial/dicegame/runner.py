import sys

from .die import Die
from .utils import i_just_throw_an_exception


class GameRunner:
    round = 1
    wins = 0
    loses = 0

    def __init__(self):
        self.dice = Die.create_dice(5)
        # self.reset()

    # def reset(self):
    #     self.round = 1
    #     self.wins = 0
    #     self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        while True:
            runner = cls()

            print("Round {}\n".format(runner.round))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                GameRunner.wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                GameRunner.loses += 1
                c = 0
            print("Wins: {} Loses {}".format(runner.wins, runner.loses))
            GameRunner.round += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = input("Would you like to play again?[Y/n]: ")

            if prompt in ['y', 'Y'] or prompt == '':
                continue
            elif prompt in ['n', 'N']:
                sys.exit()
            else:
                i_just_throw_an_exception()
