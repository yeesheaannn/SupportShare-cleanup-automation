###############################################################
##	cleanSupportShare.py
##
##	Script to read Files and Folders in SupportShare
##
##  01-06-2023		1.0.0	Arief - Initial Submit
##  01-06-2023      1.1.0   Arief - Added 30 days threshold
##                                - Added exclude Folders to be read
##	12-06-2023		1.2.0	Arief - Prompt to user before Files and Folder deletion
##	14-06-2023		1.2.0	Arief - Remove unnecessary syntax
##  10-05-2024		1.2.1	Arief - Update shutil instead of os.rmdir to delete not empty folder
##  20-09-2024      1.2.2   Arief - Added exclude Certificate folder to be read
##  20-11-2024      1.2.3   YS    - Done modifying the script
###############################################################

import os
import shutil
import time
import logging
from datetime import datetime

supportshare_path = '//qhs/fsusec/SupportShare'
current_time = time.time()
threshold = 30 * 24 * 60 * 60  # 30 days

# Generate a log file name with the current date
current_date = datetime.now().strftime("%d-%m-%Y")
log_file = f"//qhs/fsusec/AdminShare/Scripts/Misc/Clean SupportShare/HS5/logs/{current_date}_Clean_SupportShare.log"

# Function to setup a logger with file output
def setup_logger(log_file, level=logging.INFO):
    handler = logging.FileHandler(log_file)        
    handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s'))

    logger = logging.getLogger("CleanupLogger")
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger
    
logger = setup_logger(log_file)

# Exclude folder by specific name
excluded_folders = ['FileTransfer', 'Operations', 'Tools', 'Temporary', 'Certificate']

try: 
    files = []
    folders = []

    logger.info("Starting cleanup process for SupportShare...")

    for item_name in os.listdir(supportshare_path):

        # Skip the folder if folder name matches
        if item_name in excluded_folders:
            continue
        
        item_path = os.path.join(supportshare_path, item_name)
    
        # Check if the file is older than the threshold
        if os.path.isfile(item_path) and current_time - os.path.getmtime(item_path) > threshold:
            files.append(item_name)
        elif os.path.isdir(item_path) and current_time - os.path.getmtime(item_path) > threshold:
            folders.append(item_name)

    if not files and not folders:
        logger.info("No files and folders can be deleted.\n")
    else:
        logger.info("Files found for deletion:")
        if not files:
            logger.info("No files can be deleted.")
        else:
            for file_name in files:
                logger.info(f"  {file_name}")
    
        logger.info("Folders found for deletion:")
        if not folders:
            logger.info("No folders can be deleted.")
        else:
            for folder_name in folders:
                logger.info(f"  {folder_name}")
   
        for file_name in files:
            file_path_to_delete = os.path.join(supportshare_path, file_name)
            logger.info(f"Deleting file: {file_name}")
            os.remove(file_path_to_delete)
    
        for folder_name in folders:
            folder_path_to_delete = os.path.join(supportshare_path, folder_name)
            logger.info(f"Deleting folder: {folder_name}")
            shutil.rmtree(folder_path_to_delete)
        
        logger.info("Cleanup process completed.\n")

except Exception as err:
    logger.error(err)