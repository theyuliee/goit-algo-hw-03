from datetime import datetime
def get_days_from_today(date: str) -> int:
    try:
        date = datetime.strptime(date, '%Y-%m-%d').date()
        today = datetime.today().date()
        diff_date = today - date
        return diff_date.days
    except ValueError :
        return 'Неправильний формат дати. '

print(get_days_from_today('2024-09-20'))