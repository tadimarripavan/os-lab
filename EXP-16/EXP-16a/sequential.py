disk = [0] * 100
start_block = int(input("Enter the starting block: "))
length = int(input("Enter the length of the file: "))

can_allocate = True
for i in range(start_block, start_block + length):
    if i >= len(disk) or disk[i] == 1:  
        can_allocate = False
        break

if can_allocate:
    for i in range(start_block, start_block + length):
        disk[i] = 1  
        print(f"{i}->1")
    print("The file is allocated to disk.")
else:
    print("Error: Not enough continuous free blocks available for allocation.")
