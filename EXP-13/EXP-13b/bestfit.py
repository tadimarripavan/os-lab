def best_fit(blocks, files):
    allocation = [-1] * len(files)  

    for i in range(len(files)):
        best_index = -1

        for j in range(len(blocks)):
            if blocks[j] >= files[i]:
                if best_index == -1 or blocks[j] < blocks[best_index]:
                    best_index = j

        if best_index != -1:
            allocation[i] = best_index
            blocks[best_index] -= files[i]

    print("File No\tFile Size\tBlock No\tBlock Size\tFragment")
    for i in range(len(files)):
        if allocation[i] != -1:
            block_no = allocation[i] + 1
            block_size = blocks[allocation[i]] + files[i]
            fragment = blocks[allocation[i]]
            print(f"{i + 1}\t{files[i]}\t\t{block_no}\t\t{block_size}\t\t{fragment}")
        else:
            print(f"{i + 1}\t{files[i]}\t\tNot Allocated")

num_blocks = int(input("Enter the number of blocks: "))
num_files = int(input("Enter the number of files: "))

print("Enter the size of the blocks:")
blocks = [int(input(f"Block {i + 1}: ")) for i in range(num_blocks)]

print("Enter the size of the files:")
files = [int(input(f"File {i + 1}: ")) for i in range(num_files)]

best_fit(blocks, files)
