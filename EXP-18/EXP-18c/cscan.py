def cscan_disk_scheduling(tracks, initial_head):
    tracks.append(initial_head)
    tracks.sort()
    head_index = tracks.index(initial_head)
    right = tracks[head_index:]
    left = tracks[:head_index]
    order = right + [0] + left

    total_movements = 0
    differences = []
    current_position = initial_head
    for i in range(1, len(order)):
        movement = abs(order[i] - current_position)
        differences.append(movement)
        total_movements += movement
        current_position = order[i]
    print("Tracks traversed   Difference Between tracks")
    for i in range(1, len(order)):
        print(f"{order[i]}                {differences[i-1]}")

    avg_movements = total_movements / (len(order) - 1)
    print(f"\nAverage seek time : {avg_movements:.7f}")
tracks = list(map(int, input("Enter the track position: ").split()))
initial_head = int(input("Enter starting position: "))
cscan_disk_scheduling(tracks, initial_head)
