# Linked List with File I/O
This project implements a program that reads a list of integers from a file, stores them in a sorted linked list, and allows user interaction for insertion or removal.

## How to Use:
1. Create a text file named data.txt and populate it with a list of integers, one per line. Ensure there are no duplicates.
2. Run the program using python main.py.
3. The program will:
  -  Read the data from data.txt.
  -  Print the initial sorted linked list.
  -  Ask you to enter an integer value (x).
  -  Based on the entered value:
        -  If x exists in the list, it will be removed.
        -  If x doesn't exist, it will be inserted into the linked list while maintaining sorted order.
        -   Print the final linked list.
          
## Code Structure:
The code is organized into two modules:
  -  linked_list.py: Defines the Node and LinkedList classes for creating and manipulating a linked list.
  -  main.py: Implements the main program logic for reading data from a file, creating the linked list, and user interaction.
