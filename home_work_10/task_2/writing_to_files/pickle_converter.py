"""
The module takes a list of dictionaries and writes it to a pickle file
"""
import pickle


class PickleConverter:
    def __init__(self, data, file):
        self.data = data
        self.file = file

    def create_pickle(data, file):
        with open(file, 'wb') as f:
            pickle.dump(data, f)
