# Global variables using dict ADT and boolean to model problem
left_side = {'teachers': 3,
             'students': 2}
right_side = {'teachers': 0,
              'students': 0}
boat_on_left = True


def move_one(role):
    global boat_on_left
    if boat_on_left:
        boat_on_left = not boat_on_left
        if left_side[role] > 0:
            left_side[role] -= 1
            right_side[role] += 1
        else:
            print(f'Error: no {role} left to move on the left (m1)')
    else:
        boat_on_left = not boat_on_left
        if right_side[role] > 0:
            left_side[role] += 1
            right_side[role] -= 1
        else:
            print(f'Error: no {role} left to move on the right (m1)')


def move_two_students():
    global boat_on_left
    if boat_on_left:
        boat_on_left = not boat_on_left
        if left_side['students'] > 1:
            left_side['students'] -= 2
            right_side['students'] += 2
        else:
            print('Error: no students left to move on the left (m2)')
    else:
        boat_on_left = not boat_on_left
        if right_side['students'] > 1:
            left_side['students'] += 2
            right_side['students'] -= 2
        else:
            print('Error: no students left to move on the right (m2)')


print(f'The left side is {left_side["teachers"] * "T" + left_side["students"] * "S"}'
      f' and the right side is {right_side["teachers"] * "T" + right_side["students"] * "S"}')

# possible steps:

move_two_students()
move_one('students')
move_one('teachers')
move_one('students')

move_two_students()
move_one('students')
move_one('teachers')
move_one('students')

move_two_students()
move_one('students')
move_one('teachers')
move_one('students')

move_two_students()

print(f'The left side is {left_side["teachers"] * "T" + left_side["students"] * "S"}'
      f' and the right side is {right_side["teachers"] * "T" + right_side["students"] * "S"}')
