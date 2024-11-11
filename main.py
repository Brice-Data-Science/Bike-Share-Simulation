"""Main.py: Bike Share Simulation."""


# import matplotlib.pyplot as plt
# import pandas as pd
import random
# from datetime import datetime, timedelta


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

    def __repr__(self):
        """
        Returns a string representation of the Bikeshare object.

        Returns
        -------
        str
            A string displaying the number of bikes at each location.
        """
        return f'Bikeshare(olin={self.olin}, wellesley={self.wellesley})'

    def main(self):
        """The instance to start the simulation."""
        self.simulation()

    def move_bikes(self, from_location, to_location, number):
        """
        Moves a specified number of bikes from one location to another, if
        available.

        Parameters
        ----------
        from_location : str
            The location from which bikes will be moved
            (e.g., 'olin' or 'wellesley').
        to_location : str
            The location to which bikes will be moved
            (e.g., 'olin' or 'wellesley').
        number : int
            The number of bikes to move.

        Returns
        -------
        None
        """
        if getattr(self, from_location) >= number:
            setattr(self, from_location, getattr(self, from_location) - number)
            setattr(self, to_location, getattr(self, to_location) + number)
            print(f'Moved {number} bikes from {from_location} to '
                  f'{to_location}.')
        else:
            print(f'Not enough bikes available at {from_location}to move '
                  f'{number} bikes.')

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

    def random_move(self):
        """
        Picks a random number and moves a bike depending on the numbe generated.
        """

        number = random.random()
        if number < 0.35:
            print(f"Number: {number:.2f}")
            result = self.bike_to_olin()

        elif number < 0.80:
            print(f"Number: {number:.2f}")
            result = self.bike_to_wellesley()

        else:
            print(f"Number: {number:.2f}")
            print("No bikes were shared.")
            result = "No bikes were shared"

        print(f"Random number: {number:.2f}, Action: {result}")  # Debug print
        return result

    def simulation(self):
        """Run simulation of business operations."""
        number = random.randint(40, 151)

        for num in range(1, number):
            self.random_move()

# Create an instance
if __name__ == "__main__":
    bikeshare = BikeShare(olin=8, wellesley=4)
    bikeshare.main()
