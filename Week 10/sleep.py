def sheep(n):
    for i in range(n):
        yield "🐏" * i

print(*sheep(10000))