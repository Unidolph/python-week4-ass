 modify_file(input_file, output_file):
    try:
        # Read the input file
        with open(input_file, 'r') as file:
            content = file.read()
            
        # Modify the content (for example, convert to uppercase)
        modified_content = content.upper()
        
        # Write to the output file
        with open(output_file, 'w') as file:
            file.write(modified_content)
            
        print(f"Successfully read from {input_file} and wrote modified content to {output_file}")
        
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except PermissionError:
        print(f"Error: Permission denied when accessing {input_file} or {output_file}")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    input_file = "sample.txt"
    output_file = "modified_sample.txt"
    modify_file(input_file, output_file)