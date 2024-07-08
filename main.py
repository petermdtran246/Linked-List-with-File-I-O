from linked_list import LinkedList

def read_numbers_from_file(file_name):
    numbers = []
    with open(file_name, 'r') as file:
        for line in file:
            number = int(line.strip())
            numbers.append(number)
    return numbers

if __name__ == "__main__":
    # Read numbers from file
    file_data = 'data.txt'
    numbers = read_numbers_from_file(file_data)

    # Insert sorted numbers into linked list
    linked_list = LinkedList()
    for number in numbers:
        linked_list.insert(number)

    # Print the initial linked list
    print(f'Initial linked list: ')
    linked_list.print_list()

    # Ask the user for a number to insert or remove
    x = int(input(f'Enter an integer value x: '))

    # Insert or remove x
    if linked_list.find(x):
        linked_list.remove(x)
        print(f'Removed {x} from the linked list. ')
    else:
        linked_list.insert(x)
        print(f'Inserted {x} into the linked list. ')

    # Print the final linked list
    print(f'Final linked list: ')
    linked_list.print_list()