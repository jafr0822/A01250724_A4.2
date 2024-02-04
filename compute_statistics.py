"""Actividad 4.2 Ejercicio 1 - A01250724"""

import argparse
from pathlib import Path
import time

initial_timestamp = time.time()

parser = argparse.ArgumentParser(
    prog="A01250724 - Actividad 4.2: Ejercicio 1",
    description="Ejercicio 1 de Actividad 4.2 de Pruebas de software y aseguramiento de la calidad",
)

parser.add_argument("file_path")
args = parser.parse_args()

file_path = Path(args.file_path)

if not(file_path.exists() and file_path.is_file() and file_path.suffix==".txt"):
    raise ValueError("Ruta a archivo inválida")

with open(file_path, encoding="utf-8") as file:
    text_lines = file.readlines()

parsed_numbers = []

for i, line in enumerate(text_lines):
    if line.strip().isnumeric():
        parsed_numbers.append(float(line))
    else:
        print(f"Valor invalido: {line} en linea {i+1}")


# Mean

sum_total = 0
for number in parsed_numbers:
    sum_total += number

mean = sum_total / len(parsed_numbers)


# Median

parsed_numbers.sort()
middle_index = len(parsed_numbers) // 2

if len(parsed_numbers) % 2 == 0:
    median = (parsed_numbers[middle_index - 1] + parsed_numbers[middle_index]) / 2
else:
    median = parsed_numbers[middle_index]


# Mode

frequency = {}

for number in parsed_numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

max_frequency = max(frequency.values())
mode_values = [key for key, value in frequency.items() if value == max_frequency]


# Standard deviation and Variance

squared_diff = [(x - mean) ** 2 for x in parsed_numbers]
variance = sum(squared_diff) / len(parsed_numbers)
std_dev = variance ** 0.5


# Elapsed time calculation
final_timestamp = time.time()
elapsed_time = final_timestamp - initial_timestamp


# Results compilation

results = [
    f"Mean: {mean}",
    f"Median: {median}",
    f"Mode: {mode_values}",
    f"Variance: {variance}",
    f"Std Dev: {std_dev}",
    f"Elapsed Time: {elapsed_time}",
]


# Outputting results to terminal and file

with open("StatisticsResults.txt", "w", encoding="utf-8") as results_file:
    for result in results:
        results_file.write(result + "\n")
        print(result)
