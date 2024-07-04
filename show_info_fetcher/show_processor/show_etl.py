import os
import json
import traceback

import requests




class ShowETL:

    def __init__(self):
        self.directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.files_directory = os.path.join(self.directory, "data_files", "to_be_processed", 'shows')

        # make it configurable
        self.retriever_base_url = "http://127.0.0.1:5000"
        self.retriever_base_add_document_end_point = f"{self.retriever_base_url}/retriever/add_documents"


    def process_data(self):

        for file_name in os.listdir(self.files_directory):
            file_path = os.path.join(self.files_directory, file_name)


            with open(file_path) as file:
                self.format_data_and_send(json.loads(file.read()))


    def format_data_and_send(self, data):

    #     get show information
        show_name = data[0]['_links']['show']['name']

        documents = []
        for index, episode in enumerate(data):
            episode_name = episode['name']
            episode_airdate = episode['airdate']
            episode_rating = episode['rating']['average']
            episode_summary = episode['summary']
            episode_number = episode['number']

            document = f"The  summary of the episode {episode_number} named {episode_name} of the show {show_name} is {episode_summary}. It aired on {episode_airdate} and had a rating of {episode_rating}"
            documents.append(document)
        print(f"Sending Episodes of {show_name}")
        self.send_document_to_retriever(documents)








    def send_document_to_retriever(self, documents):

        try:
            requests.post(self.retriever_base_add_document_end_point, json = documents)
        except Exception as e:
            print(f"Exception occured while sending documents to the retriever {e}")
            print(traceback.format_exc())

