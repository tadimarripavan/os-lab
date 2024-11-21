def fifo_page_replacement(pages, capacity):
    memory = [-1] * capacity
    page_faults = 0
    fifo_index = 0

    for page in pages:
        if page not in memory:
            page_faults += 1
            memory[fifo_index] = page
            fifo_index = (fifo_index + 1) % capacity
        
        print(" ".join(str(x) for x in memory))

    print(f"\nNumber of page faults: {page_faults}")

# Example input based on the provided output
pages = list(map(int,input("Enter the pages").split()))
capacity = int(input("Enter frames"))
fifo_page_replacement(pages, capacity)
