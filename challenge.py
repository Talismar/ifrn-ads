result = {"sequence_size": 0, "number": 0}

for int_number in range(1, 1000000):
    current_number = int_number
    current_sequence_size = 1

    while current_number > 1:
        if current_number % 2 == 0:
            current_number //= 2

        else:
            current_number = (current_number * 3) + 1

        current_sequence_size += 1

    if current_sequence_size > result["sequence_size"]:
        result["sequence_size"] = current_sequence_size
        result["number"] = int_number

print(result)
