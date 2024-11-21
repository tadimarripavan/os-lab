def scan_disk_scheduling(tracks, initial_head):
    tracks.append(initial_head)
    tracks.sort()
    head_index = tracks.index(initial_head)
    right = tracks[head_index:]
    left = tracks[:head_index][::-1]
    order = right + left[1:]

    total_movements = 0
    differences = []
    current_position = initial_head
    for i in range(1, len(order)):
        movement = abs(order[i] - current_position)
        differences.append(movement)
        total_movements += movement
        current_position = order[i]
    print("Tracks traversed   Difference between tracks")
    for i in range(1, len(order)):
        print(f"{order[i]}                {differences[i-1]}")

    avg_movements = total_movements / (len(order) - 1)
    print(f"\nAverage header movements: {avg_movements:.2f}")

n = int(input("Enter no. of tracks: "))
tracks = list(map(int, input("Enter track position: ").split()))
initial_head = int(input("Enter initial head position: "))
scan_disk_scheduling(tracks, initial_head)
