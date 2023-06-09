separator = "___________________________________________\n"

# INFO: replace % with next variable
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." %
      mass_percentage)
print(separator)


# INFO: replace all % in the same order of next variables in tupla
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" %
      ("Moon", "Earth", "Moon", "Earth"))
print(separator)

# INFO: .format will replace {} with the first parameter
mass_percentage1 = "1/6"
print("On the Moon, you would weigh about {} of your weight on Earth.".format(
    mass_percentage1))
print(separator)

# INFO: also you can specify the position of replacer
mass_percentage2 = "1/6"
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format(
    "Moon", mass_percentage2))
print(separator)

# INFO: also you can specify the word in {} to replacer in paramters
mass_percentage3 = "1/6"
print("""You are lighter on the {moon}, because on the {moon} you would weigh about {mass} of your weight on Earth.""".format(
    moon="Moon", mass=mass_percentage3))
print(separator)

# NOTE: also exist f-strings allows code inside of a string (JS backticks)
print(
    f"On the Moon, you would weigh about {mass_percentage} of your weight on Earth.")
print(
    f"On the Moon, you would weigh about {round(100/6, 1)}% of your weight on Earth.")

subject = "interesting facts about the moon"
heading = f"{subject.title()}"
print(heading)
print(separator)
