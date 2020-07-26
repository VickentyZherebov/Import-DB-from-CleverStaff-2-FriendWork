import re


class Candidate:
    def __init__(self, number, first_name, patronymic, last_name, desired_position, current_position, current_place,
                 birth_date, sex, status, phone: str, email, skype, facebook, linkedin: str, type_of_employment,
                 field_of_activity, work_experience, salary, currency, language, region, date_of_adding,
                 local_id):
        self.number = number
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.desired_position = desired_position
        self.current_position = current_position
        self.current_place = current_place
        self.birth_date = None
        if birth_date is not None:
            year = birth_date[0:4]
            month = birth_date[5:7]
            day = birth_date[8:10]
            self.birth_date = day + '.' + month + '.' + year
        self.sex = sex
        self.status = None
        if status == "Активный поиск":
            status = "Активный поиск"
            self.status = status
        if status == "Нанят":
            status = "Активный поиск"
            self.status = status
        if status == "Наш сотрудник":
            status = "Активный поиск"
            self.status = status
        if status == "Не заинтересован":
            status = "Активный поиск"
            self.status = status
        if status == "Пассивный поиск":
            status = "Отклик"
            self.status = status
        self.phone_comment = None
        self.phone = None
        if phone is not None and re.fullmatch("\\d+", phone):
            self.phone = phone
        else:
            self.phone_comment = phone
        self.email_comment = None
        self.email = None
        if email is not None and re.search("\s", email):
            self.email_comment = email
        else:
            self.email = email
        self.skype = skype
        self.facebook = facebook
        self.linkedin_is_link = None
        self.linkedin = None
        if linkedin is not None:
            self.linkedin_is_link = "li"
            self.linkedin = linkedin
        self.type_of_employment = type_of_employment
        self.field_of_activity = field_of_activity
        self.work_experience = work_experience
        self.salary = salary
        self.currency = currency
        self.language = language
        self.region = region
        self.date_of_adding = None
        if date_of_adding is not None:
            year = date_of_adding[0:4]
            month = date_of_adding[5:7]
            day = date_of_adding[8:10]
            self.date_of_adding = day + '.' + month + '.' + year
        self.local_id = local_id
        self.actions = []
        self.comments = []

    def __repr__(self) -> str:
        return self.__dict__.__repr__()
