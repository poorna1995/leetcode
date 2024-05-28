heros = ["spider man", "thor", "hulk", "iron man", "captain america"]

# heros.append("black panther")

# heros.insert(3, "black panther")

# heros[1:3] = ["doctor strange"]
# print(heros)


# Length of the list
# 2. Add 'black panther' at the end of this list
# 3. You realize that you need to add 'black panther' after 'hulk',
#    so remove it from the list first and then add it after 'hulk'
# 4. Now you don't like thor and hulk because they get angry easily :)
#    So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
#    Do that with one line of code.
# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)


class solution:
    def length(self, heros):
        return len(heros)


print(solution().length(heros))


class solution:
    def add_string(self, heros):
        heros.append("black panther")
        return heros


print(solution().add_string(heros))


class solution:
    def remove_string(self, heros):
        heros.remove("black panther")
        heros.insert(3, "black panther")
        return heros


print(solution().remove_string(heros))


class solution:
    def replace(self, heros):
        heros[1:3] = ["doctor strange"]
        return heros


print(solution().replace(heros))


class solution:
    def sorting(self, heros):
        heros.sort()
        return heros


print(solution().sorting(heros))
