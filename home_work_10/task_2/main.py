from writing_to_files import csv_converter, json_converter, pickle_converter
from path_converter_to_dictionary import ConverterPath


path = '/home/nikolay/PycharmProjects/Python_home_works'
data = ConverterPath.directory_bypass(path)

json_converter.JsonConverter.create_json(data, 'result.json')
csv_converter.CvsConverter.create_csv(data, 'result.csv')
pickle_converter.PickleConverter.create_pickle(data, 'result.pickle')
