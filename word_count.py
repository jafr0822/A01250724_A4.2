"""Actividad 4.2 Ejercicio 3 - A01250724"""

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

parsed_words = []

for i, line in enumerate(text_lines):
    parsed_words.append(line.strip())

    # print(f"Valor invalido: {line} en linea {i+1}")


# Count words

frequency = {}

for word in parsed_words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1


# Elapsed time calculation
final_timestamp = time.time()
elapsed_time = final_timestamp - initial_timestamp


# Results compilation

results = [
    f"Elapsed Time: {elapsed_time}",
]


# Outputting results to terminal and file

with open("WordCountResults.txt", "w", encoding="utf-8") as results_file:
    for result in results:
        results_file.write(result + "\n")
        print(result)

    HEADER = "Word\tCount"
    results_file.write(HEADER + "\n")
    print(HEADER)

    for word, count in frequency.items():
        word_count = f"{word}\t{count}"
        results_file.write(word_count + "\n")
        print(word_count)
