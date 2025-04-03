def modify_content(content):
    # Example modification: Convert text to uppercase
    return content.upper()
def process_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        modified_content = modify_content(content)
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    
