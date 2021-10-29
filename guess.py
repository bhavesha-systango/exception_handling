from random import randrange

def main():
    number = randrange(100)
    while True:
        try:
            guess = int(input("enter no. ?"))
        except ValueError:
            print("valueerror")
        if guess == number:
            print("you win")
            break

if __name__ == "__main__":
    main()