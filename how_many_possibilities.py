from itertools import product

correct_lp = "14B378[IR22]"
pattern = "1#B3#8[IR2#]" # Shitty LP :D :))

combinations = product("0123456789", repeat=pattern.count('#'))
possibilities = [pattern.replace("#", "{}").format(*combo) for combo in combinations]

# Find the correct prediction's index
correct_index = possibilities.index(correct_lp) + 1  # Adding 1 to match human counting

print(f"There is {len(possibilities)} possibilities for this LP")
print(f"Correct prediction found at number: {correct_index}")