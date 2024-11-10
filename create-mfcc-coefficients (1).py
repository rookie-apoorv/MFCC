# Uncomment the following line if you do not have the Python module 'librosa' installed
# !pip install librosa

import os
import numpy as np
import pandas as pd
import librosa

# Function to create MFCC coefficients given an audio file

def create_MFCC_coefficients(file_name):

    sr_value = 44100
    n_mfcc_count = 20
    
    try:
        # Load the audio file using librosa
        y, sr = librosa.load(file_name, sr=sr_value)
              
        # Compute MFCC coefficients for the segment
        mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=n_mfcc_count)
        #print(f"file_name: {file_name}: y={len(y)}, sr={sr}, mfccs matrix:{np.shape(mfccs)}")
        
        # Create and return MFCC dataframe
        coeff_df = pd.DataFrame(mfccs)
        
        return coeff_df

    except Exception as e:
       print(f"Error creating MFCC coefficients: {file_name}:{str(e)}")

input_folder = "MP3_for_training/asha_bhosle"  # Folder with MP3 files
output_folder = "MFCC_train/asha_bhosle"                       # Folder to store CSV files

# Create output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Process each MP3 file in the input folder
for file_name in os.listdir(input_folder):
    if file_name.endswith(".mp3"):
        full_path = os.path.join(input_folder, file_name)
        
        # Generate MFCC coefficients
        coeff_df = create_MFCC_coefficients(full_path)
        
        if coeff_df is not None:
            # Create a CSV file for each MP3 file in the output folder
            csv_file_name = f"{os.path.splitext(file_name)[0]}-MFCC.csv"
            output_path = os.path.join(output_folder, csv_file_name)
            
            # Save DataFrame to CSV
            coeff_df.to_csv(output_path, index=False)
            print(f"Saved: {output_path}")

            
