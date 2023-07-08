"""
The module takes a list of dictionaries and writes it to a pickle file
"""
import pickle


def create_pickle(data, file):
    with open(file, 'wb') as f:
        pickle.dump(data, f)
