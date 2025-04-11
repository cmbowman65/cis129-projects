"""
CIS188, Lab 9 - Image and PDF Zip File

This program takes a provided zip file and then:
- finds the downloaded zip file 'files.zip' (a little extra, but program will run if
  'files.zip' is anywhere on the c drive)
- creates two new folders, called images and pdf, in the directory of 'files.zip'
- organizes files from 'files.zip' into the images and pdf folders, based on file types
- prints a directory of the folders and files in the images and pdf folders
- displays the total number of files in each folder

Author:  Cliff Bowman

Date:  11 Apr 2025

"""

import shutil, os, zipfile, sys
from pathlib import Path

def find_file_path(filename, search_path):
    """
    Finds a file within a specified directory and its subdirectories
    
    Action:  searches a specified directory for a specific file

    Input:   filename: The name of the file to find.
             search_path: The directory to search in.
    
    Output:  None

    Returns: The Path object of the file if found.
    """    
    search_path = Path(search_path)
    for root, _, files in os.walk(search_path):
        if filename in files:
            return Path(root) / filename
        

def contents_and_total(directory):
    """
    Outputs directory path, names of files in directory, and number of files
    
    Action:  uses os.walk to go through directory

    Input:   directory: The name of the folder to iterate and 
             output contents and number of files
    
    Output:  Directory name, each file in the folder, and the total number of files 
             in the folder

    Returns: None
    """
    
    print(f"\nDirectory listing for {directory}:")  
    file_total = 0  # initialize counter
    for root, _, files in os.walk(directory):
        for file in files:
            print(file)  
            file_total += 1  
    print('=' * 45 + '\n')
    print(f"Total number of files in {directory}: {file_total}\n")  


def main():    
    """ 
    Main function
    
    Action: Calls other functions, quits program if it cannot find 'files.zip', 
            unzips files.zip, extracts files, closes files.zip, creates new 
            directories, moves files to appropriate directory.
    
    Input:  none
    
    Output: Path for 'files.zip' or output if files.zip cannot be found. 
    
    Return: none
    """   
    # call to find path for 'files.zip'
    zip_path = find_file_path('files.zip', 'c:\\')

    # output path for user of 'files.zip' or quit the program if not found
    if zip_path:
        print(f"File 'files.zip' found at: {zip_path}")
    
    else:
        print("File 'files.zip' not found on C drive.")
        print("The program will quit for you to download 'files.zip' to the C drive.")
        sys.exit()
    
    # path object for parent directory of 'files.zip'
    current_dir = zip_path.parent

    # define the paths for the new directories 'images' and 'pdf' and create folders if not already created
    images = current_dir / 'images'
    pdfs = current_dir / 'pdf'
    images.mkdir(exist_ok=True)
    pdfs.mkdir(exist_ok=True)

    # unzip 'files.zip', extract files to 'all_files' folder and close zip file
    with zipfile.ZipFile(current_dir / 'files.zip', 'r') as my_zip:
        my_zip.extractall(current_dir / 'all_files')

    # use os.walk to go through each directory/subdirectory in 'all_files' 
    for root, _, files in os.walk(current_dir / 'all_files'):
        for file in files:
            p = Path(root) / file
            
            # move files to the appropriate directory by file extension
            if p.suffix == '.jpg':
                os.rename(p, images / p.name)
            elif p.suffix == '.pdf':
                os.rename(p, pdfs / p.name)
    
    # remove folder 'all_files', subdirectories, and files            
    shutil.rmtree(current_dir / 'all_files')               
    
    # call to output results            
    contents_and_total(images)
    contents_and_total(pdfs)

# call main
main()