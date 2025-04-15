import datetime as dt
from typing import Optional

class Calculator:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.records = []

    def add_record(self, record):
        """Cохраняет новую запись о расходах или приеме пищи"""
        self.records.append(record)

    def get_today_stats(self):
        """Считает сколько потрачено сегодня"""
        today = dt.datetime.now().date()
        return sum(r.amount for r in self.records if r.date == today)

    def get_week_stats(self):
        """Считает сколько потрачено за последнюю неделю"""
        today = dt.datetime.now().date()
        week_ago = today - dt.timedelta(days=6)
        return sum(r.amount for r in self.records if week_ago <= r.date <= today)


class CashCalculator(Calculator):
    """Калькулятор денег"""



    def get_today_cash_remained(self, currency):
        """Определяе сколько денег можно потратить сегодня в рублях, долларах или евро"""

        self.USD_RATE = 84.38
        self.EUR_RATE = 93.16
        today_spent = self.get_today_stats()  # сколько потрачено сегодня
        remained = self.limit - today_spent  # сколько осталось

        if remained == 0:
            return f'Денег нет, держись'

        currency_info = {
            'rub': (1, 'руб'),
            'usd': (self.USD_RATE, 'USD'),
            'eur': (self.EUR_RATE, 'Euro')
        }

        if currency not in currency_info:
            return 'Неизвестная валюта'

        rate, name = currency_info[currency]
        cash_abs = abs(remained) / rate
        cash_rounded = round(cash_abs, 2)

        if remained > 0:
            return f'На сегодня осталось {cash_rounded:.2f} {name}'
        else:
            return f'Денег нет, держись: твой долг - {cash_rounded:.2f} {name}'


class CaloriesCalculator(Calculator):
    """Калькулятор калорий"""

    def get_calories_remained(self):
        """Определяет сколько калорий можно получить сегодня"""
        today_spent = self.get_today_stats()
        remained = self.limit - today_spent

        if remained > 0:
            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remained} кКал'
        else:
            return 'Хватит есть!'


class Record:
    def __init__(self,amount: int, comment: str, date: Optional[str] = None) -> None:
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()




if __name__ == '__main__':



    # r1 = Record(amount=145, comment='Безудержный шопинг', date='08.03.2019')
    # r2 = Record(amount=1568, comment='Наполнение потребительской корзины', date='09.03.2019')
    # r3 = Record(amount=691, comment='Катание на такси', date='08.03.2019')

    # r4 = Record(amount=1186, comment='Кусок тортика. И ещё один', date='24.02.2019')
    # r5 = Record(amount=84, comment='Йогурт', date='23.02.2019')
    # r6 = Record(amount=1140, comment='Баночка чипсов', date='24.02.2019')

    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(145, 'кофе'))
    cash_calculator.add_record(Record(300, 'обед'))
    cash_calculator.add_record(Record(3000, 'бар', '01.04.2025'))

    print(cash_calculator.get_today_cash_remained('rub'))

    cal_calculator = CaloriesCalculator(2000)
    cal_calculator.add_record(Record(1500, 'обед'))
    cal_calculator.add_record(Record(500, 'ужин'))

    print(cal_calculator.get_calories_remained())
