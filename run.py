from app import GhanianName
import sys


app = GhanianName()
if len(sys.argv) == 3:
    app.set_info(sys.argv[1], sys.argv[2])
else:
    app.ask_info()

print('You were born on a {}.'.format(app.get_weekday_name()))
print('Your Ghanian name is {}'.format(app.get_ghanian_name()))
