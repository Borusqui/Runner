class Tracks:
    def __init__(self, name, distance, category, max_participants):
        self.name = name
        self.distance = distance
        self.category = category
        self.participants = []
        self.max_participants = max_participants

    def add_participant(self, runner, base_time, variability):
        """Adds a participant with their generated finish time."""
        finish_time = runner.generate_finish_time(base_time, variability)
        self.participants.append((runner.name, finish_time))

    def rank_participants(self):
        """Ranks participants based on their finish time"""
        self.participants.sort(key=lambda x: x[1])
        ranked_participants = [(rank + 1, p[0], p[1]) for rank, p in enumerate(self.participants)]
        return ranked_participants
    


def print_ranking(track):
    """Prints the ranking of participants for a given track"""
    ranked_participants = track.rank_participants()
    print(f"Ranking for {track.name}: ")
    for rank, name, time in ranked_participants:
        print(f"Rank {rank}: {name}, Finish Time: {time} minutes")

    

#varName = lenght KM, baseTime in minutes
race_base_times = {
    "five_k": {"distance": 5.0, "base_time": 25}, 
    "ten_k": {"distance": 10.0, "base_time": 50},
    "fifteen_k": {"distance": 15.0, "base_time": 75},
    "half_marathon": {"distance": 21.0975, "base_time": 105},
    "marathon": {"distance": 42.195, "base_time": 200},
    "ultra_run": {"distance": 50.0, "base_time": 300}
}

marathon_info = race_base_times["marathon"]
five_k_info = race_base_times["five_k"]
ten_k_info = race_base_times["ten_k"]
fiften_k_info = race_base_times["fifteen_k"]
half_marathon_info = race_base_times["half_marathon"]
ultra_run_info = race_base_times["ultra_run"]


track1 = Tracks("Boston Marathon", marathon_info["distance"], 3, 20)
track2 = Tracks("Copenhagen Marathon", marathon_info["distance"], 3, 20)
track3 = Tracks("Around the lake", five_k_info["distance"], 1, 10)

print(f"Track 3: {track3.name}, {track3.distance} km, Category: {track3.category}")

# runners = [
#     Runner("Alice", 0.1, 0.1, 0.1, 0.1),
#     Runner("Bob", 0.9, 0.9, 0.9, 0.9),
#     Runner("Charlie", 0.6, 0.7, 0.9, 0.8),
#     Runner("David", 0.85, 0.75, 0.8, 0.9),
#     Runner("Eve", 0.95, 0.9, 0.9, 0.85),
#     Runner("Frank", 0.5, 0.6, 0.7, 0.5)
# ]

# base_time = marathon_info["base_time"]
# base_time = five_k_info["base_time"]

# variability = 7.5

# for runner in runners:
#     track3.add_participant(runner, base_time, variability)

# print_ranking(track3)'
