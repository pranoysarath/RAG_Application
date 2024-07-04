import os
import shutil


class ShowCleanup:

    def __init__(self):
        directory = os.path.dirname(os.path.dirname(__file__))
        self.target_folder = os.path.join(directory, 'data_files', 'processed')
        self.source_folder = os.path.join(directory, 'data_files', 'to_be_processed')


    def cleanup(self):
        self.backup_show_info()

    def backup_show_info(self):

        try:
            for file_name in os.listdir(os.path.join(self.source_folder, 'shows')):

                src_file_path = os.path.join(self.source_folder, 'shows', file_name)
                ds_file_path = os.path.join(self.target_folder, 'shows', file_name)
                shutil.move(src_file_path, ds_file_path)

            # removing the processed shows
            src_file_path = os.path.join(self.source_folder, 'show_mappings.json')
            open(src_file_path, "w").close()

        except Exception as e:
            print(f"Exception occurred during cleanup {e}")

# ShowCleanup().cleanup()