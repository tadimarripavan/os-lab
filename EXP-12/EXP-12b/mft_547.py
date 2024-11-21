def mft():
    ms = int(input("Enter the total memory available (in Bytes) -- "))
    bs = int(input("Enter the block size (in Bytes)-- "))
    n = int(input("Enter the number of processes -- "))

    mp = [int(input(f"Enter memory required for process {i+1} (in Bytes)-- ")) for i in range(n)]
    nob = ms // bs
    ef = ms - nob * bs
    t = 0
    p = 0

    print(f"\nNo. of Blocks available in memory--{nob}")
    print("\n\nPROCESS\tMEMORYREQUIRED\tALLOCATED\tINTERNAL FRAGMENTATION")

    for i in range(n):
        print(f"\n {i+1}\t\t{mp[i]}", end='')
        if mp[i] > bs:
            print("\t\tNO\t\t---")
        else:
            print(f"\t\tYES\t{bs-mp[i]}")
            t += bs-mp[i]
            p += 1
        if p == nob:
            print("\nMemory is Full, Remaining Processes cannot be accommodated")
            break

    print(f"\n\nTotal Internal Fragmentation is {t}")
    print(f"Total External Fragmentation is {ef}")

mft()
