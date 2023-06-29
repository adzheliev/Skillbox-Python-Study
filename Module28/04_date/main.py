class Date:

    def __init__(self, day: int = 0, month: int = 0, year: int = 0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return f'День: {self.day}\t Месяц: {self.month}\t Год: {self.year}'


    """Метод принимает строку и если она корректна, выдаёт строку в нужном формате"""
    @classmethod
    def from_string(cls, string_to_convert:str) -> 'Date':
        if cls.is_date_valid(string_to_convert):
            day, month, year = map(int,string_to_convert.split('-'))
            date = cls(day, month, year)
            return date

    """Медод принимает строку, проверяет её формат на корректность, а также даты на соответствие
        Учитывается количество дней в определённых месяцах, а также високосные годы"""
    @classmethod
    def is_date_valid(cls, string_to_check: str) -> bool:
        try:
            day, month, year = map(int,string_to_check.split('-'))
        except Exception:
            print('Неверный формат даты')
            return False
        if day < 1 or day > 31:
            return False
        elif month < 1 or month > 12:
            return False
        else:
            if day == 31 and month in [2, 4, 6, 9, 11]:
                return False
            else:
                if day > 29 and month == 2:
                    return False
                else:
                    if day == 29 and (year % 4 != 0 and year % 100 == 0 or year % 400 != 0):
                        return False
                    else:
                        return True


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))