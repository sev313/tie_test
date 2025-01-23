# Actuator Simulation

Create a class that models this actuator with at least the following methods:

- Initialize
*Prepare the actuator for operation.
- SetCurrent
*Set the actuator current
- GetPosition
*Get the position of the actuator. Assume instantaneous movement according to the values in the table.

*If exact current is not listed in the table, return the position value for the nearest current listed.

- GetState
*Return the current state of the actuator

- Shutdown
*Cleanly shut down the actuator (set to zero current)

The Actuator class should have a notion of its current state. Possible states include:
- Uninitialized
- Operational
- Error
- Unknown

Actuator should enter the Error state if current is set to an out of bounds value (higher than max value than listed in the table, negative, etc.).

In this state, it should only respond to Shutdown and Initialize commands.

Write a program that demonstrates the following:
1. Actuator starts in Unknown or Uninitialized state
2. Initialization
3. Returning position for various currents, including currents not listed in the table
4. Entering Error state on invalid input
5. Not responding to SetCurrent commands when in Error state
6. Other test cases as appropriate
