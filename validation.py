def validate_input(value):
    if value.strip() == "":
        return "Input cannot be empty"
    return "Valid input"

print(validate_input("Hello"))
print(validate_input(""))
