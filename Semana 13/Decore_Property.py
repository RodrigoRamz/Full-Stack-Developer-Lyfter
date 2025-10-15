from datetime import date

def check_adult_user(func):
        def wrapper(user, *args, **kwargs):
            if not isinstance(user, User):
                raise TypeError("First Parameter should be a User object")
            if user.age < 18:
                raise PermissionError(f"User {user.name} is not over 18 years old. Your age is {user.age}.")
            return func(user, *args, **kwargs)
        return wrapper


class User:
    def __init__(self, name, date_of_birth):
        self.name= name
        self.date_of_birth= date_of_birth

    @property
    def age(self):
        today = date.today()
        years = today.year - self.date_of_birth.year
        #adjust if the Birthday has not passed
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            years -= 1
        return years
    

    
@check_adult_user
def access_system(user):
    return f"Access Approved to {user.name}, age {user.age}"
    
adult = User("Rodrigo", date(1987, 8, 2,))
minor = User("Johnny", date(2010, 5, 12))

print(access_system(adult))
print(access_system(minor))