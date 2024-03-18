Introduction:
The config_csv2parquet.py script facilitates the conversion of CSV files to Parquet format. 
Before running the script, ensure that the Python file resides in the same directory as the CSV files intended for conversion. Subfolders within the directory are not supported.

Generating an Executable (.exe) File:

Step 1: Install PyInstaller
Ensure that PyInstaller is installed on your system. If not, you can install it via pip using the following command: 
"pip install pyinstaller"

Step 2: Navigate to the Script's Directory
Open a command prompt or Anaconda prompt and navigate to the directory where the config_csv2parquet.py script is located. You can use the cd command to change directories.
For example: "cd I:/Projects/csv_to_parquet"

Step 3: Generate the Executable File
Execute the following command to generate a standalone executable file: 
"pyinstaller config_csv2parquet.py --onefile"
