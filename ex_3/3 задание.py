import pandas as pd

PATH_DEPARTMENTS = '../data/задача 3/departments.csv'
PATH_OPERATIONS = '../data/задача 3/operations.csv'


def get_pivot(path_departments, path_operations) -> pd.DataFrame:
    """Возвращает сводную по месяцам для операций по департаментам"""

    # Считываем
    df_departments = pd.read_csv(path_departments)
    df_operations = pd.read_csv(path_operations)

    # Объединяем в таблицу с наименованием департамента
    df = pd.merge(df_operations, df_departments, how='left', left_on='department_id', right_on='id')
    df = df[(df['month'] <= 12) & (df['day'] <= 31)]
    select_columns = ['year', 'month', 'day', 'name', 'income']
    df = df[select_columns]

    # Получаем сводную таблицу по месяцам отделов
    pivot_df = df.pivot_table(values='income', index=['year', 'month'], columns='name', aggfunc='sum', fill_value=0)
    pivot_df = pivot_df.reset_index().rename_axis(None, axis=1)

    # Подготовка под формат
    columns = ['year', 'month', 'department', 'income']
    result_df = pd.DataFrame(columns=columns)
    len_pivot = len(pivot_df)
    for name in pivot_df.columns[2:]:
        year = pivot_df.year.values
        month = pivot_df.month.values
        department_name = len_pivot * [name]
        income = pivot_df[name]

        add_df = pd.DataFrame(dict(zip(columns, [year, month, department_name, income])))
        add_df = add_df.groupby('year'). \
            filter(lambda x: (x['income'] > 0).all())  # убираем значения простая отдела в течение года
        result_df = pd.concat([result_df, add_df])
    result_df = result_df.sort_values(['year', 'month', 'department'])

    return result_df


if __name__ == '__main__':
    df = get_pivot(PATH_DEPARTMENTS, PATH_OPERATIONS)
    df.to_csv('3_ex__result.csv', index=False)
