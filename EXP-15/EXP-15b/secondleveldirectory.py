
class Directory:
    def __init__(self, name):
        self.name = name
        self.files = []

    def add_file(self, file_name):
        self.files.append(file_name)

    def delete_file(self, file_name):
        if file_name in self.files:
            self.files.remove(file_name)
            print(f"File {file_name} deleted")
        else:
            print(f"File {file_name} not found")

    def search_file(self, file_name):
        if file_name in self.files:
            print(f"File {file_name} found")
        else:
            print(f"File {file_name} not found")

class FileSystem:
    def __init__(self):
        self.directories = {}

    def create_directory(self, dir_name):
        if dir_name not in self.directories:
            self.directories[dir_name] = Directory(dir_name)
            print(f"Directory {dir_name} created")
        else:
            print(f"Directory {dir_name} already exists")

    def create_file(self, dir_name, file_name):
        if dir_name in self.directories:
            self.directories[dir_name].add_file(file_name)
            print(f"File {file_name} created")
        else:
            print(f"Directory {dir_name} not found")

    def delete_file(self, dir_name, file_name):
        if dir_name in self.directories:
            self.directories[dir_name].delete_file(file_name)
        else:
            print(f"Directory {dir_name} not found")

    def search_file(self, dir_name, file_name):
        if dir_name in self.directories:
            self.directories[dir_name].search_file(file_name)
        else:
            print(f"Directory {dir_name} not found")

    def display(self):
        if not self.directories:
            print("No Directories")
        else:
            print("\nDirectory\tFiles")
            for dir_name, directory in self.directories.items():
                print(f"\n{dir_name}\t\t", end="")
                for file_name in directory.files:
                    print(f"\t{file_name}", end="")

def main():
    file_system = FileSystem()

    while True:
        print("\n1. Create Directory")
        print("2. Create File")
        print("3. Delete File")
        print("4. Search File")
        print("5. Display")
        print("6. Exit")
        choice = input("Enter your choice -- ")

        if choice == "1":
            dir_name = input("Enter name of directory -- ")
            file_system.create_directory(dir_name)
        elif choice == "2":
            dir_name = input("Enter name of the directory -- ")
            file_name = input("Enter name of the file -- ")
            file_system.create_file(dir_name, file_name)
        elif choice == "3":
            dir_name = input("Enter name of the directory -- ")
            file_name = input("Enter name of the file -- ")
            file_system.delete_file(dir_name, file_name)
        elif choice == "4":
            dir_name = input("Enter name of the directory -- ")
            file_name = input("Enter name of the file -- ")
            file_system.search_file(dir_name, file_name)
        elif choice == "5":
            file_system.display()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

main()
