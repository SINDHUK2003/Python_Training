import keyword
from collections import defaultdict as dd

input_file = 'Day3/Input.txt'
output_file = 'Day3/Output.txt'

predefined_keywords = keyword.kwlist
print(predefined_keywords)
Hash = dd(int)

try:
    with open(input_file, 'r') as file:
        for line in file:
            line = line.replace(",", " ").replace(".", " ")
            for x in line.lower().split():
                if x in predefined_keywords:
                    Hash[x] += 1

    with open(output_file, 'w') as out:
        for x in predefined_keywords:
            out.write(f"{x} : {Hash[x]}\n")

except FileNotFoundError:
    print("File Not Found")

finally:
    print("Log analysis completed")

