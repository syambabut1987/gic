from car import Car
from simulation import Simulation

def get_user_input(prompt):   #Prompts the user for input and validates it as an integer.
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def validate_direction(direction):  #Checks if the provided direction is valid ('N', 'S', 'E', or 'W').
    return direction in ['N', 'S', 'E', 'W']

def validate_position(x, y, field_width, field_height):  #Checks if the given position is within the field boundaries.
    return 0 <= x < field_width and 0 <= y < field_height



#The entry point of the program, running the simulation loop and handling user interaction.
def main():
    print("Welcome to Auto Driving Car Simulation!")

    while True:
        field_width, field_height = map(int, get_user_input("Please enter the width and height of the simulation field in 'x y' format: ").split())

        cars = []

        while True:
            print(f"You have created a field of {field_width} x {field_height}.")
            print("Please choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            choice = get_user_input("Enter your choice: ")

            if choice == '1':
                car_name = get_user_input("Please enter the name of the car: ")
                while True:
                    x, y, direction = get_user_input("Please enter initial position of car {} in 'x y Direction' format: ".format(car_name)).split()
                    x, y = int(x), int(y)
                    if validate_position(x, y, field_width, field_height) and validate_direction(direction):
                        break
                    else:
                        print("Invalid input. Please try again.")
                commands = get_user_input("Please enter the commands for car {}: ".format(car_name))
                cars.append(Car(car_name, x, y, direction, commands))
                Simulation.print_car_info(cars)
            elif choice == '2':
                Simulation.process_simulation(cars, field_width,field_height)
                break
            else:
                print("Invalid choice. Please try again.")

        print("Please choose from the following options:")
        print("[1] Start over")
        print("[2] Exit")
        choice = get_user_input("Enter your choice: ")
        if choice == '1':
            continue
        elif choice == '2':
            print("Thank you for running the simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Exiting.")
            break

if __name__ == "__main__":
    main()