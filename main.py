import pandas
from datetime import datetime
from application.db.people import Employee
from application.sallary import calculate_salary

if __name__ == '__main__':
    emp_1 = Employee('Alex', 'Bogatyrev')
    sal = calculate_salary(6000)
    date_now = datetime.now()
    print(f'У {emp_1.name} {emp_1.surname} зарплата {sal}руб. в месяц')
    print(date_now)
   
    


