def round_robin():
    n=int(input("Enter the no of processes: "))
    bt=[int(input(f"Enter Burst Time for process {i+1}: "))for i in range(n)]
    ct=bt.copy()
    slice=int(input("Enter the size of the slice: "))
    tat=[0]*n
    temp=0
    while any(b>0 for b in bt):
        for i in range(n):
            if bt[i]>0:
                if bt[i]<=slice:
                    temp+=bt[i]
                    tat[i]=temp
                    bt[i]=0
                else:
                    bt[i]-=slice
                    temp+=slice
    wt=[tat[i]-ct[i] for i in range(n)]
    print("\n\tPROCESS\t BURST TIME \t WAITING TIME \t TURNAROUND TIME")
    for i in range(n):
        print(f"\t{i+1} \t {ct[i]} \t\t {wt[i]} \t\t {tat[i]}")
    print("\nThe Average Waiting time is: ",(sum(wt)/n))
    print("\nThe Average Turnaround time is: ",(sum(tat)/n))
round_robin()
