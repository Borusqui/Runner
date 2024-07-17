from tracks import Tracks
from runner import Runner
import config

def instantiate_run():
    runners = Runner.generate_runners(track_category=3.0, num_runners=10)
    track3.add_participant(alice, config.marathon_info["base_time"])

def main():
    # Initialize tracks
    track1 = Tracks("Boston Marathon", config.marathon_info["distance"], 3, 20)
    track2 = Tracks("Copenhagen Marathon", config.marathon_info["distance"], 3, 20)
    track3 = Tracks("Around the lake", config.five_k_info["distance"], 1, 10)

    alice = Runner("Alice", 0.3, 0.3, 0.3, 0.3)
                    #fitness, form, recovery, knowledge

    # Generate other runners with lower skills for comparison
    runners = Runner.generate_runners(track_category=3.0, num_runners=20)

    # Add Alice to the track
    track3.add_participant(alice, config.marathon_info["base_time"])

    # Add other runners to the track
    for runner in runners:
        track3.add_participant(runner, config.marathon_info["base_time"])
 

    prize_money = config.marathon_info["prize_money"] # Total prize money

    distributed_prizes = track3.distribute_prize_money(prize_money)

    for rank, name, time, prize in distributed_prizes:
        print(f"Rank {rank}: {name}, Time: {time}, Prize: ${prize}")

if __name__ == "__main__":
    main()