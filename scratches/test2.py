from collections import deque
import random

CYRILLIC_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщьъыэюя'

QUEUE = deque(CYRILLIC_LETTERS[:3])

total_count = 0


def get_members(query: str):
    global total_count

    total_count += 1
    result = random.randint(0, 500 - 100 * len(query))
    print(f'{query} ({result})')

    if result > 200:
        for letter in CYRILLIC_LETTERS:
            get_members(query + letter)


for i in CYRILLIC_LETTERS[:3]:
    get_members(i)

print(total_count)
