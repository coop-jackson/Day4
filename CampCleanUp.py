count = 0
with open('cleanup_assignments.txt') as file:
    for line in file.readlines():
        elfs = line.strip().split(',')
        min_max_one = elfs[0].split('-')
        min_max_two = elfs[1].split('-')
        print(line.strip())
        #checks if min_max_one within min_max_two
        if int(min_max_one[0]) >= int(min_max_two[0]) and int(min_max_one[1]) <= int(min_max_two[1]):
            count += 1
        #checks if min_max_two within min_max_one
        elif int(min_max_one[0]) <= int(min_max_two[0]) and int(min_max_one[1]) >= int(min_max_two[1]):
            count += 1

print(f'overlapping groups {count}')

#part two

count = 0
with open('cleanup_assignments.txt') as file:
    for line in file.readlines():
        elfs = line.strip().split(',')
        min_max_one = elfs[0].split('-')
        min_max_two = elfs[1].split('-')
        # check relationship of min-maxes
        print(line.strip())
        # checks lower bounds overlap
        if int(min_max_one[0]) <= int(min_max_two[0]) and int(min_max_one[1]) >= int(min_max_two[0]):
            count += 1
        # checks upper bounds overlap
        elif int(min_max_one[0]) >= int(min_max_two[0]) and int(min_max_one[0]) <= int(min_max_two[1]):
            count += 1
print(f'overlapping groups {count}')
