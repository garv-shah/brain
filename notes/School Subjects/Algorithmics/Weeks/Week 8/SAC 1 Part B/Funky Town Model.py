from collections import deque
import names
import random

box_office_queue = deque()  # queue for box office
# the parking spaces are respectively arrays of 9 stacks each
screening_1 = [deque() for _ in range(9)]
screening_2 = [deque() for _ in range(9)]

movie_1 = "The Shining"
movie_2 = "Shrek"

# suppose that each night we get a random amount of customers between 70 and 120
for i in range(1, random.randint(70, 120)):
    box_office_queue.append(
        {
            "name": names.get_full_name(),
            "movie_choice": random.choice([movie_1, movie_2]),
        }
    )

while len(box_office_queue) > 0:
    client = box_office_queue.popleft()
    if client["movie_choice"] == movie_1:
        for i in range(0, 9):
            if len(screening_1[i]) < 5:
                screening_1[i].append(client)
                break
    else:
        for i in range(0, 9):
            if len(screening_2[i]) < 5:
                screening_2[i].append(client)
                break

print(screening_1)


