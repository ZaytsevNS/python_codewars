# Solution for task: https://www.codewars.com/kata/5885b5d2b632089dc30000cc/

from datetime import datetime


def day_of_week(date: str) -> str:
    """ This function takes an date in format d/m/Y(String) and return what day of the week it was(String) """
    return datetime.strptime(date, '%d/%m/%Y').strftime('%A')
