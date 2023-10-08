def round_to_decimal_places(number, decimal_places):
    rounded_number = round(number, decimal_places)
    return rounded_number
input_number = 3.14159265359
decimal_places = 2
rounded_number = round_to_decimal_places(input_number, decimal_places)
print(f"Округленное число: {rounded_number}")