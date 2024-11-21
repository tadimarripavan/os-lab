def pro_con():
    buffer = []
    buffer_size = 1  

    while True:
        print("\n1. Produce 2. Consume 3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:  
            if len(buffer) < buffer_size:
                value = int(input("Enter the value: "))
                buffer.append(value)
            else:
                print("Buffer is Full")

        elif choice == 2:  
            if buffer:
                consumed_value = buffer.pop(0)
                print(f"The consumed value is {consumed_value}")
            else:
                print("Buffer is Empty")

        elif choice == 3:  
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")
pro_con()
