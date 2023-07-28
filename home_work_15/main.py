import argparse
from file_recorder import create_csv
from path_converter_to_dictionary import directory_bypass


parser = argparse.ArgumentParser()
parser.add_argument('path', metavar='P', type=str)
# path = '/home/nikolay/PycharmProjects/Python_home_works'
args = parser.parse_args()
data = directory_bypass(args.path)
create_csv(data, 'result.csv')
