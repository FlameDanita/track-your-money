import pandas as pd
import datetime

class money_tracker_month:
    def __init__(self, month_number=datetime.date.today().month):
        self.day = datetime.date.today().day
        self.month_number = month_number
        self.year = datetime.date.today().year
        self.num_to_month = {
            1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель', 5: 'Май', 6: 'Июнь',
            7: 'Июль', 8: 'Август', 9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь' }
        self.month_name = self.num_to_month[month_number]
        self.date = datetime.datetime(day=self.day, month=self.month_number, year=self.year)

        self.table = pd.DataFrame({'дата': [], 'категория': [], 'сумма': [], 'комментарий': []})
        self.table_name = str(self.month_name)+'_'+str(self.year)+'.xlsx'

        self.expenses_group =  {1: 'продукты',
                               2: 'транспорт',
                               3: 'развлечения',
                               4: 'здоровье',
                               5: 'связь',
                               6: 'квартплата',
                               7: 'непредвиденное',
                               8: 'одежда',
                               9: 'цифровые',
                               10: 'ненужные',
                               11: 'прочее'}
        
        self.gain_group = {100: 'зарплата',
                           101: 'подработка',
                           102: 'дивиденды',
                           103: 'депозиты'}

    def create_xlsx(self, filename=None):
        if filename == None:
            self.table.to_excel(self.table_name, index=0)
        else:
            self.table_name = filename
            self.table.to_excel(filename, index=0)

    def read_xlsx(self, filename=None):
        if filename == None:
            self.table = pd.read_excel(self.table_name)
        else:
            self.table_name = filename
            self.table = pd.read_excel(filename)

            self.month_name = filename.split('_')[0]
            for key, value in self.num_to_month.items():
                if self.month_name == value:
                    self.month_number = key
            self.year = int(filename.split('_')[1].split('.')[0])

            self.date = datetime.datetime(day=self.day, month=self.month_number, year=self.year)

    def write_xlsx(self):
        self.table.to_excel(self.table_name, index=0)

    def get_expenses_group(self):
        print('Группы расходов:')
        for key, value in self.expenses_group.items():
            print("{:>2}".format(key), end='|')
            print("{:<15}".format(value)+'|')
        print()

        print('Группы доходов:')
        for key, value in self.gain_group.items():
            print("{:>2}".format(key), end='|')
            print("{:<15}".format(value)+'|')
        print()

    def add_expenses_manual(self, date=0, category='прочее', value=0,  comment=''):
        self.table.loc[len(self.table)] = [date, category, value, comment]

    def add_expenses_auto(self):
        flag = True
        month_num = "{:>02d}".format(self.month_number)
        while True:
            date = "{:>02d}".format(int(input('Дата = '))) + '.' + month_num + '.' + str(self.year)

            num_category = int(input('Категория = '))

            cost = int(input('Сумма = '))
            if num_category in self.expenses_group.keys():
                self.table.loc[len(self.table)] = [date, self.expenses_group[num_category], -cost, str(input('Комментарий = '))]
            elif num_category in self.gain_group.keys():
                self.table.loc[len(self.table)] = [date, self.gain_group[num_category], cost, str(input('Комментарий = '))]
            else:
                pass
                # добавить ошибку ввода

            if str(input('Продолжить?[Y/n]')) == 'n':
                break

