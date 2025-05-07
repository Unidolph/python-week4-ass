def read_file():
    while True:
        filename = input("Please enter the filename to read: ")
        
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile contents:")
                print("-" * 20)
                print(content)
                print("-" * 20)
                break
                
        except FileNotFoundError:
            print(f"Error: The file '{filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"Error: Permission denied when trying to access '{filename}'. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
            print("Please try again with a different file.")
        
        retry = input("\nWould you like to try another file? (yes/no): ")
        if retry.lower() != 'yes':
            print("Program terminated.")
            break

if __name__ == "__main__":
    print("Welcome to the File Reader Program!")
    read_file()