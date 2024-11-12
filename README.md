# Bike Share Simulation

A Python simulation for a bikeshare system that models daily bike movements between two locations, **Olin** and **Wellesley**, throughout the year. This simulation adjusts the behavior of bike movements based on seasonal variations, with more activity in the summer and reduced activity in the winter.

The simulation records daily data, including the number of bikes at each location and the actions taken each day, and outputs this data to a CSV file for further analysis.

## Table of Contents

- [Bike Share Simulation](#bike-share-simulation)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Parameters](#parameters)
  - [Output](#output)
  - [Project Structure](#project-structure)
  - [License](#license)

## Features

- Models a simple bikeshare system with two locations: Olin and Wellesley.
- Seasonal variation: winter and summer months impact the frequency of bike movements.
- Daily simulation for any specified time range.
- Outputs simulation results to a CSV file for data analysis.

## Installation

1. **Clone the Repository**:

   git clone https://github.com/your-username/bike-share-simulation.git
   cd bike-share-simulation

## Usage

1. **Define initial conditions**:

    if __name__ == "__main__":  
    bikeshare = BikeShare *(olin=8, wellesley=4)*  
    current_date = datetime(2023, 1, 1)  
    end_date = datetime(2024, 12, 31)  
    bikeshare.simulation(current_date, end_date)  

2. **Set Simulation Period**:

    if __name__ == "__main__":
    bikeshare = BikeShare(olin=8, wellesley=4)  
    current_date = datetime *(2023, 1, 1)*  
    end_date = datetime *(2024, 12, 31)*  
    bikeshare.simulation(current_date, end_date)  

3. **Run the Simulation**: Execute the main script to run the simulation and generate a CSV file with daily data.  

    iPython: %run main.py  
    bash: python main.py  

## Parameters

1. **olin**: Initial number of bikes at the Olin location
2. **wellesley**: Initial number of bikes at the Wellesley location
3. **current_date**: Start date for the simulation
4. **end_date**: End date for the simulation

## Output

1. The simulation generates a CSV file, bike_share_simulation.csv, saved in the data/ folder. Each row in the CSV contains:
    - Date: The date of the simulation day.
    - Olin Bikes: Number of bikes at Olin at the end of the day.
    - Wellesley Bikes: Number of bikes at Wellesley at the end of the day.
    - Action: Description of the action taken (e.g., moving bikes between locations).

    **Sample Output**  
    Date, 	    Olin Bikes, 	Wellesley Bikes, 	        Action  
    2023-01-01, 	    8, 	        4, 	            Moved 1 bike from Wellesley  
    2023-01-02, 	    7, 	        5, 	            No bikes were shared  
    2023-01-03, 	    6, 	        6, 	            Moved 1 bike from Olin to Wellesley  

## Project Structure

your-repository/  
│  
├── data/  
│   └── bike_share_simulation.csv,     Output CSV file with simulation data  
│  
├── Main.py,                           Main script to run the simulation  
│  
└── README.md,                         Project documentation  

## License

This project is licensed under the Apache License. See the LICENSE file for details.
