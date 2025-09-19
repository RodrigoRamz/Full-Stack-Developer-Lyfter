
class Student: #class in the student's model
    def __init__(self, name, group, spanish, english, geography, sciences):
        if not str(name).strip():
            raise ValueError('Name cannot be Empty')
        if not str(group).strip():
            raise ValueError('Group cannot be empty')
        
        self.name = str(name).strip()
        self.group = str(group).strip()

        self.spanish = Student._validate_score(spanish)
        self.english = Student._validate_score(english)
        self.geography = Student._validate_score(geography)
        self.sciences = Student._validate_score(sciences)

    @staticmethod
    def _validate_score(score):
        v = int(score)
        if 0 <= v <= 100:
            return v
        raise ValueError('Score must be between 0 and 100')


    def average(self):
        #ALL: calculates and returns the average of the 4 grades. 
        return (self.spanish + self.english + self.geography + self.sciences) / 4

    def to_dict(self):
        return {
            'name': self.name,
            'group': self.group,
            'spanish': self.spanish,
            'english': self.english,
            'geography': self.geography,
            'sciences': self.sciences,
        }

    @classmethod
    def from_dict(cls, d):
        return cls(
            d.get('name', ''),
            d.get('group', ''),
            d.get('spanish', 0),
            d.get('english', 0),
            d.get('geography', 0),
            d.get('sciences', 0),
        )


    def __repr__(self):
        return f'Student({self.name}, {self.group}, avg={self.average():.2f})'