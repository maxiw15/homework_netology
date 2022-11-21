from application.salary import calculate_salary
from application.db.people import get_employees
from datetime import datetime
from dirty_main import *
import pandas as pd

if __name__ == '__main__':
    current_date = datetime.now().date()
    print(current_date)
    calculate_salary()
    get_employees()
    get_money()
