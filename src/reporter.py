class DataFrameReporter:
    def __init__(self, float_format='0.05f', percent_format='0.02%', include_all=False):
        self.float_format = float_format
        self.percent_format = percent_format
        self.include_all = include_all

    # добавьте в класс метод show_report
    def show_report(self, df, title=None):
        if title != None:
            print(title)
        else:
            pass
        return f"Количество столбцов: {df.shape[1]}\nКоличество строк: {df.shape[0]}\nКоличество дубликатов: {df.duplicated().sum()}\nДоля дубликатов: {format(df.duplicated().sum() / df.shape[0], '0.02%')}"
