class Employee:

    def __init__(self, name):
        self.name = name
        self.job_title = ""
        self.employment_start_date = ""
    
class Company:

    def __init__(self, business_name, address, industry_type):
        self.business_name = business_name
        self.address = address
        self.industry_type = industry_type
        self.employee_list = list()
        
    def description(self):
        employee_list_string = ""
        for employee in self.employee_list:
            employee_list_string += f'\n\t* {employee.name}'
        return print(f'{self.business_name} is in the business of {self.industry_type} and has the following employees {employee_list_string}')

netflix = Company('Netflix', '201 Barrett Pkwy', 'entertainment')
hulu = Company('Hulu', '482 Main St', 'entertainment')

employee_1 = Employee('Chase')
employee_2 = Employee('Corri')
employee_3 = Employee('Erin')
employee_4 = Employee('Matt')
employee_5 = Employee('Joseph')

netflix.employee_list.extend([employee_1, employee_2])
hulu.employee_list.extend([employee_3, employee_4, employee_5])

netflix.description()
hulu.description()