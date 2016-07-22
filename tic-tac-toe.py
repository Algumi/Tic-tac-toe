from random import randint


class Game(object):
    def __init__(self, game_mod, board_size, complexity):
        self.game_mod = game_mod
        self.board_size = board_size
        self.complexity = complexity
    board = []
    turn = 0  # the current turn of the game
    bot_turn = "O"
    player_turn = "X"

    def generate_board(self):  # creating the board(size depends on the options) of the game
        for i in range(self.board_size * self.board_size):
            self.board.append("#")

    def clean_board(self):  # refreshes the variables of our class for the new game
        for i in range(self.board_size * self.board_size):
            self.board[i] = "#"
        self.turn = 0

    def print_board(self):
        letter = unichr(97)  # unichr(97) == "a"
        print " ",
        for x in range(self.board_size):  # prints the top part of the board
            print x,
        print
        for i in range(self.board_size):
            print letter,
            for j in range(self.board_size):
                print self.board[i * 3 + j],
            print
            letter = unichr(ord(letter.lower()) + 1)  # needed for going through the letters(a, b, c...)

    def read_turn(self):  # reads the coordinates of player's move
            print "It's your turn!"
            self.print_board()
            print ">> please, enter the coordinates of your turn:"
            x = int(raw_input("X: "))
            while x < 0 or x > self.board_size:  # checks if players move is correct
                print "there is no such coordinate, enter the correct number: "
                x = int(raw_input("X: "))
            y = transform_letter(raw_input("Y: "))
            while y < 0 or y > self.board_size:  # checks if players move is correct
                print "there is no such coordinate, enter the correct number: "
                y = int(raw_input("Y: "))
            coord = x + y * self.board_size
            if self.board[coord] != "#":
                print "this cell is not empty, try again"
                return -1
            return coord

    def random_move(self):  # generates random move of the bot
        coord = randint(0, self.board_size * self.board_size - 1)
        while self.board[coord] != "#":  # checks if the cell is empty
            coord = randint(0, self.board_size * self.board_size - 1)
        self.board[coord] = self.bot_turn

    def random_des(self):  # ~desu-desu (it decides if we randomize move or not)
        random = randint(0, 100)
        if random > self.complexity:
            self.random_move()
            return True
        else:
            return False

    def check_for_danger_3(self):  # checks if we have two similar figures in a row(if we can lose or win)
        win_ans = [1]  # the list of our win moves
        lose_ans = [2]  # the list of our losing moves
        no_ans = [-1]  # needed to avoid problems with return data, when we have no dangerous situations
        win_case = 0  # needed to decide, what we'll return at the end
        lose_case = 0
        if self.board[0] == "#":  # a lot of checks, but I didn't find a better solution of this problem
            if self.board[3] == self.board[6] and self.board[3] != "#":
                if self.board[3] == self.bot_turn:
                    win_case = 1
                    win_ans.append(0)
                else:
                    lose_case = 1
                    lose_ans.append(0)
            if self.board[1] == self.board[2] and self.board[1] != "#":
                if self.board[1] == self.bot_turn:
                    win_case = 1
                    win_ans.append(0)
                else:
                    lose_case = 1
                    lose_ans.append(0)
            if self.board[4] == self.board[8] and self.board[4] != "#":
                if self.board[4] == self.bot_turn:
                    win_case = 1
                    win_ans.append(0)
                else:
                    lose_case = 1
                    lose_ans.append(0)
        if self.board[1] == "#":
            if self.board[0] == self.board[2] and self.board[0] != "#":
                if self.board[0] == self.bot_turn:
                    win_case = 1
                    win_ans.append(1)
                else:
                    lose_case = 1
                    lose_ans.append(1)
            if self.board[4] == self.board[7] and self.board[4] != "#":
                if self.board[4] == self.bot_turn:
                    win_case = 1
                    win_ans.append(1)
                else:
                    lose_case = 1
                    lose_ans.append(1)
        if self.board[2] == "#":
            if self.board[0] == self.board[1] and self.board[0] != "#":
                if self.board[0] == self.bot_turn:
                    win_case = 1
                    win_ans.append(2)
                else:
                    lose_case = 1
                    lose_ans.append(2)
            if self.board[5] == self.board[8] and self.board[5] != "#":
                if self.board[5] == self.bot_turn:
                    win_case = 1
                    win_ans.append(2)
                else:
                    lose_case = 1
                    lose_ans.append(2)
            if self.board[4] == self.board[6] and self.board[4] != "#":
                if self.board[4] == self.bot_turn:
                    win_case = 1
                    win_ans.append(2)
                else:
                    lose_case = 1
                    lose_ans.append(2)
        if self.board[3] == "#":
            if self.board[4] == self.board[5] and self.board[4] != "#":
                if self.board[4] == self.bot_turn:
                    win_case = 1
                    win_ans.append(3)
                else:
                    lose_case = 1
                    lose_ans.append(3)
            if self.board[0] == self.board[6] and self.board[0] != "#":
                if self.board[0] == self.bot_turn:
                    win_case = 1
                    win_ans.append(3)
                else:
                    lose_case = 1
                    lose_ans.append(3)
        if self.board[4] == "#":
            if self.board[0] == self.board[8] and self.board[0] != "#":
                if self.board[0] == self.bot_turn:
                    win_case = 1
                    win_ans.append(4)
                else:
                    lose_case = 1
                    lose_ans.append(4)
            if self.board[3] == self.board[5] and self.board[3] != "#":
                if self.board[3] == self.bot_turn:
                    win_case = 1
                    win_ans.append(4)
                else:
                    lose_case = 1
                    lose_ans.append(4)
            if self.board[6] == self.board[2] and self.board[6] != "#":
                if self.board[6] == self.bot_turn:
                    win_case = 1
                    win_ans.append(4)
                else:
                    lose_case = 1
                    lose_ans.append(4)
            if self.board[1] == self.board[7] and self.board[1] != "#":
                if self.board[1] == self.bot_turn:
                    win_case = 1
                    win_ans.append(4)
                else:
                    lose_case = 1
                    lose_ans.append(4)
        if self.board[5] == "#":
            if self.board[3] == self.board[4] and self.board[3] != "#":
                if self.board[3] == self.bot_turn:
                    win_case = 1
                    win_ans.append(5)
                else:
                    lose_case = 1
                    lose_ans.append(5)
            if self.board[2] == self.board[8] and self.board[2] != "#":
                if self.board[2] == self.bot_turn:
                    win_case = 1
                    win_ans.append(5)
                else:
                    lose_case = 1
                    lose_ans.append(5)
        if self.board[6] == "#":
            if self.board[0] == self.board[3] and self.board[0] != "#":
                if self.board[0] == self.bot_turn:
                    win_case = 1
                    win_ans.append(6)
                else:
                    lose_case = 1
                    lose_ans.append(6)
            if self.board[4] == self.board[2] and self.board[4] != "#":
                if self.board[4] == self.bot_turn:
                    win_case = 1
                    win_ans.append(6)
                else:
                    lose_case = 1
                    lose_ans.append(6)
            if self.board[7] == self.board[8] and self.board[7] != "#":
                if self.board[7] == self.bot_turn:
                    win_case = 1
                    win_ans.append(6)
                else:
                    lose_case = 1
                    lose_ans.append(6)
        if self.board[7] == "#":
            if self.board[6] == self.board[8] and self.board[6] != "#":
                if self.board[6] == self.bot_turn:
                    win_case = 1
                    win_ans.append(7)
                else:
                    lose_case = 1
                    lose_ans.append(7)
            if self.board[1] == self.board[4] and self.board[1] != "#":
                if self.board[1] == self.bot_turn:
                    win_case = 1
                    win_ans.append(7)
                else:
                    lose_case = 1
                    lose_ans.append(7)
        if self.board[8] == "#":
            if self.board[0] == self.board[4] and self.board[0] != "#":
                if self.board[0] == self.bot_turn:
                    win_case = 1
                    win_ans.append(8)
                else:
                    lose_case = 1
                    lose_ans.append(8)
            if self.board[6] == self.board[7] and self.board[6] != "#":
                if self.board[6] == self.bot_turn:
                    win_case = 1
                    win_ans.append(8)
                else:
                    lose_case = 1
                    lose_ans.append(8)
            if self.board[2] == self.board[5] and self.board[2] != "#":
                if self.board[2] == self.bot_turn:
                    win_case = 1
                    win_ans.append(8)
                else:
                    lose_case = 1
                    lose_ans.append(8)
        if win_case == 1:
            return win_ans
        if lose_case == 1:
            return lose_ans
        return no_ans

    def check_win_3(self):  # checks if we have 3 figures in a row, I tried to make it beautiful, but got fuckup
        if self.board[0] == self.board[1] and self.board[0] == self.board[2]:
            if self.board[0] == self.bot_turn:
                return 1  # bot wins
            if self.board[0] == self.player_turn:
                return 2  # player wins
        if self.board[0] == self.board[3] and self.board[0] == self.board[6]:
            if self.board[0] == self.bot_turn:
                return 1
            if self.board[0] == self.player_turn:
                return 2
        if self.board[0] == self.board[4] and self.board[0] == self.board[8]:
            if self.board[0] == self.bot_turn:
                return 1
            if self.board[0] == self.player_turn:
                return 2
        if self.board[1] == self.board[4] and self.board[1] == self.board[7]:
            if self.board[1] == self.bot_turn:
                return 1
            if self.board[1] == self.player_turn:
                return 2
        if self.board[2] == self.board[5] and self.board[2] == self.board[8]:
            if self.board[2] == self.bot_turn:
                return 1
            if self.board[2] == self.player_turn:
                return 2
        if self.board[3] == self.board[4] and self.board[3] == self.board[5]:
            if self.board[3] == self.bot_turn:
                return 1
            if self.board[3] == self.player_turn:
                return 2
        if self.board[6] == self.board[7] and self.board[6] == self.board[8]:
            if self.board[6] == self.bot_turn:
                return 1
            if self.board[6] == self.player_turn:
                return 2
        if self.board[6] == self.board[4] and self.board[6] == self.board[2]:
            if self.board[6] == self.bot_turn:
                return 1
            if self.board[6] == self.player_turn:
                return 2
        return -1

    def best_move_3(self):  # this method tries to find the best move and make analysis of the situation on the board
        best = [-1, 0]  # the first element is a coordinate of best move and the second is a value of this move
        for i in range(self.board_size * self.board_size):
            if self.board[i] == "#":
                self.board[i] = self.player_turn
                coord = self.check_for_danger_3()
                if coord[0] == 1:
                    if len(coord) > 2:
                        best[0] = i
                        best[1] = 10000  # to make a fork(of our figures on board)  - the most valuable move
                    if len(coord) == 2:
                        if best[1] < 100:  # to make one case of our win have less value
                            best[0] = i
                            best[1] = 100
                if coord[0] == 2:
                    if len(coord) > 2:
                        if best[1] < 1000:  # to prevent a fork on the player - second valued move
                            best[0] = i
                            best[1] = 1000
                    if len(coord) == 2:
                        if best[1] < 10:  # prevent one win case of player - not very important
                            best[0] = i  # but i think it makes the moves of the bot better
                            best[1] = 10
                self.board[i] = "#"
            if self.board[i] == "#":  # the same operations, but checks aggressive moves of the bot
                self.board[i] = self.bot_turn
                coord = self.check_for_danger_3()
                if coord[0] == 1:
                    if len(coord) > 2:
                        best[0] = i
                        best[1] = 10000
                    if len(coord) == 2:
                        if best[1] < 100:
                            best[0] = i
                            best[1] = 100
                if coord[0] == 2:
                    if len(coord) > 2:
                        if best[1] < 1000:
                            best[0] = i
                            best[1] = 1000
                    if len(coord) == 2:
                        if best[1] < 10:
                            best[0] = i
                            best[1] = 10
                self.board[i] = "#"
        return best[0]

    def generate_move_3(self):  # generates bot's move on board 3x3
        if not self.random_des():  # makes a mistake randomly(depends on complexity of the game)
            if self.turn == 0:
                self.board[4] = self.bot_turn  # most valuable move on the start
            else:
                if self.turn == 1:
                    if self.board[4] != "#":
                        unexp = randint(0, 3)
                        if unexp == 0:
                            self.board[0] = self.bot_turn
                        if unexp == 1:
                            self.board[2] = self.bot_turn
                        if unexp == 2:
                            self.board[6] = self.bot_turn
                        if unexp == 3:
                            self.board[8] = self.bot_turn
                    else:
                        self.board[4] = self.bot_turn
                if self.turn == 2:
                    if self.board[4] == "#":  # if we made a mistake on the first move
                        self.board[4] = self.bot_turn
                        return True
                    if self.board[1] == self.board[3] and self.board[5] == self.board[7]:  # fast check of changes
                        if self.board[0] == self.board[8]:
                            unexp = randint(0, 1)  # more random for the god of random
                            if unexp == 0:
                                self.board[0] = self.bot_turn
                            else:
                                self.board[8] = self.bot_turn
                        else:
                            unexp = randint(0, 1)
                            if unexp == 0:
                                self.board[2] = self.bot_turn
                            else:
                                self.board[6] = self.bot_turn
                    else:
                        unexp = randint(0, 8)  # makes the game of the bot more random
                        if self.board[1] != self.board[7]:
                            while unexp == 1 or unexp == 4 or unexp == 7:
                                unexp = randint(0, 8)
                            self.board[unexp] = self.bot_turn
                        else:
                            if self.board[3] != self.board[5]:
                                while unexp == 3 or unexp == 4 or unexp == 5:
                                    unexp = randint(0, 8)
                                self.board[unexp] = self.bot_turn
                if self.turn == 3:
                    if self.board[0] == self.board[8] != "#" or self.board[2] == self.board[6] != "#":
                        unexp = randint(0, 3)
                        if unexp == 0:
                            self.board[1] = self.bot_turn
                        if unexp == 1:
                            self.board[3] = self.bot_turn
                        if unexp == 2:
                            self.board[5] = self.bot_turn
                        if unexp == 3:
                            self.board[7] = self.bot_turn
                    else:
                        coord = self.check_for_danger_3()
                        if coord[0] != -1:
                            self.board[coord[1]] = self.bot_turn
                        else:
                            coord = self.best_move_3()
                            if coord != -1:
                                self.board[coord] = self.bot_turn
                            else:
                                self.random_move()
                if 3 < self.turn < 9:
                    coord = self.check_for_danger_3()
                    if coord[0] != -1:
                        self.board[coord[1]] = self.bot_turn
                    else:
                        coord = self.best_move_3()
                        if coord != -1:
                            self.board[coord] = self.bot_turn
                        else:
                            self.random_move()
        self.turn += 1

    def board_3_game(self):  # the main process of the game on board 3x3
        if self.game_mod == 2:  # initialize the figures of each player
            self.player_turn = "O"
            self.bot_turn = "X"
        if self.game_mod == 2:
            self.generate_move_3()
        while self.turn < 9:
            coord = self.read_turn()
            while coord == -1:
                coord = self.read_turn()
            self.board[coord] = self.player_turn
            if self.check_win_3() == 1:
                return 1
            if self.check_win_3() == 2:
                return 2
            self.turn += 1
            self.print_board()
            self.generate_move_3()
            if self.check_win_3() == 1:
                self.print_board()
                return 1
            if self.check_win_3() == 2:
                return 2
        return 0


