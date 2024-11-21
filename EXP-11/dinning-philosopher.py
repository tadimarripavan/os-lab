def main():
    philosophers = []
    hungry_positions = []
    total_philosophers = int(input("Enter the total number of philosophers: "))
    hungry_count = int(input("How many are hungry: "))
    
    for i in range(hungry_count):
        pos = int(input(f"Enter philosopher {i + 1} position: "))
        hungry_positions.append(pos - 1)  
    
    for i in range(total_philosophers):
        philosophers.append("waiting")
    
    while True:
        print("\n1. One can eat at a time")
        print("2. Two can eat at a time")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            print("Allow one philosopher to eat at any time")
            for pos in hungry_positions:
                print(f"P {pos + 1} is granted to eat")
                for other_pos in hungry_positions:
                    if other_pos != pos:
                        print(f"P {other_pos + 1} is waiting")   
        elif choice == 2:
            print("Allow two philosophers to eat at same time")
            combinations = [(i, j) for i in hungry_positions for j in hungry_positions if i != j]
            combination_count = 1
            
            for i, j in combinations:
                print(f"combination {combination_count}")
                print(f"P {i + 1} and P {j + 1} are granted to eat")
                for pos in hungry_positions:
                    if pos != i and pos != j:
                        print(f"P {pos + 1} is waiting")
                combination_count += 1 
        elif choice == 3:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice, please try again.")

main()
