
camelCase = input("camelCase: ")
snake_case = ""

# characters in camelCase 
for char in camelCase:
    # If characters is upper 
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char

# Output snake_case
print(f"snake_case: {snake_case}")