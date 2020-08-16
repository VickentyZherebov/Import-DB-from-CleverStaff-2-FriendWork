import re


class Candidate:
    def __init__(self, number, first_name, patronymic, last_name, desired_position, current_position, current_place,
                 birth_date, sex, status, phone: str, email: str, skype, facebook, linkedin: str, type_of_employment,
                 field_of_activity, work_experience, salary, currency, language, region, date_of_adding,
                 local_id):
        self.number = number
        self.first_name = first_name
        self.patronymic = patronymic
        self.last_name = last_name
        self.desired_position = desired_position
        self.current_position = current_position
        self.current_place = current_place
        self.birth_date = self._reformat_birth_date(birth_date)
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
        elif phone is not None:
            phone_lines = phone.split(', ', 1)
            if len(phone_lines) >= 2:
                self.phone = phone_lines[0]
                self.phone_comment = phone_lines[1]
            else:
                self.phone_comment = phone
        self.email_comment = None
        self.email = None
        if email is not None and re.fullmatch("(^|\s)[-a-z0-9_.]+@([-a-z0-9]+\.)+[a-z]{2,6}(\s|$)", email):
            self.email = email
        elif email is not None:
            email_lines = email.split(', ', 1)
            if len(email_lines) >= 2:
                self.email = email_lines[0]
                self.email_comment = email_lines[1]
            else:
                self.email_comment = email
        else:
            self.email = email
        self.skype = skype
        self.facebook = facebook
        self.linkedin_comment = None
        self.linkedin_is_link = None
        self.linkedin = None
        if linkedin is not None and re.fullmatch("http?s://www.linkedin.com/\S+\s*", linkedin):
            self.linkedin_is_link = "li"
            self.linkedin = linkedin
        elif linkedin is not None and re.fullmatch("linkedin.com\S+\s*", linkedin):
            self.linkedin_is_link = "li"
            self.linkedin = linkedin
        else:
            self.linkedin_comment = linkedin
        self.type_of_employment = type_of_employment
        self.field_of_activity = field_of_activity
        self.work_experience = work_experience
        self.salary = salary
        self.currency = currency
        if language is not None:
            language_lines = language.split(', ', -1)
            count = 0
            for i in language:
                if i == ",":
                    count = count + 1
            if count == 1:
                language_name = language.split(' ', 1)
                print(language_name[0])
            if count == 2:
                language_name = language.split(' ', 2)
                print(language_name[0])
                print(language_name[1])
        self.region = region
        self.date_of_adding = self._reformat_date_added(date_of_adding)
        self.local_id = local_id
        self.actions = []
        self.comments = []

    def _reformat_birth_date(self, external_date: [str]) -> [str]:
        if external_date is not None:
            match = re.fullmatch("(\\d{4})-(\\d{2})-(\\d{2})", external_date)
            if match:
                year = match.group(1)
                month = match.group(2)
                day = match.group(3)
                return f'{day}.{month}.{year}'

        return None

    def _reformat_date_added(self, external_date: [str]) -> [str]:
        if external_date is not None:
            match = re.fullmatch("(\\d{4})-(\\d{2})-(\\d{2}) (\\d{2}):(\\d{2})", external_date)
            if match:
                year = match.group(1)
                month = match.group(2)
                day = match.group(3)
                return f'{day}.{month}.{year}'

        return None

    def __repr__(self) -> str:
        return self.__dict__.__repr__()
