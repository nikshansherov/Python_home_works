from writing_to_files import csv_converter, json_converter, pickle_converter
from path_converter_to_dictionary import directory_bypass


path = '/home/nikolay/PycharmProjects/Python_home_works'
data = directory_bypass(path)

json_converter.create_json(data, 'result.json')
csv_converter.create_csv(data, 'result.csv')
pickle_converter.create_pickle(data, 'result.pickle')
