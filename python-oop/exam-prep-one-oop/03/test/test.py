from project.climbing_robot import ClimbingRobot
from unittest import TestCase, main


class TestClimbingRobot(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot('Mountain', 'leg', 1200, 20)

    def test_initialise_method(self):
        self.assertEqual(self.robot.category, 'Mountain')
        self.assertEqual(self.robot.part_type, 'leg')
        self.assertEqual(self.robot.capacity, 1200)
        self.assertEqual(self.robot.memory, 20)

    def test_with_invalid_category(self):
        with self.assertRaises(ValueError) as ex:
            robot = ClimbingRobot('Car', 'leg', 1200, 20)
        self.assertEqual(str(ex.exception), "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']")

    def test_get_used_capacity(self):
        self.assertEqual(self.robot.get_used_capacity(), 0)

        first_software = {
            "name": 123321,
            "capacity_consumption": 500,
            "memory_consumption": 10
        }
        second_software = {
            "name": 11,
            "capacity_consumption": 600,
            "memory_consumption": 10
        }

        self.robot.install_software(first_software)
        self.robot.install_software(second_software)

        self.assertEqual(self.robot.get_used_capacity(), 1100)

    def test_get_available_capacity(self):
        self.assertEqual(self.robot.get_available_capacity(), 1200)

        first_software = {
            "name": 123321,
            "capacity_consumption": 500,
            "memory_consumption": 10
        }
        second_software = {
            "name": 11,
            "capacity_consumption": 600,
            "memory_consumption": 10
        }

        self.robot.install_software(first_software)
        self.robot.install_software(second_software)

        self.assertEqual(self.robot.get_available_capacity(), 100)

    def test_get_used_memory(self):
        # try with more elements in array
        self.assertEqual(self.robot.get_used_memory(), 0)
        first_software = {
            "name": 123321,
            "capacity_consumption": 500,
            "memory_consumption": 10
        }
        second_software = {
            "name": 11,
            "capacity_consumption": 600,
            "memory_consumption": 10
        }

        self.robot.install_software(first_software)
        self.robot.install_software(second_software)

        self.assertEqual(self.robot.get_used_memory(), 20)

    def test_get_available_memory(self):
        self.assertEqual(self.robot.get_available_memory(), 20)

        first_software = {
            "name": 123321,
            "capacity_consumption": 500,
            "memory_consumption": 10
        }
        second_software = {
            "name": 11,
            "capacity_consumption": 600,
            "memory_consumption": 10
        }

        self.robot.install_software(first_software)
        self.robot.install_software(second_software)

        self.assertEqual(self.robot.get_available_memory(), 0)

    def test_install_software(self):
        ok_software = {
            "name": 123321,
            "capacity_consumption": 500,
            "memory_consumption": 10
        }

        # install software successfully
        self.assertEqual(self.robot.install_software(ok_software),
                         "Software '123321' successfully installed on Mountain part.")
        self.assertIn(ok_software, self.robot.installed_software)

    def test_install_software_too_much_capacity(self):
        not_enough_capacity_soft = {
            "name": 1111,
            "capacity_consumption": 1500,
            "memory_consumption": 10
        }
        self.assertEqual(self.robot.install_software(not_enough_capacity_soft),
                         "Software '1111' cannot be installed on Mountain part.")
        self.assertNotIn(not_enough_capacity_soft, self.robot.installed_software)

    def test_install_software_too_much_memory(self):
        not_enough_memory_soft = {
            "name": 222,
            "capacity_consumption": 1000,
            "memory_consumption": 30
        }
        self.assertEqual(self.robot.install_software(not_enough_memory_soft),
                         "Software '222' cannot be installed on Mountain part.")
        self.assertNotIn(not_enough_memory_soft, self.robot.installed_software)

    def test_install_storage(self):
        first_software = {
            "name": 11,
            "capacity_consumption": 1000,
            "memory_consumption": 15
        }
        second_software = {
            "name": 2,
            "capacity_consumption": 600,
            "memory_consumption": 10
        }
        self.assertEqual(self.robot.install_software(first_software),
                         "Software '11' successfully installed on Mountain part.")
        self.assertIn(first_software, self.robot.installed_software)
        self.assertEqual(self.robot.install_software(second_software),
                         "Software '2' cannot be installed on Mountain part.")
        self.assertNotIn(second_software, self.robot.installed_software)


if __name__ == '__main__':
    main()
