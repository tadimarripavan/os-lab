def main():
    directory_name = input("Enter name of directory -- ")
    files = []
    while True:
        print("\n1. Create File")
        print("2. Delete File")
        print("3. Search File")
        print("4. Display Files")
        print("5. Exit")        
        choice = int(input("Enter your choice – "))

        if choice == 1:  
            file_name = input("Enter the name of the file -- ")
            if file_name in files:
                print(f"File {file_name} already exists")
            else:
                files.append(file_name)
                print(f"File {file_name} created")

        elif choice == 2:  
            file_name = input("Enter the name of the file – ")
            if file_name in files:
                files.remove(file_name)
                print(f"File {file_name} is deleted")
            else:
                print(f"File {file_name} not found")

        elif choice == 3:  
            file_name = input("Enter the name of the file – ")
            if file_name in files:
                print(f"File {file_name} found")
            else:
                print(f"File {file_name} not found")

        elif choice == 4:  
            if files:
                print("The Files are --", " ".join(files))
            else:
                print("No files in the directory")

        elif choice == 5:  
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")
main()
