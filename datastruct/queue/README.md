# Queue

## Basic operator

|   Operator    |  Time complexity | Space complexity |           Note            |
| ------------- | ---------------- | ---------------- | ------------------------- |
|  Enqueue      |       O(1)       |        O(1)      | Add to the rear           |
|  Dequeue      |       O(1)       |        O(1)      | Delete the front          |
|  Peek         |       O(n)       |        O(n)      | Return the first element  |
|  is_Empty     |       O(n)       |        O(1)      |                           |
|  is_Full      |       O(n)       |        O(1)      |                           |

## Application

- Task scheduling
- Data transfer
- Simulation
- Priority queues

## Implement

- Implement Queue using Array
- Implement Queue using LinkedList

## Type of Queue

### 1. Circular Queue

The data struct are perform based on First-In First-Out (FIFO) principle. The last position is connected back to the first position to make a circle. It's also called "Ring Buffer"

### 2. Input restricted Queue 

In this type of Queue, the input can be taken from one side.
