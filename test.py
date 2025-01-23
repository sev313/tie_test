import unittest
from actuator.actuator import Actuator


class TestActuator(unittest.TestCase):

    def setUp(self):


        #Initialize the Actuator 
        self.actuator = Actuator(0)




    def test_initialize_state(self):
        self.assertEqual(self.actuator.state, "Uninitialized")


    def test_get_position_value_not_in_table(self):
        self.actuator.SetCurrent(1)
        self.assertEqual(self.actuator.GetPosition(), 0.942073306627607)
        self.assertEqual(self.actuator.state, "Operational")

    def test_set_current_within_limits(self):
        self.actuator.SetCurrent(1.01576130816775)
        self.assertEqual(self.actuator.GetPosition(), 1.00637670257657)
        self.assertEqual(self.actuator.state, "Operational")

    def test_set_current_outside_limits(self):
        self.actuator.SetCurrent(self.actuator.upperLimit+1)
        self.assertEqual(self.actuator.state, "Error")        

    def test_set_current_negative(self):
        self.actuator.SetCurrent(-1)
        self.assertEqual(self.actuator.state, "Error")   

    def test_get_state(self):
        self.assertEqual(self.actuator.GetState(), "Uninitialized")
        self.actuator.SetCurrent(0.3)
        self.assertEqual(self.actuator.GetState(), "Operational")
        self.actuator.SetCurrent(self.actuator.upperLimit+1)
        self.assertEqual(self.actuator.GetState(), "Error")

    def test_no_response_in_error_state(self):

        self.actuator.SetCurrent(self.actuator.upperLimit+1)
        self.assertEqual(self.actuator.GetState(), "Error")
        self.actuator.SetCurrent(1)
        self.assertEqual(self.actuator.GetPosition(), None)
        

if __name__ == '__main__':
    unittest.main()
