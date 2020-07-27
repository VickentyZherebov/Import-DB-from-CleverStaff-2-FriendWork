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
        self.birth_date = self._reformat_date(birth_date)
        self.sex = sex

        head_hunt_states = [
            "Активный поиск",
            "Нанят",
            "Наш сотрудник",
            "Не заинтересован"
        ]
        self_response = [
            "Пассивный поиск"
        ]

        if status in head_hunt_states:
            self.status = "Активный поиск"
        elif status in self_response:
            self.status = "Отклик"
        else:
            self.status = None

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
        self.date_of_adding = self._reformat_date(date_of_adding)
        self.local_id = local_id
        self.actions = []
        self.comments = []

    def _reformat_date(self, external_date: [str]) -> [str]:
        if external_date is not None:
            match = re.fullmatch("(\\d{4})-(\\d{2})-(\\d{2})", external_date)
            if match:
                year = match.group(1)
                month = match.group(2)
                day = match.group(3)
                return f'{day}.{month}.{year}'

        return None

    def __repr__(self) -> str:
        return self.__dict__.__repr__()
