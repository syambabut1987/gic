
class Simulation:
    @staticmethod
    def print_car_info(cars):  #Prints information about the cars in the simulation.
        print("Your current list of cars are:")
        for car in cars:
            print(
                f"- {car.initial_settings['name']}, ({car.initial_settings['x']},{car.initial_settings['y']}) {car.initial_settings['direction']}, {car.initial_settings['commands']}")

    @staticmethod
    def process_simulation(cars, field_width,field_height):  #Runs the simulation for the given cars, field dimensions, and prints the results.
        if cars:
            collision_detected, collision_point, collision_step = Simulation.run_simulation(cars, field_width, field_height)
            Simulation.print_car_info(cars)
            if collision_detected:
                print(f"After simulation, the result is:")
                for car in cars:
                    if car.collision_detected:
                        print(
                            f"- {car.name}, collides with {car.collision_car_name} at {collision_point} at step {collision_step}")
            else:
                print(f"After simulation, the result is:")
                for car in cars:
                    print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
        else:
            print("Please add at least one car to the field.")


    @staticmethod
    def run_simulation(cars, field_width, field_height):  #Executes the core simulation logic, detecting collisions and updating car positions.
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