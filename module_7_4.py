# "Форматирование строк"

team1_num = 5           # количество участников первой команды
team2_num = 6           # количество участников второй команды
score_1 = 40            # количество задач решённых командой 1
score_2 = 42            # количество задач решённых командой 2
team1_time = 1552.512   # время за которое команда 1 решила задачи
team2_time = 2153.31451  # время за которое команда 2 решила задачи
# tasks_total = 82        # количество задач
# time_avg = 45.2         # среднее время решения
# challenge_result = 'Победа команды Волшебники данных!'  # исход соревнования

# tasks_total = score_1 + score_2

time_avg = round((team1_time + team2_time)/(score_1 + score_2), 1)

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    challenge_result = 'Победа команды Мастера кода!'
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    challenge_result = 'Победа команды Волшебники Данных!'
else:
    result = 'Ничья!'


print("В команде Мастера кода участников: %s ! " % (str(team1_num)))
print("В команде Волшебники данных участников: %s ! " % (str(team2_num)))
print("Итого сегодня в командах участников: %s и %s ! " %
      ((str(team1_num)), (str(team2_num))))

print("Команда Мастера кода решила задач: {} !" .format(str(score_1)))
print("Команда Волшебники данных решила задач: {} !" .format(str(score_2)))

print("Мастера кода решили задачи за {} c !" .format(str(round(team1_time, 1))))
print("Волшебники данных решили задачи за {} c !" .format(
    str(round(team2_time, 1))))

print(f"Результат битвы: {challenge_result}!")
print(
    f"Сегодня было решено {score_1 + score_2} задач, в среднем по {time_avg} секунды на задачу!")
