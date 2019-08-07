from unittest import mock, TestCase, main

from app import GhanianName


class NameTestCase(TestCase):

    def test_weekday_name(self):
        app = GhanianName()
        app.gender = 'm'
        app.dob = '14/11/1972'
        self.assertEqual(app.get_weekday_name(), 'Tuesday')


if __name__ == '__main__':
    main()
