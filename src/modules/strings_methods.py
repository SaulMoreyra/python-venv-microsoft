separator = "___________________________________________\n"

# INFO: title works as a capitalice
heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)
print(separator)

# INFO: split without parameters takes space by default
temperatures = "Daylight: 260 F Nighttime: -280 F"
temperatures_list = temperatures .split()
print(temperatures_list)
print(separator)

# INFO: split by \n
temperatures1 = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list1 = temperatures1 .split('\n')
print(temperatures_list)
print(separator)

# INFO: "contains" in returns False or True
search = "Moon"
pharagraph = "This text will describe facts and challenges with space travel"
exist = search in pharagraph
print(exist)
print(separator)

pharagraph2 = "This text will describe facts about the Moon"
exist2 = search in pharagraph2
print(exist2)
print(separator)

# INFO: find will retuns first character index if doesn't exists will return -1
temperatures2 = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures2.find("Moon"))
print(temperatures2.find("Mars"))
print(temperatures2[64:64 + len("Mars")])
print(separator)

# INFO: will count how many times is repeated
"Mars"
print(temperatures2.count("Moon"))
print(temperatures2.count("Mars"))
print(separator)


# INFO: lower and upper
print("The Moon And The Earth".lower())
print("The Moon And The Earth".upper())
print(separator)


# INFO: for in using split, also isnumeric checks if string cotains a valid number
# INFO: isdecimal doesn't work with "decimals" 34.4
mars_temperature = "The highest temperature on Mars is between 30 C and 36.4 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
    elif item.isdecimal():
        print(item)
print(separator)

# INFO: endswith and startswith
if "30 C".endswith("C"):
    print("This temperature is in Celsius")
if "-30 C".startswith("-"):
    print("This temperature is to cold")
print(separator)

# INFO: replace mutate
pharagraph3 = "Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."
replaced = pharagraph3.replace("Celsius", "C")
print(replaced)
print(separator)

# INFO: join works with array of strings as a parameter
# NOTE: NO WORKS LIKE JS
# NOTE: Its necesary define firts the joiner and pass an iterable element (array)
moon_facts = ["Hello", "Earth", "and", "Mars"]
print(' '.join(moon_facts))
print('-'.join(moon_facts))
