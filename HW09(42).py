# Задача 42: 
# Узнать какая максимальная households в зоне минимального значения population.

df[df['population']==df['population'].min()]['households'].max()

# 4.0