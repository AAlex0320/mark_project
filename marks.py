# marks.py - a small marks tracker (Week 3 project)
marks = [72, 85, 64, 90, 58]

# Add up all the marks, then divide by how many there are
def average(marks_list):
    total = 0                         # accumulator: starts at 0
    for mark in marks_list:           # one round for each mark
        total = total + mark
    return total / len(marks_list)    # send the answer back

print("Average:", average(marks))
