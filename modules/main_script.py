from tracks import Tracks
from runner import Runner
import config

def print_ranking(track):
    """Prints the ranking of participants for a given track"""
    ranked_participants = track.rank_participants()
    print(f"Ranking for {track.name}: ")
    for rank, name, time in ranked_participants:
        print(f"Rank {rank}: {name}, Finish Time: {time} minutes")

def main():
    # Initialize tracks
    track1 = Tracks("Boston Marathon", config.marathon_info["distance"], 3, 20)
    track2 = Tracks("Copenhagen Marathon", config.marathon_info["distance"], 3, 20)
    track3 = Tracks("Around the lake", config.five_k_info["distance"], 1, 10)

    alice = Runner("Alice", 0.1, 0.1, 0.1, 0.1)
                    #fitness, form, recovery, knowledge

    # Generate other runners with lower skills for comparison
    runners = Runner.generate_runners(track_category=0.2, num_runners=20)

    # Add Alice to the track
    track3.add_participant(alice, config.marathon_info["base_time"])

    # Add other runners to the track
    for runner in runners:
        track3.add_participant(runner, config.marathon_info["base_time"])

    # Print the ranking
    print_ranking(track3)

if __name__ == "__main__":
    main()