from math import ceil, floor
separator = "___________________________________________\n"

sum = 30 + 12
print(sum)
print(separator)

difference = 30 - 12
print(difference)
print(separator)

product = 30 * 12
print(product)
print(separator)

quotient = 30 / 12
print(quotient)
print(separator)

# INFO: division by inferior number (rounds the division to down) using //
print(1042 / 60)  # 17.366666666666667
print(1042 // 60)  # 17
print(separator)

# INFO: operations order
module = 1042 % 60
print(module)
print(separator)

result_1 = 1032 + 26 * 2
print(result_1)

result_2 = 1032 + (26 * 2)
print(result_2)

result_3 = (1032 + 26) * 2
print(result_3)
print(separator)


# INFO: convert strings into numbers
demo_int = int('215')
print(demo_int)

demo_float = float('215.3')
print(demo_float)
print(separator)


# INFO: absolute values
print(39 - 16)
print(16 - 39)
print(abs(39 - 16))
print(abs(16 - 39))
print(separator)

print(round(14.4))
print(round(14.6))


round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
