from datetime import date
class PayrollDeduction:
    def __init__(self,description,date,charge_amt,id):
        self.__description = description
        self.__date = date
        self.__charge_amt = charge_amt
        self.__id = id


    def get_description(self):
        return self.__description
    def get_date(self):
        return self.__date
    def get_charge_amt(self):
        return self.__charge_amt
    def get_id(self):
        return self.__id

