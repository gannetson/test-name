import datetime


class GhanianName(object):

    gender = ''
    dob = ''

    names = [
        {
            # Sunday
            'm': 'Kwasi',
            'f': 'Acoseya',
        },
        {
            # Monday
            'm': 'Kojo',
            'f': 'Adwoa',
        },
        {
            # Tuesday
            'm': 'Kobena',
            'f': 'Abenna',
        },
        {
            # Wednesday
            'm': 'Kwaku',
            'f': 'Akweya',
        },
        {
            # Thursday
            'm': 'Kofi',
            'f': 'Efiya',
        },
        {
            # Friday
            'm': 'Yaw',
            'f': 'Ya',
        },
        {
            # Saturday
            'm': 'Kwame',
            'f': 'Ama',
        }
    ]

    def set_info(self, dob, name):
        self.dob = dob
        self.gender = name

    def ask_info(self):
        self.dob = input('What is your date of birth (dd/mm/yyy): ')
        self.gender = input('Are you male or female? m/f: ')

    def get_weekday(self):
        date = datetime.datetime.strptime(self.dob, '%d/%m/%Y')
        return date.weekday()

    def get_ghanian_name(self):
        return self.names[self.get_weekday()][self.gender]

    def get_weekday_name(self):
        date = datetime.datetime.strptime(self.dob, '%d/%m/%Y')
        return date.strftime('%A')
