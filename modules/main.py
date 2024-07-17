from tracks import Tracks
from runner import Runner
import config


def race_track():
    """
    # Instantiate track
    track_name = Tracks("name", config.race_info["distance"])
    # Generate runners
    runners = Runner.generate_runners(track_category=3.0, num_runners=5)    
    # participant player
    track3.add_participant(player, config.marathon_info["base_time"])
    # participant competitors
    for runner in runners:
        track3.add_participant(runner, config.marathon_info["base_time"])
    # if prize money add prize money
    prize_money = config.marathon_info["prize_money"] # Total prize money
    # dristribut prize money if any prize money
    distributed_prizes = track3.distribute_prize_money(prize_money)
    if name == player.name:
        player.gold += prize
    # if necessary print
    for rank, name, time, prize in distributed_prizes:
        print(f"Rank {rank}: {name}, Time: {time}, Prize: ${prize}")
    """
def main_loop():
    while True:
        print("Menu:")
        print("1. Compete") #Go to next tourney
        print("2. Train") #What to train? fitness, knowledge
        print("3. Rest") #Just rest. But missing tourney or training
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            option_1()
        elif choice == '2':
            option_2()
        elif choice == '3':
            option_3()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

def option_1():
    pass

def option_2():
    pass

def option_3():
    pass


def main():
    main_loop()
    # Initialize tracks
    track1 = Tracks("Boston Marathon", config.marathon_info["distance"], 3, 20)
    track2 = Tracks("Copenhagen Marathon", config.marathon_info["distance"], 3, 20)
    track3 = Tracks("Around the lake", config.five_k_info["distance"], 1, 10)

    player = Runner("Alice", 0.3, 0.3, 0.3, 0.3)
                    #fitness, form, recovery, knowledge

    # Generate other runners with lower skills for comparison
    runners = Runner.generate_runners(track_category=3.0, num_runners=5)

    # Add Alice to the track
    track3.add_participant(player, config.marathon_info["base_time"])

    # Add other runners to the track
    for runner in runners:
        track3.add_participant(runner, config.marathon_info["base_time"])
 
    prize_money = config.marathon_info["prize_money"] # Total prize money

    distributed_prizes = track3.distribute_prize_money(prize_money)

    for rank, name, time, prize in distributed_prizes:
        print(f"Rank {rank}: {name}, Time: {time}, Prize: ${prize}")
        if name == player.name:
            player.gold += prize
    
    print("$",player.gold)

if __name__ == "__main__":
    main()