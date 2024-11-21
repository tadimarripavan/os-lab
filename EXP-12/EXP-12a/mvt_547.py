def mvt():
    ms = int(input("Enter the total memory available (in Bytes)-- "))
    temp = ms
    mp = []
    n = 0
    ch = 'y'

    while ch == 'y':
        mem = int(input(f"\nEnter memory required for process {n+1} (in Bytes) -- "))
        if mem <= temp:
            print(f"\nMemory is allocated for Process {n+1}")
            temp -= mem
            mp.append(mem)
            n += 1
        else:
            print("\nMemory is Full")
            break
        ch = input("\nDo you want to continue(y/n) -- ")

    print(f"\n\nTotal Memory Available -- {ms}")
    print("\n\n\tPROCESS\t\t MEMORY ALLOCATED ")
    for i, mem in enumerate(mp):
        print(f"\n \t{i+1}\t\t{mem}")
    print(f"\n\nTotal Memory Allocated is {ms-temp}")
    print(f"Total External Fragmentation is {temp}")
mvt()
