# Gic Auto Drive Simulation
Auto Drive - GIC Self Drive Simulation : 

# Auto Driving Car Simulation

This project simulates the movement of autonomous cars on a rectangular grid-based field. 

**Features**

* Simulate car movement based on a set of commands (forward, left turn, right turn).
* Define individual cars with properties like name, initial position, direction, and command sets.
* Execute car movements and update positions accordingly.
* Detect collisions between cars during simulation and track collision details.
* Provide clear output on car positions and any collisions that occurred.
* Validate user input for field dimensions, car positions, and directions.
* Offer an interactive command-line interface for user interaction.
* Include unit tests to ensure the core logic's correctness.

**Getting Started**

1. **Prerequisites:**
   - Python installed on your system (https://www.python.org/downloads/)

2. **Running the Simulation:**
   - Clone or download the project files.
   - Open a terminal or command prompt and navigate to the project directory.
   - Run the simulation script: <python installation directory path>\python3 .\gic_auto_drive\com\gic\main.py  

3. **User Interaction:**
   - Follow the on-screen prompts to:
      - Define the width and height of the simulation field.
      - Add cars with their names, initial positions, directions, and command sets.
      - Run the simulation.
   - The program will display the final state of the cars, including their positions and any collisions that occurred.

**Project Structure**

gic_auto_drive/
├── com.gic.car.py             # Car class definition
├── com.gic.simulation.py      # Simulation logic and helper functions
├── com.gic.main.py      # Simulation logic and helper functions
├── com.gic.unittest.autodrivetest.py # Unit test cases
└── README.md          # This file


**High Level Main test scenarios**

## Scenario 1
Test Simulation for 1 Cars (input vs expected output)

Welcome to Auto Driving Car Simulation!
Please enter the width and height of the simulation field in 'x y' format: 10 10
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 1
Please enter the name of the car: A
Please enter initial position of car A in 'x y Direction' format: 1 2 N
Please enter the commands for car A: FFRFFFFRRL
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 2
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
After simulation, the result is:
- A, (5,4) S
Please choose from the following options:
[1] Start over
[2] Exit
Enter your choice: 2
Thank you for running the simulation. Goodbye!

## Scenario 2
Test Multi Car Simulation with 2 Cars (input vs expected output)

Welcome to Auto Driving Car Simulation!
Please enter the width and height of the simulation field in 'x y' format: 10 10
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 1
Please enter the name of the car: A
Please enter initial position of car A in 'x y Direction' format: 1 2 N
Please enter the commands for car A: FFRFFFFRRL
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 1
Please enter the name of the car: B
Please enter initial position of car B in 'x y Direction' format: 7 8 W
Please enter the commands for car B: FFLFFFFFFF
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
- B, (7,8) W, FFLFFFFFFF
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 2
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
- B, (7,8) W, FFLFFFFFFF
After simulation, the result is:
- A, collides with B at (5, 4) at step 7
- B, collides with A at (5, 4) at step 7
Please choose from the following options:
[1] Start over
[2] Exit
Enter your choice: 2
Thank you for running the simulation. Goodbye!


## Scenario 3
Test Multi Car Simulation with 3 Cars (input vs expected output)

Welcome to Auto Driving Car Simulation!
Please enter the width and height of the simulation field in 'x y' format: 10 10
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 1
Please enter the name of the car: A
Please enter initial position of car A in 'x y Direction' format: 1 2 N
Please enter the commands for car A: FFRFFFFRRL
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 1
Please enter the name of the car: B
Please enter initial position of car B in 'x y Direction' format: 7 8 W
Please enter the commands for car B: FFLFFFFFFF
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
- B, (7,8) W, FFLFFFFFFF
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 1
Please enter the name of the car: C
Please enter initial position of car C in 'x y Direction' format: 6 8 W
Please enter the commands for car C: FLFFFFFFF
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
- B, (7,8) W, FFLFFFFFFF
- C, (6,8) W, FLFFFFFFF
You have created a field of 10 x 10.
Please choose from the following options:
[1] Add a car to field
[2] Run simulation
Enter your choice: 2
Your current list of cars are:
- A, (1,2) N, FFRFFFFRRL
- B, (7,8) W, FFLFFFFFFF
- C, (6,8) W, FLFFFFFFF
After simulation, the result is:
- B, collides with C at (6, 8) at step 1
- C, collides with B at (6, 8) at step 1
Please choose from the following options:
[1] Start over
[2] Exit
Enter your choice: 2
Thank you for running the simulation. Goodbye!


