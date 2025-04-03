def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            content = infile.read()
        
        # Modify content (example: convert to uppercase)
        modified_content = content.upper()
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content written to {output_file}")
    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"An error occurred: {e}")