#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import configparser
import pandas as pd
import pyarrow as pa
import os
import pyarrow.parquet as pq

# Step 1: Get the current folder location
current_folder = os.getcwd()

# Step 2: List all .csv files and their full paths in the current folder
csv_files = [os.path.join(current_folder, filename) for filename in os.listdir(current_folder) if filename.endswith('.csv')]

# Step 3: Set the output directory to the current folder
output_directory = current_folder

# Create a configuration file
config = configparser.ConfigParser()
config['FileList'] = {}
config['FileList']['files_to_convert'] = '\n'.join(csv_files)
config['FileList']['output_directory'] = output_directory

# Save the configuration to a .ini file
with open('config.ini', 'w') as configfile:
    config.write(configfile)

# Load the configuration from the ini file
config = configparser.ConfigParser()
config.read(current_folder+'/config.ini')

# Read the list of files to convert
files_to_convert = [x.strip() for x in config.get('FileList', 'files_to_convert').split('\n')]

# Read the output directory
output_directory = config.get('FileList', 'output_directory')

# Normalize the output directory
output_directory = os.path.normpath(output_directory)

# Process each file
for input_filename in files_to_convert:
    # Construct the full input path
    full_input_path = os.path.join(output_directory, input_filename)

    # Construct the output filename, e.g., change .csv to .parquet
    output_filename = os.path.splitext(input_filename)[0] + '.parquet'

    try:
        # Try reading the CSV file into a pandas DataFrame using UTF-8 encoding
        df = pd.read_csv(full_input_path)

    except FileNotFoundError:
        print(f"The input file '{full_input_path}' does not exist.")
        continue

    except UnicodeDecodeError:
        # If reading with UTF-8 encoding fails, try reading with Latin1 encoding
        try:
            df = pd.read_csv(full_input_path, encoding='latin1')
        except Exception as e:
            print(f"An error occurred while reading the CSV file: {str(e)}")
            continue

    try:
        # Convert the pandas DataFrame to a pyarrow Table
        table = pa.Table.from_pandas(df)

        # Construct the full output path
        full_output_path = os.path.join(output_directory, output_filename)

        # Write the pyarrow Table to a Parquet file
        pq.write_table(table, full_output_path)

        print(f"Conversion complete. Parquet file saved as {full_output_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
