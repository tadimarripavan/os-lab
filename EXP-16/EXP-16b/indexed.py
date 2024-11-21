disk = [0] * 100
def allocate_index_block(index_block, files):
    if disk[index_block] == 1:
        print("Error: Index block is already occupied.")
        return False

    for file_block in files:
        if file_block >= len(disk) or disk[file_block] == 1:
            print(f"Error: Block {file_block} is already occupied or out of range.")
            return False

    disk[index_block] = 1
    for file_block in files:
        disk[file_block] = 1
    
    print("Allocated")
    print("File indexed")
    for file_block in files:
        print(f"{index_block}->{file_block}:1")
    
    return True

while True:
    index_block = int(input("Enter index block: "))
    num_files = int(input("Enter number of files on index: "))

    files = []
    for _ in range(num_files):
        file_block = int(input("Enter block number for the file: "))
        files.append(file_block)

    if allocate_index_block(index_block, files):
        choice = int(input("Enter 1 to enter more files and 0 to exit: "))
        if choice == 0:
            break
    else:
        print("Allocation failed.")
        break
