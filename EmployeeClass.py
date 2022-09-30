from unicodedata import name
class Employee:
    def __init__(self,name,id,department,title,monthly_salary):
        self.__name = name
        self.__id = id
        self.__department = department
        self.__title = title
        self.__monthly_salary = monthly_salary

    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_department(self):
        return self.__department
    def get_title(self):
        return self.__title
    def get_monthly_salary(self):
        return self.__monthly_salary