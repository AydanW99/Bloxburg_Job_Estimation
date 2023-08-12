

class PointsNeeded():
    def __init__(self):
        self.current_level = 0
        self.current_points_needed = 11
        self.previous_level = 0
        self.new_points_needed = 0
        self.total_points = 0
        self.average_time = 0
        self.highest_level = 0

    def user_stats(self):
        """This is where the user imports their stats in order for the formula to calculate"""
        self.current_level = int(input("What is your current level? "))
        self.highest_level = int(input("What level do you want to reach? "))
        for _ in range(1, self.current_level):
            self.new_points_needed = self.current_points_needed + self.previous_level * 2 + 1
            self.current_points_needed = self.new_points_needed
            self.previous_level += 1
        user_input_time = input("What is the average minutes to reach 50 points, "
                                      "leave empty to use standard value of 12? ")
        if int(user_input_time) > 0:
            self.average_time = int(user_input_time)
        else:
            self.average_time = 12
        self.formula()

    def formula(self):
        for _ in range(self.current_level, self.highest_level):
            self.new_points_needed = self.current_points_needed + self.previous_level * 2 + 1
            self.total_points += self.new_points_needed
            self.current_points_needed = self.new_points_needed
            self.previous_level += 1

        average_1 = self.average_time / 50

        time_required = average_1 * self.total_points

        print(f"\nYou have {self.total_points} points left to obtain")
        print(f"From your current level it will take you {round(time_required)} mins to get to Level 50 \n"
              f"which is {round(time_required / 60)} hours")
