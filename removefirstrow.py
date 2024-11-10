import os
import pandas as pd

def remove_first_row_from_csv(file_path):
    try:
        # Load the CSV file without assuming a header row
        df = pd.read_csv(file_path, header=None)
        
        # Remove the first row
        df = df.iloc[1:]  # Keep all rows except the first one
        
        # Save back to the same CSV file, overwriting it
        df.to_csv(file_path, index=False, header=False)
        print(f"Processed: {file_path}")
        
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

def process_all_csv_files(folder_path):
    # Recursively go through each file in the folder
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.csv'):
                full_path = os.path.join(root, file_name)
                # Process each CSV file
                remove_first_row_from_csv(full_path)

if __name__ == "__main__":
    # Folder containing the CSV files
    input_folder = "MFCC_train/tocorrect"
    process_all_csv_files(input_folder)
