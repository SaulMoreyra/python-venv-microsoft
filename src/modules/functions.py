# INFO: None is similar to void in functions
from datetime import timedelta, datetime


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


# INFO: call only one parameter
print(distance_from_earth("Moon"))
print(distance_from_earth("Saturn"))

# INFO: call only one parameter by name
print(distance_from_earth(destination="Neptune"))


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24


# INFO: call multiple parameters by orden
print(days_to_complete(238855, 75))
print(round(days_to_complete(238855, 75)))

# INFO: call multiple parameters by name
print(days_to_complete(distance=200, speed=200))
print(days_to_complete(speed=200, distance=2000))


# INFO: Using default args (js same)
def arrival_time(hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime("Arrival: %A %H:%M")


print(arrival_time())
print(arrival_time(hours=0))


# INFO: usigin default parameter for only one param
def arrival_time_2(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")


print(arrival_time_2("Moon"))
print(arrival_time_2(destination="Moon"))
print(arrival_time_2("Orbit", hours=1.2))
print(arrival_time_2(destination="Orbit", hours=1.2))


def variable_length(*args):
    print(args)


variable_length("one", "two")


def sequence_time(*args):  # PARAMS AS AN ARRAY
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"


print(sequence_time(4, 14, 18))


def variable_length_object(**kwargs):  # PARAMS AS AN DICTIONARY OBJECT
    print(kwargs)


variable_length_object(tanks=1, day="Wednesday", pilots=3)


def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission:")
    for title, name in kwargs.items():
        print(f"{title}: {name}")


# INFO: no es posile pasar un parametro con el mismo nombre
print(crew_members(captain="Neil Armstrong",
      pilot="Buzz Aldrin", command_pilot="Michael Collins"))
