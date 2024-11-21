def worst_fit(blocks, files):
    allocation = [-1] * len(files)  # Initialize allocation array

    for i in range(len(files)):
        worst_index = -1

        for j in range(len(blocks)):
            if blocks[j] >= files[i]:
                if worst_index == -1 or blocks[j] > blocks[worst_index]:
                    worst_index = j

        if worst_index != -1:
            allocation[i] = worst_index
            blocks[worst_index] -= files[i]

    # Print results
    print("File No\tFile Size\tBlock No\tBlock Size\tFragment")
    for i in range(len(files)):
        if allocation[i] != -1:
            block_no = allocation[i] + 1
            block_size = blocks[allocation[i]] + files[i]
            fragment = blocks[allocation[i]]
            print(f"{i + 1}\t{files[i]}\t\t{block_no}\t\t{block_size}\t\t{fragment}")
        else:
            print(f"{i + 1}\t{files[i]}\t\tNot Allocated")

# Input
num_blocks = int(input("Enter the number of blocks: "))
num_files = int(input("Enter the number of files: "))

print("Enter the size of the blocks:")
blocks = [int(input(f"Block {i + 1}: ")) for i in range(num_blocks)]

print("Enter the size of the files:")
files = [int(input(f"File {i + 1}: ")) for i in range(num_files)]

# Run the worst fit algorithm
worst_fit(blocks, files)
