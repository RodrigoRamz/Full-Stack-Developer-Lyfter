from datetime import date

class User:
    def __init__(self, name, date_of_birth):
        self.name = name
        self.date_of_birth = date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years
    
def require_adult(func):
    def wrapper(user: User, *args, **kwargs):
        if user.age < 18:
            raise PermissionError(f'{user.name} has {user.age} years, you are under 18 years old.')
        print(f"{user.name} has {user.age} years, you are over 18 years old.")
        return func(user, *args, **kwargs)
    return wrapper

@require_adult
def access_bank_account(user):
    return f"Access Approved to {user.name}"

adult = User("Rodrigo", date(1987, 8, 2))
minor = User("Thomas", date(2010, 5, 14))

print(access_bank_account(adult))
print(access_bank_account(minor))


