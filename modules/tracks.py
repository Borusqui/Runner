class Tracks:
    def __init__(self, name, distance, track_category, max_participants):
        self.name = name
        self.distance = distance
        self.variability = self.get_variability()
        self.track_category = track_category
        self.participants = []
        self.max_participants = max_participants

    def add_participant(self, runner, base_time):
        """Adds a participant with their generated finish time."""
        print(f"[DEBUG] {runner.name} - Base Time: {base_time}, Variability: {self.variability}")
        finish_time = runner.generate_finish_time(base_time, self.variability)
        self.participants.append((runner.name, finish_time))

    def rank_participants(self):
        """Ranks participants based on their finish time"""
        self.participants.sort(key=lambda x: x[1])
        ranked_participants = [(rank + 1, p[0], round(p[1],2)) for rank, p in enumerate(self.participants)]
        return ranked_participants
    
    def get_variability(self):
        """Determine variability based on the track distance."""
        if self.distance <= 5:
            return 5
        elif self.distance <= 10:
            return 10
        elif self.distance <= 21.0975:
            return 15
        elif self.distance <= 42.195:
            return 20
        else:
            return 30

    def distribute_prize_money(self, x, alpha=2):
        """Distributes the prize money based on the ranking"""
        ranked_participants = self.rank_participants()
        y = len(ranked_participants)
        
        # Define weights for the top three positions
        W_1 = alpha**3  # First place
        W_2 = alpha**2  # Second place
        W_3 = alpha     # Third place
        W_others = 1    # For all other positions
        
        # Calculate total weight
        W_total = W_1 + W_2 + W_3 + (y - 3) * W_others
        
        # Calculate prize money for each position
        prize_distribution = {}
        prize_distribution[1] = x * W_1 / W_total
        prize_distribution[2] = x * W_2 / W_total
        prize_distribution[3] = x * W_3 / W_total
        
        for k in range(4, y + 1):
            prize_distribution[k] = x * W_others / W_total
        
        # Distribute prize money to participants based on their rank
        distributed_prizes = []
        for rank, name, time in ranked_participants:
            prize = prize_distribution.get(rank, 0)
            distributed_prizes.append((rank, name, time, round(prize, 2)))
        
        return distributed_prizes



