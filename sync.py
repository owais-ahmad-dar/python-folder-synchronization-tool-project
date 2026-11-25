import os
import shutil
from datetime import datetime
def compare_files(source_path, backup_path):

    if not os.path.exists(backup_path):
        return "New File"

    source_size = os.path.getsize(source_path)
    backup_size = os.path.getsize(backup_path)

    source_time = os.path.getmtime(source_path)
    backup_time = os.path.getmtime(backup_path)

    if source_size != backup_size or source_time > backup_time:
        return "Updated File"

    return "Unchanged File"


def main():

    main_folder = os.path.dirname(os.path.abspath(__file__))

    source = os.path.join(main_folder, "source")
    backup = os.path.join(main_folder, "Backup")

    history = os.path.join(main_folder, "backup_history.txt")

    if os.path.exists(source):

        os.makedirs(backup, exist_ok=True)

        count = 0

        for item in os.listdir(source):

            source_path = os.path.join(source, item)
            backup_path = os.path.join(backup, item)

            status = compare_files(source_path, backup_path)

            print(item, ":", status)

            if os.path.isdir(source_path):

                shutil.copytree(
                    source_path,
                    backup_path,
                    dirs_exist_ok=True
                )

            else:
                shutil.copy2(source_path, backup_path)

            

            count += 1

        # Save backup history
        with open(history, "a") as file:

            file.write("\nBackup Date: ")
            file.write(str(datetime.now()))

            file.write("\nTotal Items: ")
            file.write(str(count))

            file.write("\nBackup Status: Successful\n")
            file.write("--------------------------\n")

        print("Backup Completed Successfully!")
        print("Total Items:", count)
        print("Backup History Saved!")

    else:
        print("Source Folder Not Found!")