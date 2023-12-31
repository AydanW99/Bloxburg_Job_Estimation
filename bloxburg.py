DEFAULT_VALUE = 15

class Bloxburg():
    def __init__(self):
        self.current_level = 0
        self.current_points_needed = 11
        self.previous_level = 0
        self.new_points_needed = 0
        self.total_points = 0
        self.average_time = 0
        self.highest_level = 0
        self.current_progress = 0

    def enter_stats(self):
        """This is where the user imports their stats in order for the formula to calculate"""
        self.current_level = int(input("What is your current level? "))
        self.highest_level = int(input("What level do you want to reach? "))
        self.current_progress = int(input(f"What is your current progress at level {self.current_level} (put 0 if unsure)? "))
        for _ in range(1, self.current_level):
            self.new_points_needed = self.current_points_needed + self.previous_level * 2 + 1
            self.current_points_needed = self.new_points_needed
            self.previous_level += 1
        user_input_time = input("What is the average minutes to reach 50 points, "
                                      "leave empty to use standard value of 15? ")
        if int(user_input_time) > 0:
            self.average_time = int(user_input_time)
        else:
            self.average_time = DEFAULT_VALUE
        self.time_required()

    def time_required(self):
        for _ in range(self.current_level, self.highest_level):
            self.new_points_needed = self.current_points_needed + self.previous_level * 2 + 1
            self.total_points += self.new_points_needed
            self.current_points_needed = self.new_points_needed
            self.previous_level += 1

        self.total_points -= self.current_progress
        average_1 = self.average_time / 50

        time_required = average_1 * self.total_points

        print(f"\nYou have {self.total_points} points left to obtain")
        print(f"From your current level it will take you {round(time_required)} mins to get to Level 50 \n"
              f"which is {round(time_required / 60)} hours")