def transform_letter(y):  # transform the letter to coordinate on the board
    result = ord(y) - 97
    return result


def start_game():  # greetings and initialization of settings
    game_mod = 1
    board_size = 3
    complexity = 100
    print "-----Welcome to the tic-tac-toe-----"
    print ">> would you like to change standard options of the game?"
    print "1 option - to play a standard game"
    print "2 option - to change the options"
    print ">> please enter 1 or 2 to make a choice: "
    pref = int(raw_input())
    while pref != 1 and pref != 2:
        print ">> please enter 1 or 2 to make a choice: "
        pref = int(raw_input())
    if pref == 2:
        print "1 option - your turn will be the first"
        print "2 option - your turn will be the second"
        print ">> enter 1 or 2 to choose your option: "
        game_mod = int(raw_input())
        while game_mod != 1 and game_mod != 2:
            print ">> please, enter 1 or 2 to make a choice: "
            game_mod = int(raw_input())
        print ">> please, enter the complexity of the game(you can choose 10%, 50%, 70% or 100%)"
        print ">> please, enter the number 10, 50, 70 or 100 to make a choice: "
        complexity = int(raw_input())
        while complexity != 10 and complexity != 50 and complexity != 70 and complexity != 100:
            print ">> please enter the correct number(10, 50, 70 or 100): "
            complexity = int(raw_input())
        # maybe some day, I'll make another board sizes, but not now :c
        # print ">> please, enter the size of the board(you can choose 3x3, 10x10 or 15x15 board size) "
        # print ">> enter the number 3, 10 or 15 to make a choice: "
        # board_size = int(raw_input())
        # while board_size != 3 and board_size != 10 and board_size != 15:
            # print ">> please enter the correct number(3, 10 or 15): "
            # board_size = int(raw_input())
    options = [game_mod, board_size, complexity]
    return options


def show_result(options):
    if options == 1:
        print "The loser is you!"
        print "Please, try to turn on your brain, the bot tired of your skill"
    if options == 2:
        print "The winner is you!"
        print "WOW, such a skill!"
    if options == 0:
        print "It's draw."
        print "You are not as bad, as i thought"


def end_game():  # check if the player want to play again
    print ">> would you like to play one more time?"
    print "1 option - play one more time"
    print "2 option - exit the game"
    print ">> please enter 1 or 2 to make a choice: "
    opt = int(raw_input())
    while opt != 1 and opt != 2:
        print ">> please enter 1 or 2 to make a choice: "
        opt = int(raw_input())
    if opt == 1:
        return 1
    else:
        return 2


def main():
    cont = 1
    while cont == 1:
        options = start_game()
        my_game = Game(options[0], options[1], options[2])
        my_game.generate_board()
        if my_game.board_size == 3:
            res = my_game.board_3_game()
            show_result(res)
        my_game.clean_board()
        cont = end_game()


main()
