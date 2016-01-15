class Dice():
    pass

def main():
    while True:
        command = input('Enter a command: ')
        if command.lower() == 'q':
            print("Exiting...")
            break
        try:
            command1 = int(command[:-1])
        except ValueError:
            print('Try Again')
            main()
        if command[-1].lower() == 'a':
            print("Rolling %s Attack Die" %command[:-1])
        elif command[-1].lower() =='d':
            print("Rolling %s Defense Die" %command[:-1])
        else:
            print("Try Again!")
            main()

main()

