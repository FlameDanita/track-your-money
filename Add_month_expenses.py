from track_your_money import money_tracker_month

month = money_tracker_month()

print('Current date:', month.day, month.month_name, month.year, sep=' ')
print()
# first.create_xlsx(filename='Сентябрь_2023.xlsx')
# first.write_xlsx()

month.read_xlsx()
month.get_expenses_group()

month.add_expenses_auto()
month.write_xlsx()

month.table.tail()