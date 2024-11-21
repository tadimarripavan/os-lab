
disk = [0] * 100
num_allocated = int(input("Enter how many blocks that are already allocated: "))
print("Enter the blocks no.s that are already allocated:")
for _ in range(num_allocated):
    block = int(input())
    disk[block] = 1  

start_block = int(input("Enter the starting index block: "))
length = int(input("Enter the length of the file: "))

allocated_count = 0
block = start_block

while allocated_count < length and block < len(disk):
    if disk[block] == 0:  
        disk[block] = 1   
        print(f"{block}->1")
        allocated_count += 1
    else:
        print(f"{block}->1 file is already allocated")
    
    block += 1
if allocated_count == length:
    print("The file is allocated to disk.")
else:
    print("Error: Not enough free blocks available to allocate the file.")
