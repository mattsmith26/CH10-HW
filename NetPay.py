import EmployeeClass as c
import PayrollDeductionClass as p
from tabulate import tabulate

employee1 = c.Employee("Jimmy Smith", "58475", "Information Systems", "Develor", "6800")

info = {"Description": ["food court", "gift contribution", "vending machine"],
        "Date": ["8/14/2022", "8/12/2022", "8/17/2022","8/22/2022", "8/5/2022"],
        "Charge_Amount": ["22.50", "25.00", "15.25","3.00","2.75"],
        "ID": ["39119","58475","21547"]

}


payded1 = p.PayrollDeduction(info["Description"][0], info["Date"][0], info["Charge_Amount"][0], info["ID"][0])
payded2 = p.PayrollDeduction(info["Description"][1], info["Date"][1], info["Charge_Amount"][1], info["ID"][1])
payded3 = p.PayrollDeduction(info["Description"][0], info["Date"][2], info["Charge_Amount"][2], info["ID"][2])
payded4 = p.PayrollDeduction(info["Description"][2], info["Date"][3], info["Charge_Amount"][3], info["ID"][1])
payded5 = p.PayrollDeduction(info["Description"][2], info["Date"][4], info["Charge_Amount"][4], info["ID"][1])



table1 = [["Name", "ID Number", "Department","Job Title","Monthly Salary"],
            ["Jimmy Smith", "58475","Information Systems", "Developer","6800"]
]

table2 = [["Description", "Date", "Charge Amount", "Job Title", "ID Number"],
            ["food court", "8/14/2022", "22.50", "39119"]


]

print(tabulate(table1, headers="firstrow", tablefmt="fancy_grid"))
print(tabulate(table2, headers= "firstrow", tablefmt="fancy_grid"))


print("*** Employee Pay ***")
print("Name: ", employee1.get_name())
print("ID Number: ", employee1.get_id())
print("Department: ", employee1.get_department())
print("Gross Pay: ", "${:,.2f}".format(float(employee1.get_monthly_salary())))
print("Net Pay: ", "${:,.2f}".format((float(employee1.get_monthly_salary()))) - (float(payded2.get_charge_amt())) - (float(payded4.get_charge_amt()))- (float(payded5.get_charge_amt))))