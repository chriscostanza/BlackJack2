def player_name_input():
    
    while True:
        playername = str(input("Please enter your name: "))
        return playername
    
    
def betting(player,computer):
    
    
    while True:
        try:
            print(f"CURRENT HOLDINGS: {player.bank}")
            computer.bank
            bet = int(input("How much would you like to wager?: "))
            if bet > player.bank:
                print("Insufficient Funds!")
            elif bet > computer.bank:
                print(f"Computer only has {computer.bank}. Wager less!")
            else:
                return bet
            

        except:
            print("That's not a valid number!")
            
def bankrupt_check(player,computer):
    
    global bankrupt
    
    if player.bank == 0:
        bankrupt = True
        print(f"{player.name} is bankrupt! {computer.name} wins!")
    elif computer.bank == 0:
        bankrupt = True
        print(f"{computer.name} is bankrupt! {player.name} wins!")
        return 
    else:
        bankrupt = False
        

def bust_check(player):
    
    return player.hand_value() > 21

    
def display_table(player,computer,bet):
    
    print("\n"*100)
    computer.computer_hand_display()
    print("")
    print("--------------------\n")
    print(f"--CURRENT POT: {bet*2}--")
    print("")
    print("--------------------\n")
    player.player_hand_display()
    print(f"Total Value: {player.hand_value()}")
    print("")
    
def display_table_end(player,computer):

    
    print("\n"*100)
    computer.player_hand_display()
    print("")
    print("--------------------")
    print("--CURRENT POT: 0 --")
    print("--------------------")
    print("")
    player.player_hand_display()
    print("")
