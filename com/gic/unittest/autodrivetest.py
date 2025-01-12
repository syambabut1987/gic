import unittest
from com.gic.car import Car
from com.gic.simulation import Simulation


class AutoDriveTest(unittest.TestCase):

    def test_one_car_simulation(self):
        field_width = 10
        field_height = 10
        car_name = "A"
        x = 1
        y = 2
        direction = "N"
        commands = "FFRFFFFRRL"
        cars = []
        cars.append(Car(car_name, x, y, direction, commands))
        Simulation.run_simulation(cars, field_width, field_height)
        self.assertFalse(cars[0].collision_detected)
        self.assertEqual(cars[0].name, "A")
        self.assertEqual(cars[0].x, 5)
        self.assertEqual(cars[0].y, 4)
        self.assertEqual(cars[0].direction, "S")


    def test_two_car_simulation(self):
        cars = []
        field_width = 10
        field_height = 10
        cars.append(Car("A", 1, 2, "N", "FFRFFFFRRL"))
        cars.append(Car("B", 7, 8, "W", "FFLFFFFFFF"))
        Simulation.run_simulation(cars, field_width, field_height)
        self.assertTrue(cars[0].collision_detected)
        self.assertEqual(cars[0].name, "A")
        self.assertEqual(cars[0].x, 5)
        self.assertEqual(cars[0].y, 4)
        self.assertEqual(cars[0].collision_step, 7)
        self.assertEqual(cars[0].collision_car_name, "B")

    def test_multi_cars_simulation(self):
        cars = []
        field_width = 10
        field_height = 10
        cars.append(Car("A", 1, 2, "N", "FFRFFFFRRL"))
        cars.append(Car("B", 7, 8, "W", "FFLFFFFFFF"))
        cars.append(Car("C", 6, 8, "W", "FLFFFFFFF"))
        Simulation.run_simulation(cars, field_width, field_height)
        self.assertTrue(cars[1].collision_detected)
        self.assertEqual(cars[1].name, "B")
        self.assertEqual(cars[1].x, 6)
        self.assertEqual(cars[1].y, 8)
        self.assertEqual(cars[1].collision_step, 1)
        self.assertEqual(cars[1].collision_car_name, "C")


    def test_init_valid_input(self):
        # Test creating a Car object with valid inputs
        car_name = "TestCar"
        x = 1
        y = 2
        direction = "N"
        commands = "FFR"
        car = Car(car_name, x, y, direction, commands)

        self.assertEqual(car.name, car_name)
        self.assertEqual(car.x, x)
        self.assertEqual(car.y, y)
        self.assertEqual(car.direction, direction)
        self.assertEqual(car.commands, commands)
        self.assertEqual(car.current_command_index, 0)
        self.assertEqual(car.initial_settings["name"], car_name)
        self.assertEqual(car.initial_settings["x"], x)
        self.assertEqual(car.initial_settings["y"], y)
        self.assertEqual(car.initial_settings["direction"], direction)
        self.assertEqual(car.initial_settings["commands"], commands)
        self.assertFalse(car.collision_detected)
        self.assertIsNone(car.collision_point)
        self.assertEqual(car.collision_step, -1)
        self.assertIsNone(car.collision_car_name)

    def test_init_invalid_direction(self):
        # Test creating a Car object with an invalid direction
        car_name = "TestCar"
        x = 1
        y = 2
        direction = "X"
        commands = "FFR"
        with self.assertRaises(ValueError):
            Car(car_name, x, y, direction, commands)

    def test_update_position_no_movement(self):
        # Test update_position when there are no movement commands
        car_name = "TestCar"
        x = 1
        y = 2
        direction = "N"
        commands = ""
        car = Car(car_name, x, y, direction, commands)
        car.update_position(5, 5)

        self.assertEqual(car.x, x)
        self.assertEqual(car.y, y)
        self.assertEqual(car.direction, direction)

    def test_update_position_move_north(self):
        # Test update_position with a move north command
        car_name = "TestCar"
        x = 1
        y = 2
        direction = "N"
        commands = "F"
        car = Car(car_name, x, y, direction, commands)
        car.update_position(5, 5)

        self.assertEqual(car.x, x)
        self.assertEqual(car.y, y + 1)
        self.assertEqual(car.direction, direction)

    def test_update_position_move_south(self):
        # Test update_position with a move south command
        car_name = "TestCar"
        x = 1
        y = 2
        direction = "S"
        commands = "F"
        car = Car(car_name, x, y, direction, commands)
        car.update_position(5, 5)

        self.assertEqual(car.x, x)
        self.assertEqual(car.y, y - 1)
        self.assertEqual(car.direction, direction)

    def test_update_position_move_east(self):
        # Test update_position with a move east command
        car_name = "TestCar"
        x = 1
        y = 2
        direction = "E"
        commands = "F"
        car = Car(car_name, x, y, direction, commands)
        car.update_position(5, 5)

        self.assertEqual(car.x, x + 1)
        self.assertEqual(car.y, y)
        self.assertEqual(car.direction, direction)

    def test_update_position_move_west(self):
        # Test update_position with a move west command
        car_name = "TestCar"
        x = 1
        y = 2
        direction = "W"
        commands = "F"
        car = Car(car_name, x, y, direction, commands)
        car.update_position(5, 5)

        self.assertEqual(car.x, x - 1)
        self.assertEqual(car.y, y)
        self.assertEqual(car.direction, direction)


if __name__ == '__main__':
    unittest.main()
