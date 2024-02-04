"""Actividad 4.2 Ejercicio 2 - A01250724"""

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
    try:
        parsed_numbers.append(int(line))
    except ValueError:
        print(f"Valor invalido: {line} en linea {i+1}")


bin_numbers = []
hex_numbers = []

for decimal_number in parsed_numbers:

    decimal_number_bk = decimal_number

    # Zero case

    if decimal_number == 0:
        bin_numbers.append("0")
        hex_numbers.append("0")
        continue


    # Negative check

    is_negative = False
    if decimal_number < 0:
        is_negative = True
        decimal_number = abs(decimal_number)

    # Binary conversion

    binary_digits = []
    while decimal_number > 0:
        binary_digits.insert(0, int(decimal_number) % 2)
        decimal_number //= 2

    if is_negative:
        # Flipping the bits
        for i, binary_digit in enumerate(binary_digits):
            if binary_digit==1:
                binary_digits[i] = 0
            else:
                binary_digits[i] = 1

        # Adding 1 to the lowest bit
        for i in range(-1, (len(binary_digits)*-1)-1, -1):
            if binary_digits[i]==0:
                binary_digits[i] = 1
                break
            else:
                binary_digits[i] = 0

        unpadded_neg_number = "".join(map(str, binary_digits))
        hex_padded_neg_number = "1" * (4 - len(unpadded_neg_number) % 4) + unpadded_neg_number
        print(unpadded_neg_number, hex_padded_neg_number)

        # Padding with 1's until it gets to 10 digits
        for i in range(0, 10-len(binary_digits)):
            binary_digits.insert(0, "1")

    bin_numbers.append("".join(map(str, binary_digits)))


    # Hexadecimal conversion

    hexadecimal_digits = []
    hex_map = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }

    if is_negative:
        decimal_number = 0
        for digit in hex_padded_neg_number:
            decimal_number = decimal_number *2 + int(digit)

    else:
        decimal_number = decimal_number_bk

    while decimal_number > 0:
        remainder = int(decimal_number) % 16
        if remainder >= 10:
            hexadecimal_digits.insert(0, hex_map[remainder])
        else:
            hexadecimal_digits.insert(0, str(remainder))
        decimal_number //= 16

    if is_negative:
        # Padding with F's until it gets to 10 digits
        for i in range(0, 10-len(hexadecimal_digits)):
            hexadecimal_digits.insert(0, "F")

    hex_numbers.append("".join(hexadecimal_digits))


# Elapsed time calculation

final_timestamp = time.time()
elapsed_time = final_timestamp - initial_timestamp


# Results compilation

results = [
    f"Elapsed Time: {elapsed_time}",
]


# Outputting results to terminal and file

with open("ConversionResults.txt", "w", encoding="utf-8") as results_file:
    for result in results:
        results_file.write(result + "\n")
        print(result)

    HEADER = "DEC\tBIN\tHEX"
    results_file.write(HEADER + "\n")
    print(HEADER)

    for i, dec_number in enumerate(parsed_numbers):
        bin_number = bin_numbers[i]
        hex_number = hex_numbers[i]

        conversion_result = f"{dec_number}\t{bin_number}\t{hex_number}\t"
        results_file.write(conversion_result + "\n")
        print(conversion_result)
