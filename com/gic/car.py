class Car:
    def __init__(self, name, x, y, direction, commands):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = commands
        self.current_command_index = 0
        self.initial_settings = {
            "name": self.name,
            "x": self.x,
            "y": self.y,
            "direction": self.direction,
            "commands": self.commands,
        }
        self.collision_detected = False
        self.collision_point = None
        self.collision_step = -1
        self.collision_car_name = None

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

    def update_collision(self, collision_detected, collision_point, collision_step, collision_car_name):
        self.collision_detected = collision_detected
        self.collision_point = collision_point
        self.collision_step = collision_step
        self.collision_car_name = collision_car_name
