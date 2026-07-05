import time

def display(total_disks, rods):
    width = (total_disks * 2) + 1

    for level in range(total_disks - 1, -1, -1):
        line = ""
        for rod_name in ['A', 'B', 'C']:
            rod = rods[rod_name]
            if level < len(rod):
                disk_size = rod[level]
                part = ("=" * (disk_size * 2 - 1)).center(width)
            else:
                part = "|".center(width)
            line += part + "    "
        print(line.rstrip())

    print("-" * ((width + 4) * 3))
    print("A".center(width) + "    " + "B".center(width) + "    " + "C".center(width))
    print("\n")

def move(n, source, auxiliary, target, source_name, auxiliary_name, target_name, rods, total_disks, stats):
    if n <= 0:
        return

    # Move n-1 disks to auxiliary
    move(n-1, source, target, auxiliary, source_name, target_name, auxiliary_name, rods, total_disks, stats)
    
    # Move the nth disk
    target.append(source.pop())
    stats['moves'] += 1 # Incremented on each actual move
    
    # Visual update
    print(f"[{stats['moves']}] Moving disk {n} from {source_name} to {target_name}:")
    display(total_disks, rods)
    time.sleep(0.8) # Animation speed
    
    # Move n-1 disks to target
    move(n-1, auxiliary, source, target, auxiliary_name, source_name, target_name, rods, total_disks, stats)

def main():
    while True:
        print('--- Tower of Hanoi ---')
        print('1. Start program')
        print('2. Exit')
        option = input('\nPlease enter your choice: ')
        
        if option == '1':
            try:
                n = int(input('How many disks? (max 8): '))       
                if n <= 0 or n > 8:
                    print("Error: Please enter a number between 1 and 8.\n")
                    continue           
                
                rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
                
                print("\nInitial State:")
                display(n, rods)
                input("Press Enter to start...")
                
                # Stats dictionary to store total moves
                stats = {'moves': 0}
                
                # Start timer
                start_time = time.time()
                
                move(n, rods['A'], rods['B'], rods['C'], "A", "B", "C", rods, n, stats)
                
                # End timer
                end_time = time.time()
                elapsed_time = end_time - start_time
                
                # Print Summary
                print("=" * 40)
                print(" Puzzle Solved Successfully!")
                print(f"Total Moves: {stats['moves']}")
                print(f"Time Taken: {elapsed_time:.2f} seconds")
                print("=" * 40 + "\n")
                
            except ValueError:
                print('Error: Please enter a valid integer!\n') 
        elif option == '2':
            print("Goodbye!")
            break
        else:
            print('Invalid choice, try again.\n')

if __name__ == "__main__":
    main()
