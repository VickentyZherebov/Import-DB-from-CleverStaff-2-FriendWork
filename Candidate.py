import re

class Candidate:
    def __init__(self, number, first_name, patronymic, last_name, desired_position, current_position, current_place,
                 birth_date, sex, status, phone: str, email, skype, facebook, linkedin, type_of_employment,
                 field_of_activity, work_experience, salary, currency, language, region, date_of_adding,
                 local_id):
        self.number = number
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.desired_position = desired_position
        self.current_position = current_position
        self.current_place = current_place
        self.birth_date = birth_date
        self.sex = sex
        self.status = status
        self.phone_comment = None
        self.phone = None
        if phone is not None and re.fullmatch("\\d+", phone):
            self.phone = phone
        else:
            self.phone_comment = phone
        self.email = email
        self.skype = skype
        self.facebook = facebook
        self.linkedin = linkedin
        self.type_of_employment = type_of_employment
        self.field_of_activity = field_of_activity
        self.work_experience = work_experience
        self.salary = salary
        self.currency = currency
        self.language = language
        self.region = region
        self.date_of_adding = date_of_adding
        self.local_id = local_id
        self.actions = []

    def __repr__(self) -> str:
        return self.__dict__.__repr__()
