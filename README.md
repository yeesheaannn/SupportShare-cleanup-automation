# SupportShare-cleanup-automation
Within DHS environment, each site has a share folder called SupportShare which usually used by projects team, support, and delivery team.

### SupportShare Path
Below you can find a list of all share folder and its path in each site.

![image](https://github.com/user-attachments/assets/3fcca0d5-d291-468e-a41f-090fb11eb059)


### Script
This script needs to run from Management Server and script also currently can be run from Management Server HSx-MGM-04 only, on each site.

Script located in X:\Scripts\Misc\Clean SupportShare\HSx\cleanSupportShare.py

![image](https://github.com/user-attachments/assets/f594ebb2-df6b-4040-869a-e38e98e9495b)

HSx refers to site.
For Production sites:

![image](https://github.com/user-attachments/assets/a65f19d0-44d2-43bc-82d7-d48a0b6260df)

For Staging site:

![image](https://github.com/user-attachments/assets/21fcd1c1-bdc0-4827-8afb-2474712b0094)


### Purpose
This script automates the cleanup of the SupportShare directory by identifying and removing files and folders that are older than 30 days, excluding specific folders from deletion. The process is logged to a file to ensure traceability and troubleshooting capabilities.


### Features
  - Customizable Cleanup Threshold:
    - Deletes files and folders older than 30 days.
    - The threshold can be adjusted by modifying the threshold variable.
   
  - Folder Exclusion:
    - Specific folders (FileTransfer, Operations, Tools, Temporary, Certificate) are excluded from deletion.
      
  - Logging:
    - Logs are stored with the current date in the filename for easy identification.
    - Includes information about files and folders found to be deleted, as well as any errors encountered.


### Main Execution
  - Iterates over the SupportShare folder path in supportshare_path.
  - Executes cleanup process for the directory, passing the logger.
  - Logs the deleted files or folders, and any errors that occur during the cleanup.


### How to Set Up and Use
1. Setup Environment:
     - Ensure Python is installed and accessible on your system.
     - Verify that the supportshare_path and log_file paths are accessible from the script's execution context.

    
2. Schedule the cleanSupportShare.py script using Task Scheduler:
     - Open Task Scheduler.
     - Click "Create Task" in the upper-right part of the Task Scheduler window.

       ![image](https://github.com/user-attachments/assets/2e01201a-5e9f-42cf-bdf4-0990d3c4923f)

     - In the General tab:
     - Enter the Name and Description for the script.
     - Choose the appropriate user account to run the script.
     - ***Ensure this account has the necessary permissions to access and modify the target directories.

     - Check "Run whether user is logged on or not" to allow the task to execute even if the user is not logged in.
     - Check "Run with highest privileges" to ensure the script has administrative permissions.
       ![image](https://github.com/user-attachments/assets/56d31fc1-cb4b-4640-bc3d-731707123b55)

     - In the Triggers tab:
     - Click "New" at the bottom.
       ![image](https://github.com/user-attachments/assets/ccbb6ceb-c3ca-454c-aff1-eb8eae4f649a)

     - Select "Monthly" as the task schedule type.
     - Choose a start date and time for the script to begin running (In this case, we are choosing "10 am" for every site).
     - Click the "Months" drop down list and select "<Select all months>" to run the script every month.
     - Under "On", select a specific occurrence (In this case, we are choosing "First Monday" for every site).
     - Click OK to save the Trigger settings.
       ![image](https://github.com/user-attachments/assets/6140ebda-4589-4822-98e3-c7e9f9c8c1de)
     - So, now the script is set to be run on on every first Monday of each month at 10 am of the server time.

     - In the Actions tab:
     - Click "New" at the bottom.
       ![image](https://github.com/user-attachments/assets/30ff096f-db40-4a1d-a0c8-141eea2e07c9)

     - Select "Start a program".
     - Specify the program python.exe along with the script path "\\qhs\fssite\AdminShare\Scripts\Misc\Clean SupportShare\HSx\cleanSupportShare.py" in the Add arguments field.
     - ***Replace the "site" behind fs with the site name (e.g., fseueh) and "x" behind HS with the site number (e.g., HS2)
     - In the Start in field, enter the C:\ directory.
     - Click OK to save the Action settings.
       ![image](https://github.com/user-attachments/assets/8107d11f-54d7-4bc2-92ac-5ce89b8351db)

     - Click OK to save the task.
     - If prompted, enter the password for the selected user account.
       ![image](https://github.com/user-attachments/assets/76e57ae0-34a8-456f-a1e5-e5a42da3c54f)

     - The task to run the cleanSupportShare.py script automatically on the first Monday of each month has been successfully scheduled.
       ![image](https://github.com/user-attachments/assets/de5a1f9a-b437-4649-aaa6-de2c3339047a)


3. Review Logs:
   - Logs are stored in the logs folder located in X:\Scripts\Misc\Clean SupportShare\HSx\logs after the script has been run by the Task Scheduler.
     ![image](https://github.com/user-attachments/assets/bef49c72-438a-49a5-ae8a-54bc575bdb92)

     ![image](https://github.com/user-attachments/assets/edad55e8-f63c-4bb8-b40c-1dc82dcf85bc)

   - Check the log files for the corresponding date to review the details about the execution process and any errors.
     ![image](https://github.com/user-attachments/assets/629a5d79-17b8-4898-8bcd-ac0c6c4b95bf)
   - If any files or folders exceed the 30-day threshold, they will be listed for deletion. Specific folders (FileTransfer, Operations, Tools, Temporary, Certificate) are excluded from deletion.
   - If no files or folders meet the threshold, the messages "No files can be deleted" or "No folders can be deleted" will be displayed.


    ![image](https://github.com/user-attachments/assets/cd99be46-655a-47b1-9796-78d667f3edb2)
   - If there are no files and folders meet the threshold, the messages "No files and folders can be deleted" will be displayed. 
