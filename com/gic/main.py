from car import Car

def get_user_input(prompt):
    while True:
        try:
            user_input = input(prompt)
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def validate_direction(direction):
    return direction in ['N', 'S', 'E', 'W']

def validate_position(x, y, field_width, field_height):
    return 0 <= x < field_width and 0 <= y < field_height

def run_simulation(cars, field_width, field_height):
    collision_detected = False
    collision_point = None
    collision_step = None

    for step in range(max(len(car.commands) for car in cars)):
        for car in cars:
            if not collision_detected:
                car.update_position(field_width, field_height)

                for other_car in cars:
                    if car != other_car and car.x == other_car.x and car.y == other_car.y:
                        collision_detected = True
                        collision_point = (car.x, car.y)
                        collision_step = step + 1
                        car.update_collision(collision_detected, collision_point, collision_step, other_car.name)
                        other_car.update_collision(collision_detected, collision_point, collision_step, car.name)
                        break

    return collision_detected, collision_point, collision_step

def print_car_info(cars):
    print("Your current list of cars are:")
    for car in cars:
        print(f"- {car.initial_settings['name']}, ({car.initial_settings['x']},{car.initial_settings['y']}) {car.initial_settings['direction']}, {car.initial_settings['commands']}")

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
                print_car_info(cars)
            elif choice == '2':
                if cars:
                    collision_detected, collision_point, collision_step = run_simulation(cars, field_width, field_height)
                    print_car_info(cars)
                    if collision_detected:
                        print(f"After simulation, the result is:")
                        for car in cars:
                            if car.collision_detected:
                                print(f"- {car.name}, collides with {car.collision_car_name} at {collision_point} at step {collision_step}")
                    else:
                        print(f"After simulation, the result is:")
                        for car in cars:
                            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
                else:
                    print("Please add at least one car to the field.")
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