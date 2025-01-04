from validator_collection import checkers

email_address = checkers.is_email(input("Email: "))
if email_address:
    print("Valid")
else:
    print("Invalid")
