import random

class Player:
    def __init__(self) -> None:
        self.current_choice = ''
        self.points = 0

    def set_choice():
        pass

    def clear_choice(self):
        self.current_choice = ''

class HumanPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def set_choice(self):
        while self.current_choice not in ['r','p','s']:
            try:
                self.current_choice = input("Rock, Paper, or Scissors [r,p,s]? ")
            except:
                pass

class ComputerPlayer(Player):
    def __init__(self) -> None:
        super().__init__()

    def set_choice(self):
        self.current_choice = random.choice(['r','p','s'])


class Game:

    def __init__(self) -> None:

        self.__setup()
    
    def  __setup(self) -> None:
        self.rounds = 0
        self.scores = {
            ('r','r'): None,
            ('p','p'): None,
            ('s','s'): None,
            ('r', 'p'): 'Lose',
            ('r','s'): 'Win',
            ('p','r'): 'Win',
            ('p', 's'): 'Lose',
            ('s', 'r'): 'Lose',
            ('s', 'p'): 'Win'
        }

        
        print('--- Rock Paper Scissors Game ---')
        while self.rounds == 0:
            try:
                self.rounds = int(input('How many rounds would you like to play? '))
            except ValueError:
                pass

        self.human_player = HumanPlayer()
        self.computer_player = ComputerPlayer()
    
    def __score(self) -> None:
        result = self.scores[(self.human_player.current_choice, self.computer_player.current_choice)]

        print('You:',self.human_player.current_choice,'|','Computer:',self.computer_player.current_choice)

        match(result):
            case 'Win':
                self.human_player.points += 1
                print('You won this round!')
            case 'Lose':
                self.computer_player.points += 1
                print('You lost this round!')
            case _:
                print('This round is a tie!')
        
        self.human_player.clear_choice()
        self.computer_player.clear_choice()

    def play(self) -> None:

        while self.rounds > 0:

            self.human_player.set_choice()
            self.computer_player.set_choice()

            self.__score()

            self.rounds -= 1

        else:
            print('[Game Summary]', 'Your Points:', self.human_player.points,'|','Computer Points:', self.computer_player.points)

            if self.human_player.points > self.computer_player.points:
                print('You won!')
            elif self.human_player.points < self.computer_player.points:
                print('Computer won!')
            else:
                print('It was a tie.')
if __name__ == '__main__':
    game = Game()
    game.play()
        


# Todo 
# handle multiple players with names
# 3 rounds minimum
