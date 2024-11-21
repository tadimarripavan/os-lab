def prevention():
    n = int(input("Enter no of jobs: "))
    jobs = [input("Enter name and time: ").split() for _ in range(n)]
    jobs = [(name, int(time)) for name, time in jobs]
    available_resources = int(input("Enter the available resources: "))
    jobs.sort(key=lambda x: x[1])
    safe_sequence = []
    for name, time in jobs:
        if time <= available_resources:
            safe_sequence.append((name, time))
            available_resources -= time
        else:
            print("No safe sequence")
            return

    print("Safe sequence is: ", end="")
    print(", ".join(f"{name} {time}" for name, time in safe_sequence) + ".")

prevention()
