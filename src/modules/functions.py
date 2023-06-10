# INFO: None is similar to void in functions
def rocket_parts():
    print("payload, propellant, structure")


def rocket_parts_1():
    return output is None


output = rocket_parts()
print(output is None)


output1 = rocket_parts_1()
print(output1 is None)


# INFO: similar to some
print(any([True, False, False]))

# INFO: numbers to string
print(str(15))


def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"


print(distance_from_earth("Moon"))
print(distance_from_earth("Saturn"))


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24


print(days_to_complete(238855, 75))
print(round(days_to_complete(238855, 75)))
