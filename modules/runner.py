import random
from tracks import Tracks

class Runner:
    def __init__(self, name, fitness, form, recovery, knowledge):
        self.name = name
        # self.age = age
        # self.gender = gender
        # self.country = country
        self.fitness = fitness # Cardiovascular endurance, strength, and flexibility. Regular training helps build stamina and prevents injuries.
        self.form = form # Correct running form reduces strain on joints and muscles.
        self.recovery = recovery # Adequate rest allows muscles to repair and prevents burnout.
        self.knowledge = knowledge # Choosing the right running shoes based on foot type and terrain is essential.
        self.current_injury = None
        self.personal_records = {}
        self.fatigue = 0

    @classmethod
    def generate_runners(cls, track_category_number, num_runners):
        """Generate runners for a race based on track category."""
        runners = []
        base_skill = 0.1
        max_skill_adjustment = 0.2 + (track_category_number * 0.05)  # Smaller increment per category

        for _ in range(num_runners):
            fitness = max(base_skill, min(1.0, random.uniform(base_skill, base_skill + max_skill_adjustment)))
            form = max(base_skill, min(0.9, random.uniform(base_skill, base_skill + max_skill_adjustment)))
            recovery = max(base_skill, min(0.9, random.uniform(base_skill, base_skill + max_skill_adjustment)))
            knowledge = max(base_skill, min(0.8, random.uniform(base_skill, base_skill + max_skill_adjustment)))

            # Generate runner name
            name = f"Runner {_ + 1}"

            # Create runner instance and add to list
            runner = cls(name, fitness, form, recovery, knowledge)
            runners.append(runner)

        return runners

    def generate_finish_time(self, base_time, variability):
        """Generates a finish time based on the runner's skills."""
        # Calculate a performance factor based on the runner's skills
        performance_factor = (self.fitness + self.form + self.recovery + self.knowledge) / 4

        # The better the performance factor, the lower the finish time
        mean_time = base_time / performance_factor
        std_dev_time = mean_time * variability
        return round(random.normalvariate(mean_time, std_dev_time), 2)
    
    def check_health(self):
        """Checks the runner's current health status."""
        if self.current_injury:
            print(f"{self.name} is currently injured: {self.current_injury}")
        else:
            print(f"{self.name} is without injuries and a fatigue level of {self.fatigue}")
            if self.fatigue > 75:
                print(f"{self.name} is suffering from serious fatigue. Take a break.")
            elif self.fatigue > 60:
                print(f"{self.name} is suffering from fatigue. Think about taking a break.")
            elif self.fatigue > 25:
                print(f"{self.name} is not suffering from fatigue yet. But be careful.")
            else:
                print(f"{self.name}'s is currently not fatigued.")
    
    def enter_race(self, track, base_time, variability):
        """Registers the runner for a race on a given track."""
        finish_time = self.generate_finish_time(base_time, variability)
        track.add_participant(self, finish_time, variability)        

    def train(self):
        print("Training...")


    def study(self):
        print("Studying...")

    def rest(self):
        print("Resting...")

def print_ranking(track):
    """Prints the ranking of participants for a given track"""
    ranked_participants = track.rank_participants()
    print(f"Ranking for {track.name}: ")
    for rank, name, time in ranked_participants:
        print(f"Rank {rank}: {name}, Finish Time: {time} minutes")

if __name__ == "__main__":
    alice = Runner("Alice", 0.42, 0.42, 0.45, 0.41)
                    #fitness, form, recovery, knowledge

    base_time = 200  # Base time for marathon in minutes
    variability = 0.1  # Variability in finish times
    marathon_track = Tracks("City Marathon", 42.195, 6, 20)
    alice.enter_race(marathon_track, base_time, variability)

    # Check health status
    alice.check_health()


    track_category_number = 1  # Example category number of the track
    num_runners = 50

    # Generate runners based on track category
    runners = Runner.generate_runners(track_category_number, num_runners)

    # Print out the generated runners' attributes (for demonstration)
    for runner in runners:
        print(f"Runner: {runner.name}, Fitness: {runner.fitness:.2f}, Form: {runner.form:.2f}, Recovery: {runner.recovery:.2f}, Knowledge: {runner.knowledge:.2f}")

    for runner in runners:
        marathon_track.add_participant(runner, base_time, variability)

    print_ranking(marathon_track)
