print('''
                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           |'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'|U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-|U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You approach the end of a hallway, you can go left or right. WHAT DO YOU CHOOSE? [Left | Right]: ")

if choice == "Left":
    choice = input("There is a sudden lake somehow appearing in front of you! Wait for a boat? [Yes | No]: ")
    if choice == "Yes":
        choice = input("YOU ARE NOW AT A DOOR!!!! WHICH ONE?! RED, BLUE, YELLOW!: ")
        if choice == "Yellow":
            print("YOU FOUND THE TREASURE!")
        else:
            print("YOU HAVE DIED IN THE MOST HORRIBLE OF WAYS!")
    else:
        print("SUCKS TO DIE NERD")
else:
    print("GAME OVER!!!! YOU ARE EATEN ALIVE!!!")