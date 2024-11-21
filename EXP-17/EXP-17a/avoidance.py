def is_safe_state(processes, available, allocation, max_claim):
    work = available[:]  
    finish = [False] * len(processes)
    safe_sequence = []

    while len(safe_sequence) < len(processes):
        progress_made = False
        for i in range(len(processes)):
            if not finish[i]:  
                if all(max_claim[i][j] - allocation[i][j] <= work[j] for j in range(len(available))):
                    for j in range(len(available)):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_sequence.append(i)
                    progress_made = True
                    break
        if not progress_made:  
            return False, []

    return True, safe_sequence

def main():
    num_processes, num_resources = map(int, input("Enter the no. of processes and resources: ").split())

    print("Enter the claim matrix:")
    claim_matrix = [list(map(int, input().split())) for _ in range(num_processes)]


    print("Enter the allocation matrix:")
    allocation_matrix = [list(map(int, input().split())) for _ in range(num_processes)]

    print("Resource vector:")
    available_resources = list(map(int, input().split()))

    safe, safe_sequence = is_safe_state(range(num_processes), available_resources, allocation_matrix, claim_matrix)

    if safe:
        print("System is in safe mode")
        print("The given state is safe state.")
        print("Safe sequence is:", safe_sequence)

        for process in safe_sequence:
            print(f"All the resources can be allocated to Process {process + 1}")
            for j in range(num_resources):
                available_resources[j] += allocation_matrix[process][j]
            print(f"Available resources are: {' '.join(map(str, available_resources))}")
            executed = input(f"Process {process + 1} executed?: ").strip().lower()
            if executed != 'y':
                print("Process did not execute.")
                break
    else:
        print("System is in an unsafe state.")
main()
