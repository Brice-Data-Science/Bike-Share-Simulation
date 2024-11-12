"""Main.py: Bike Share Simulation."""

import csv
import random
from datetime import datetime, timedelta


class BikeShare:
    """
    A class to represent a bikeshare system with multiple locations.

    Attributes
    ----------
    olin : int
        Number of bikes available at the Olin location.
    wellesley : int
        Number of bikes available at the Wellesley location.

    Methods
    -------
    move_bikes(from_location, to_location, number):
        Moves a specified number of bikes from one location to another if
        available.

    bike_to_wellesley():
        Moves one bike from Olin to Wellesley, if available, and prints the
        action and updated totals.

    bike_to_olin():
        Moves one bike from Wellesley to Olin, if available, and prints the
        action and updated totals.
    """


    def __init__(self, olin, wellesley):
        """
        Initializes the Bikeshare object with the number of bikes at each
        location.

        Parameters
        ----------
        olin : int
            Initial number of bikes at the Olin location.
        wellesley : int
            Initial number of bikes at the Wellesley location.
        """
        self.olin = olin
        self.wellesley = wellesley
        self.data = []  # Collects daily simulation data


    def __repr__(self):
        """
        Returns a string representation of the Bikeshare object.

        Returns
        -------
        str
            A string displaying the number of bikes at each location.
        """
        return f'Bikeshare(olin={self.olin}, wellesley={self.wellesley})'



    def bike_to_wellesley(self):
        """
        Moves one bike from Olin to Wellesley, if available.

        This method checks if there is at least one bike at Olin. If so, it moves
        one bike from Olin to Wellesley, prints the action, and then prints the 
        updated totals at each location. If there are no bikes at Olin, it 
        prints a message indicating the action cannot be completed.
        
        Returns
        -------
        None
        """
        if self.olin >= 1:
            self.olin -= 1
            self.wellesley += 1
            return "Moved 1 bike from Olin to Wellesley."
        else:
            return "Not enough bikes at Olin to move to Wellesley."

        # Print the updated totals
        print(f"Total bikes - Olin: {self.olin}, Wellesley: {self.wellesley}")


    def bike_to_olin(self):
        """
        Moves one bike from Wellesley to Olin, if available.

        This method checks if there is at least one bike at Wellesley. If so,
        it moves one bike from Wellesley to Olin, prints the action, and then
        prints the updated totals at each location. If there are no bikes at
        Wellesley, it prints a message indicating the action cannot be
        completed.
        
        Returns
        -------
        None
        """
        if self.wellesley >= 1:
            self.wellesley -= 1
            self.olin += 1
            return "Moved 1 bike from Wellesley to Olin."
        else:
            return "Not enough bikes at Wellesley to move to Olin."

        # Print the updated totals
        print(f"Total bikes = Olin: {self.olin}, Wellesley: {self.wellesley}")


    def random_move(self, is_winter):
        """
        Picks a random number and moves a bike depending on the numbe generated.
        """

        number = random.random()
        if is_winter:
            if number < 0.20:
                return self.bike_to_olin()
            elif number < 0.60:
                return self.bike_to_wellesley()
        else: # summer
            if number < 0.35:
                return self.bike_to_olin()

            elif number < 0.65:
                return self.bike_to_wellesley()

            elif number < 0.85:
                return self.bike_to_olin() * 2

            else:
                return self.bike_to_wellesley() * 2


    def simulation(self, start_date, simulation_end_date):
        """Run simulation of business operations."""
        sim_date = start_date
        while sim_date <= simulation_end_date:
            # Determine if it's winter or summer based on the month
            is_winter = sim_date.month in [11, 12, 1, 2]

            # Perform a bike-sharing action for the day
            action = self.random_move(is_winter)

            # Collect daily data
            self.data.append({
                "Date": sim_date.strftime('%Y-%m-%d'),
                "Olin Bikes": self.olin,
                "Wellesley Bikes": self.wellesley,
                "Action": action
            })

            # Move to the next day
            sim_date += timedelta(days=1)

        # Write data to CSV
        with open('data/bike_share_simulation.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Date", "Olin Bikes", "Wellesley Bikes", "Action"])
            writer.writeheader()
            writer.writerows(self.data)

# Create an instance
if __name__ == "__main__":
    # Set initial parameters for the number of bikes starting at each location
    bikeshare = BikeShare(olin=8, wellesley=4)
    # Enter start and end dates for simulation below
    current_date = datetime(2023, 1, 1)
    end_date = datetime(2024, 12, 31)
    bikeshare.simulation(current_date, end_date)
