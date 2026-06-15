def play_games():
    secret=67
    tries=0
    while True:
        guess=int(input("Guess the number:"))
        if guess>secret:
            print("Too high")
            tries=tries+1
        elif guess<secret:
            print("Too high")
            tries=tries+1
        else:
            print("Correct you got it in",tries,"tries")
            break
play_games()
