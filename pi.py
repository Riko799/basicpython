text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO

words = text.replace(",", "").split()
word_lengths = [str(len(word)) for word in words]
result_string = ''.join(word_lengths)

print(result_string)


