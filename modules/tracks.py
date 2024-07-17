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
