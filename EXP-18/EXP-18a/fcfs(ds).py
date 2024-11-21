def fcfs_ds():
    n = int(input("Enter the number of tracks: "))
    t = []
    print("Enter the tracks to be traversed:")
    for i in range(n):
        track = int(input(f"Track {i + 1}: "))
        t.append(track)
    tohm = []
    tot = 0
    for i in range(1, n):
        difference = abs(t[i] - t[i - 1])
        tohm.append(difference)
        tot += difference
    avhm = tot / n
    print("Tracks traversed\tDifference between tracks")
    for i in range(1, n):
        print(f"{t[i]}\t\t\t{tohm[i - 1]}")
    print(f"\nAverage header movements: {avhm:.6f}")
fcfs_ds()
