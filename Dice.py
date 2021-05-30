def exercise1(trial):
    hasSix = False
    isPair = False
    pairs = 0
    for char in trial:
        # This is the case if a 6 is found and no 6 has been found before it
        if char == '6' and not isPair:
            if hasSix:
                isPair = True
            else:
                hasSix = True
        # This is the case where a pair of 6 has been found, but the current char is also a 6
        elif char == '6' and isPair:
            isPair = False
            hasSix = True
        else:
            if isPair:
                pairs += 1
            hasSix = False
            isPair = False
    # This is the case if the pair has been found at the end of the sequence
    if isPair:
        pairs += 1
    return pairs


def exercise2(trial):
    count = 0
    tmp_count = 0
    for char in trial:
        if char == '6':
            if tmp_count > count:
                count = tmp_count
            tmp_count = 0
        else:
            tmp_count += 1
    return tmp_count if tmp_count > count else count


def exercise3(trial):
    luckyseries = []
    counter = 0
    for char in trial:
        if char == '6' or char == '5':
            counter += 1
        else:
            if counter > 0:
                luckyseries.append(counter)
                counter = 0
    if len(luckyseries) == 0:
        return counter
    if counter != 0:
        luckyseries.append(counter)
        counter = 0
    # Creating a copy of the luckyseries without duplicates
    luckyseries_no_duplicates = list(dict.fromkeys(luckyseries))
    # Creating a tuple (count, series) with the most frequent luckyseries
    most_frequent = (0, 0)
    for char in luckyseries_no_duplicates:
        if luckyseries.count(char) > most_frequent[0]:
            most_frequent = (luckyseries.count(char), char)
        if luckyseries.count(char) == most_frequent[0] and char > most_frequent[1]:
            most_frequent = (luckyseries.count(char), char)
    return most_frequent[1]


def main():
    input_file = open('input.txt', 'r')
    input_array = input_file.readlines()
    input_file.close()
    for i in range(len(input_array)):
        line = input_array[i]
        # Getting the trial and number of throws from the file
        num_of_throws = line.strip().split('\\n')[0].strip()
        trial = line.strip().split('\\n')[1].strip()
        input = 'Number of throws: ' + num_of_throws + '\nSequence: ' + trial
        # Checking that the number of throws matches the length of the trial
        if int(num_of_throws) == len(trial):
            # Saving the result from each exercise
            ex_1 = str(exercise1(trial))
            ex_2 = str(exercise2(trial))
            ex_3 = str(exercise3(trial))
            # Each exercise has to be printed on its own line
            output = 'Exercise 1: ' + ex_1 + '\nExercise 2: ' + ex_2 + '\nExercise 3: ' + ex_3
            print(input + '\n\n' + output + '\n')
        else:
            print('The number of throws does not match the length of the sequence.')


if __name__ == '__main__':
    main()
