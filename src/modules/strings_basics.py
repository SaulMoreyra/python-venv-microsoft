separator = "___________________________________________\n"

# print
fact = "The Moon has no atmosphere."
print(fact)  # "The Moon has no atmosphere."
print(separator)

# INFO: the string are inmutables
fact1 = "The Moon has no atmosphere."
fact1 + "No sound can be heard on the Moon."
print(fact)  # "The Moon has no atmosphere."
print(separator)

# INFO: to concat another string is necesary create anothes var
fact2 = "The Moon has no atmosphere."
two_facts = fact2 + "No sound can be heard on the Moon."
print(two_facts)
print(separator)

# INFO: sigle ' when you need use inside double"
print('The "near side" is the part of the Moon that faces the Earth.')
print(separator)

# INFO: double " when you need use inside single '
print("We only see about 60% of the Moon's surface.")
print(separator)

# INFO: triple double " when you need to mix inside double and single
print("""We only see about 60% of the Moon's surface, this is known as the "near side".""")
print(separator)

# INFO: multiline
multiline = "Facts about the Moon:\n There is no atmosphere.\n There is no sound."
print(multiline)
print(separator)


multiline1 = """Facts about the Moon: \n There is no atmosphere. \n There is no sound."""
print(multiline1)
print(separator)
