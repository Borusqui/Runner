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
        self.gold = 0

    @classmethod
    def generate_runners(cls, track_category, num_runners):
        """Generate runners for a race based on track category."""
        runners = []
        base_skill = 0.1
        max_skill_adjustment = 0.1 + (track_category * 0.05)  # Smaller increment per category

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
        # Calculate performance factor based on runner's attributes
        performance_factor = (self.fitness + self.form + self.recovery + self.knowledge) / 4
        print(f"[DEBUG] {self.name} - Performance Factor: {performance_factor}")
        
        # Apply performance factor to the base time
        time_adjustment = base_time * performance_factor
        print(f"[DEBUG] {self.name} - Time Adjustment: {time_adjustment}")
        
        # Introduce variability to simulate race conditions
        random_variability = random.uniform(-variability, variability)
        print(f"[DEBUG] {self.name} - Random Variability: {random_variability}")
        
        finish_time = base_time - time_adjustment + random_variability
        finish_time = round(finish_time, 2)
        print(f"[DEBUG] {self.name} - Finish Time: {finish_time}")
        
        return finish_time
    
    # def generate_finish_time(self, base_time, variability):
    #     """Generates a finish time based on the runner's skills."""
    #     # Calculate a performance factor based on the runner's skills
    #     performance_factor = (self.fitness + self.form + self.recovery + self.knowledge) / 4

    #     # The better the performance factor, the lower the finish time
    #     mean_time = base_time / performance_factor
    #     std_dev_time = mean_time * variability
    #     return round(random.normalvariate(mean_time, std_dev_time), 2)

    
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
    
    def train_fitness(self):
        print("Training fitness...")
        # self.fatigue += x
        # self.fitness += y

    def train_knowledge(self):
        print("Training Knowledge...")
        # self.knowledge += x

    def rest(self):
        print("Resting...")
        # self.recovery += y
        # self.fatigue -= x
