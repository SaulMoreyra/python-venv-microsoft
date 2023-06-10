from time import sleep

countdown = [4, 3, 2, 1, 0]

# for number in countdown:
#     print(number)
#     # sleep(1)  # Wait 1 second
# print("Blast off!! 🚀")

array_of_tuplas = [(10, 9), (8, 7), (6, 5), (4, 3), (2, 1)]
for left, right in array_of_tuplas:
    print(f"Left: {left}, Right: {right}")


array_of_arrays = [[1, 1], [4, 5], [6, 2]]
for [left, right] in array_of_arrays:
    print(f"Left: {left}, Right: {right}")


numeros = [1, 2, 3]

a, b, c = numeros

print(a)  # Salida: 1
print(b)  # Salida: 2
print(c)  # Salida: 3
