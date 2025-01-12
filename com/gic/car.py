class Car:
    # Initializes a new Car object.
    def __init__(self, name, x, y, direction, commands):
        self.name = name #The name of the car.
        self.x = x #(int): The x-coordinate of the car's position on the field.
        self.y = y #(int): The y-coordinate of the car's position on the field.
        # Validate direction before assigning
        if direction not in ['N', 'S', 'E', 'W']:
            raise ValueError("Invalid direction. Direction must be N, S, E, or W.")
        self.direction = direction #(str): The direction the car is facing ('N', 'S', 'E', or 'W').
        self.commands = commands  # (str): A string of commands for the car to execute ('F' for forward, 'L' for left turn, 'R' for right turn).
        self.current_command_index = 0 #(int): The index of the current command in the commands string.
        # (dict): A dictionary containing the car's initial settings (name, x, y, direction, commands).
        self.initial_settings = {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "direction": self.direction,
            "commands": self.commands,
        }
        self.collision_detected = False # (bool): A flag indicating whether the car has collided with another car.
        self.collision_point = None # (tuple): A tuple representing the collision point (x, y) if a collision occurs.
        self.collision_step = -1 #  (int): The step at which the collision occurred.
        self.collision_car_name = None #(str): The name of the car that the current car collided with (if any).

    #Updates the car's position based on the next command and checks for boundary conditions.
    def update_position(self, field_width, field_height):
        if self.current_command_index < len(self.commands):
            command = self.commands[self.current_command_index]
            if command == 'F':
                if self.direction == 'N' and self.y < field_height - 1:
                    self.y += 1
                elif self.direction == 'S' and self.y > 0:
                    self.y -= 1
                elif self.direction == 'E' and self.x < field_width - 1:
                    self.x += 1
                elif self.direction == 'W' and self.x > 0:
                    self.x -= 1
            elif command == 'L':
                if self.direction == 'N':
                    self.direction = 'W'
                elif self.direction == 'S':
                    self.direction = 'E'
                elif self.direction == 'E':
                    self.direction = 'N'
                elif self.direction == 'W':
                    self.direction = 'S'
            elif command == 'R':
                if self.direction == 'N':
                    self.direction = 'E'
                elif self.direction == 'S':
                    self.direction = 'W'
                elif self.direction == 'E':
                    self.direction = 'S'
                elif self.direction == 'W':
                    self.direction = 'N'
            self.current_command_index += 1

    # Updates the collision information for the car.
    def update_collision(self, collision_detected, collision_point, collision_step, collision_car_name):
        self.collision_detected = collision_detected
        self.collision_point = collision_point
        self.collision_step = collision_step
        self.collision_car_name = collision_car_name
