def format_phone_number(phone_number):
    area_code = phone_number[:3]
    prefix = phone_number[3:6]
    line_number = phone_number[6:]
    formatted_number = f"({area_code}) {prefix}-{line_number}"
    return formatted_number

# Sample Input
phone_number = "8005551212"

# Output
print(format_phone_number(phone_number))