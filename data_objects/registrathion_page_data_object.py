from dataclasses import dataclass
from enum import Enum


class Gender(Enum):
    Female = 'Female'
    Male = 'Male'
    Other = 'Other'

class Month(Enum):
    January = 0
    February = 1
    March = 2
    April = 3
    May = 4
    June = 5
    July = 6
    August = 7
    September = 8
    October  = 9
    November = 10
    December = 11

@dataclass
class UserData:
    first_name: str
    last_name: str
    email: str
    gender: Gender
    pnone_number: str
    birth_day: int
    birth_month: Month
    birth_year: int
    subjects: list
    hobbies: list
    file_name: str
    address: str
    state: str
    sity: str
