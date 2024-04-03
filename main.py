
from ps9pr4 import *


def main():
    print("Play Against:\n 1.AIplayer\n 2.Random Computer Player\n 3.Second Player")
    while True:
        try:
            col = int(input("Pick Game Mode: \n"))
        except ValueError:
            print("Not a number\n")
            continue
        if 0< col < 4 :
            if col==1:
                try:
                    difficulty = int(input("Enter difficulty(0 to 5): \n"))
                except ValueError:
                    print("Not a number\n")
                    continue
                if difficulty<0 or difficulty>5:
                    print("Invalid option.\n")
                    continue
                connect_four(Player('X'),AIPlayer('O','LEFT',difficulty))
            elif col==2:
                connect_four(Player('X'),RandomPlayer('O'))
            elif col==3:
                connect_four(Player('X'),Player('O'))

        else: 
            print("Invalid option.\n")
            print("")

main()