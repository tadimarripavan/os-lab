def lru_page_replacement(frames, reference_string):
    memory = []
    page_faults = 0

    print("Frame status after each page reference:")
    for page in reference_string:
        if page not in memory:
            # Page fault occurs
            if len(memory) < frames:
                memory.append(page)
            else:
                # Replace the least recently used page
                memory.pop(0)
                memory.append(page)
            page_faults += 1
        else:
            # Page hit, move page to the most recent position
            memory.remove(page)
            memory.append(page)

        # Print current frame status
        print(' '.join(str(p) if p != -1 else '-' for p in memory + [-1] * (frames - len(memory))))

    print(f"No of page faults: {page_faults}")

# Get runtime input
frames = int(input("Enter number of frames: "))
reference_string = list(map(int, input("Enter the reference string (space-separated): ").split()))

lru_page_replacement(frames, reference_string)
