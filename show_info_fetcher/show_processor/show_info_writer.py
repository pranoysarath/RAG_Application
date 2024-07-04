import json
import os
import time

from RAG.show_info_fetcher.fetch_api.tv_maze_api import TVMazeInfoFetcher


class ShowInfoWriter:

    def __init__(self):
        directory = os.path.dirname(__file__)
        self.target_folder = os.path.join(directory, '../data_files', 'to_be_processed', 'shows')
        self.source_folder = os.path.join(directory, '../data_files', 'to_be_processed', 'show_mappings.json')
        self.show_info_to_retrieve = self.get_show_ids(self.source_folder)


    def get_show_ids(self, file_path):

        with open(file_path) as file:
            show_mapping = file.read()
        return json.loads(show_mapping)

    def get_new_show_info(self):

        for show_name,show_id in self.show_info_to_retrieve.items():

            with open(os.path.join(self.target_folder, show_name), 'w') as file:
                file.write(json.dumps(TVMazeInfoFetcher.fetch_episode_info(show_id)))
            time.sleep(1)



# ShowInfoWriter().get_new_show_info()





