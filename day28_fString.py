# without f string we to format string as shown under
letter = "My name is {} and I am from {}"
name = "Atta"
country = "Pakistan"
print(letter.format(name, country))
print(
    letter.format(country, name)
)  # this is drawback we have to keep in mind the correct order of format arguments in order to get desired output, which make it in convenient

# so python introduce f strings

letter = f"We use f string like this: My name is {{name}} and i am from {{country}}"
print(letter)

letter = f"My name is {name} and i am from {country}"
print(letter)

price = 49.999999
txt = f"For Only {price:.2f} Dollars!"
print(txt)
