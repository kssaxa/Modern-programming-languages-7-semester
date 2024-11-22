import csv
import random
from statistics import median, mean, stdev
from threading import Thread

global_data = {}


# Первая часть - заполение файлов
def recording(file):
    row = ["A", "B", "C", "D"]
    data = []
    for i in range(0, 30):  # надо 10**8
        insert = (random.choice(row), (random.uniform(1, 1000)))
        data.append(insert)

    with open(file, "w", newline="") as f:
        csv.writer(f).writerows(data)


# Вторая часть - нахождение мадианы


def median_deviation(files):
    with open(files) as file:
        data_list = [row for row in csv.reader(file)]
    data_list.sort()
    all_data = {}
    latters_list = {}
    for record in data_list:
        if record[0] not in latters_list:
            latters_list[record[0]] = []
        latters_list[record[0]].append(float(record[1]))

    for latter, number in latters_list.items():
        mediana = median(number)
        average = mean(number)
        deviation = stdev(number, average)
        all_data[latter] = [mediana, deviation]

    print(f"для файла {str(files)} \n {all_data}")


files = ["output1.csv", "output2.csv", "output3.csv", "output4.csv", "output5.csv"]
for file in files:
    recording(file)
    # median_deviation(file)

# потоки
for file in files:
    th = Thread(target=median_deviation, args=(file,))
    th.start()
# осталось найти общие медианы и отклонение
