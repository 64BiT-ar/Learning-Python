
inp = input("camelCase: ").strip()
snake_case = ""

for i in inp:
    if i.islower(): 
        snake_case += i
    else:
        snake_case += "_"
        snake_case += i.lower()

print(f"snake_case: {snake_case}")