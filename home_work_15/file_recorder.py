import logging
from time import asctime


def create_csv(data, file):
    logging.basicConfig(filename=file, filemode='w',
                        encoding='utf-8', level=logging.INFO)
    logging.info(asctime())
    for obj in data:
        logging.info(f' объект - {obj.name}, расширение файла - {obj.file_extension}, '
                     f'тип объекта - {obj.type}, родитель - {obj.parent}')
