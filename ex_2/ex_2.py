import pandas as pd

PATH = '../data/задача 2/numbers.csv'


def get_max_positive_number(values: pd.array) -> int:
    """Возвращает максмальную длину подряд идущих чисел >=0"""
    max_length, cur_length = 0, 0

    for num in values:
        if num > 0:
            cur_length += 1
            max_length = max(max_length, cur_length)
        else:
            cur_length = 0

    return max_length


if __name__ == '__main__':
    df = pd.read_csv(PATH)

    result = get_max_positive_number(df.value.values)
    pd.DataFrame({"max_length": [result]}).to_csv('numbers_out.csv', index=False)
    print(f'Ответ получен: {result}\nи сохранен в файл numbers_out.csv')

# Ответ получен: 3
# и сохранен в файл numbers_out.csv
