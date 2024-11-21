def optimal_page_replacement(frames, reference_string):
    memory = []
    page_faults = 0

    for i, page in enumerate(reference_string):
        if page not in memory:
            if len(memory) < frames:
                memory.append(page)
            else:
                farthest = -1
                index_to_replace = -1
                for j in range(len(memory)):
                    if memory[j] not in reference_string[i + 1:]:
                        index_to_replace = j
                        break
                    else:
                        next_index = reference_string[i + 1:].index(memory[j])
                        if next_index > farthest:
                            farthest = next_index
                            index_to_replace = j

                memory[index_to_replace] = page
            page_faults += 1
        
        print(' '.join(str(p) if p != -1 else '-' for p in memory + [-1] * (frames - len(memory))))

    page_fault_rate = (page_faults / len(reference_string)) * 100

    print(f"Number of page faults: {page_faults}")
    print(f"Page fault rate = {page_fault_rate:.6f}")

n = int(input("Enter length of the reference string: "))
reference_string = list(map(int, input("Enter the reference string: ").split()))
frames = int(input("Enter no of frames: "))

optimal_page_replacement(frames, reference_string)
