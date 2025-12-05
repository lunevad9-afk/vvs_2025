import pandas as pd
import numpy as np

df = pd.read_csv('tested.csv')
print("вывод количества нулевых элементов столбцов")
print(df.isnull().sum(), "\n")
print("вывод типа данных столбцов")
print(df.dtypes, "\n")
n=input("Ввод количества строк для вывода: ")
n = int(n) 
print(df.head(n), "\n")
print("вывод статистики по столцбу Age")
statistics = df['Age'].describe()
print(statistics, "\n")

col_strok = df.shape[0]
print(f"Количество строк: {col_strok}")

col_headers = len(df.columns)
print("Количество заголовков:", col_headers, "\n")

median_value = df['Age'].median()
df['Age'] = df['Age'].fillna(median_value)
print(df["Age"], "\n")

#удаление 20 любых строк с нулевым 
indices_to_drop = np.random.choice(df.index, 20, replace=False)
df_dropped = df.drop(indices_to_drop)

#cравнение
survived = df['Survived'].values
sex = df['Sex'].values
age = df['Age'].values
is_male = (sex == 'male')
is_female = (sex == 'female')


male_survived_rate = np.mean(survived[is_male]) * 100
female_survived_rate = np.mean(survived[is_female]) * 100
print(f"Процент выживших: Мужчины = {male_survived_rate:.2f}%, Женщины = {female_survived_rate:.2f}%\n")


male_mean_age = np.nanmean(age[is_male])
female_mean_age = np.nanmean(age[is_female])
print(f"Средний возраст: Мужчины = {male_mean_age:.2f}, Женщины = {female_mean_age:.2f}\n")


male_survived_age = np.nanmean(age[is_male & (survived == 1)])
male_dead_age = np.nanmean(age[is_male & (survived == 0)])
female_survived_age = np.nanmean(age[is_female & (survived == 1)])
female_dead_age = np.nanmean(age[is_female & (survived == 0)])
print(f"Мужчины: выжившие = {male_survived_age:.2f}, погибшие = {male_dead_age:.2f}")
print(f"Женщины: выжившие = {female_survived_age:.2f}, погибшие = {female_dead_age:.2f}\n")


filter_a = df[(df['Age'] > 30) & (df['Sex'] == 'male') & (df['Pclass'] == 1)]
filter_b = df[((df['Age'] < 18) | (df['Sex'] == 'female')) & (df['Survived'] == 1)]
print(f">30 лет, мужчины, 1-й класс: {len(filter_a)} пассажиров")
print(filter_a, "\n")
print(f"\nb. <18 лет ИЛИ женщины, выжившие: {len(filter_b)} пассажиров")
print(filter_b, "\n")


# Создаем сводную таблицу
pivot_table = df.pivot_table(
    index=['Pclass', 'Sex'],
    values=['Age', 'Survived', 'Fare'],
    aggfunc={
        'Age': 'mean',
        'Survived': 'mean',
        'Fare': 'mean'
    }
).round(2)

# Добавляем количество пассажиров в каждой группе
counts = df.groupby(['Pclass', 'Sex']).size()
pivot_table['Количество'] = counts
pivot_table['доля-выживших_%'] = (pivot_table['Survived'] * 100).round(1)

# Переименовываем столбцы
pivot_table = pivot_table.rename(columns={
    'Age': 'средний-возраст',
    'Fare': 'Средняя-цена-билета',
    'Survived': 'Джившихоля_вы'
})

# Выводим только подходящие столбцы в верном порядке
result_table = pivot_table[['средний-возраст', 'доля-выживших_%', 'Средняя-цена-билета', 'Количество']]
print(result_table.to_string())