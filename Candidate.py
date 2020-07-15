class Candidate:
    def __init__(self, number, first_name, patro_nymic, last_name, desired_position, current_position, current_place,
                 birth_date, sex, status, phone, email, skype, facebook, linkedin, type_of_employment,
                 field_of_activity, work_experience, salary, currency, language, language_level, region, date_of_adding,
                 local_id, action_date, action_creator, action, comment_date, comment_creator, comment):
        self.number = number
        self.first_name = first_name
        self.patro_nymic = patro_nymic
        self.last_name = last_name
        self.desired_position = desired_position
        self.current_position = current_position
        self.current_place = current_place
        self.birth_date = birth_date
        self.sex = sex
        self.status = status
        self.phone = phone
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
        self.language_level = language_level
        self.region = region
        self.date_of_adding = date_of_adding
        self.local_id = local_id
        self.action_date = action_date
        self.action_creator = action_creator
        self.action = action
        self.comment_date = comment_date
        self.comment_creator = comment_creator
        self.comment = comment

    def __str__(self):
        return "test"

    def __repr__(self) -> str:
        return self.__dict__.__str__()
