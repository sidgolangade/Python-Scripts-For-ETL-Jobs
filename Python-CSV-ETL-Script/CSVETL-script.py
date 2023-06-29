import csv

def extract_data(input_file):
    data = []
    with open(input_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return data

def transform_data(data):
    transformed_data = []
    for row in data:
        transformed_row = [cell.upper() for cell in row]  # Example transformation: Convert all cells to uppercase
        transformed_data.append(transformed_row)
    return transformed_data

def load_data(output_file, data):
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def etl_process(input_file, output_file):
    # Extract data from CSV
    extracted_data = extract_data(input_file)
    
    # Transform the extracted data
    transformed_data = transform_data(extracted_data)
    
    # Load the transformed data into a new CSV file
    load_data(output_file, transformed_data)

# Example usage
input_file = input("Enter the Path where the 'input.csv' file is located: ")
output_file = 'output.csv'
etl_process(input_file, output_file)
