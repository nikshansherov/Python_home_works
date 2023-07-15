import csv
import random


def get_subjects(file):
    with open(file, 'r', encoding='utf-8') as f:
        file = csv.reader(f)
        for subjects in file:
            return subjects


LIST_SUBJECTS = get_subjects('subjects.csv')


class FormatCheck:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def validate(self, value):
        if not value.isalpha():
            raise TypeError(f'Значение {value} должно быть текстом!')


class SubjectsCheck:
    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)

    def __set__(self, instance, value):
        for i in value:
            if not LIST_SUBJECTS.count(i):
                raise ValueError(f'Предмет {i} не входит в изучаемые студентами')
            else:
                setattr(instance, self.param_name, value)


class Student:
    name = FormatCheck()
    last_name = FormatCheck()
    patronymic = FormatCheck()
    subjects = SubjectsCheck()
    NUMBER_OF_SUBJECT_GRADES = 5

    def __init__(self, last_name, name, patronymic, subjects):
        self.name = name.capitalize()
        self.last_name = last_name.capitalize()
        self.patronymic = patronymic.capitalize()
        self.subjects = subjects
        self.assessments_dict = self.create_rating_dict(2, 5, 'оценки')
        self.tests_dict = self.create_rating_dict(1, 100, 'баллы по тестам')

    def create_rating_dict(self, min_rand, max_rand, name_key):
        rat_dict = {}
        sum_average_score = 0
        for sub in self.subjects:
            lst = []
            dict_sub = {}
            sum = 0
            for i in range(self.NUMBER_OF_SUBJECT_GRADES):
                ran = random.randint(min_rand, max_rand)
                sum += ran
                lst.append(ran)
            dict_sub[name_key] = lst
            average_score = sum / self.NUMBER_OF_SUBJECT_GRADES
            dict_sub['средний бал'] = average_score
            sum_average_score += average_score
            rat_dict[sub] = dict_sub
        rat_dict['средний бал по всем предметам'] = round(sum_average_score / len(self.subjects), 2)
        return rat_dict


subjects_1 = ['математика', 'философия']
st_1 = Student('антонов', 'антон', 'Антонович', subjects_1)

subjects_2 = ['политология', 'физика']
st_2 = Student('иванов', 'Иван', 'иванович', subjects_2)

print(f'Студент {st_1.last_name} {st_1.name} {st_1.patronymic} \nрейтинг оценок: {st_1.assessments_dict} \n'
      f'рейтинг тестов: {st_1.tests_dict}')
print(f'Студент {st_2.last_name} {st_2.name} {st_1.patronymic} \nрейтинг оценок: {st_2.assessments_dict} \n'
      f'рейтинг тестов: {st_2.tests_dict}')
