import random
import string

DIGITS = [_ for _ in string.digits]
LOWERCASE_CHARACTERS = [_ for _ in string.ascii_lowercase]

UPPERCASE_CHARACTERS = [_ for _ in string.ascii_uppercase]

SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<','&','#', ';']


TEMP_PASS_LIST = []
password = ''
COMBINED_LIST = DIGITS + LOWERCASE_CHARACTERS + UPPERCASE_CHARACTERS + SYMBOLS
def temp_pass():
  rand_digit = random.choice(DIGITS)
  rand_upper = random.choice(UPPERCASE_CHARACTERS)
  rand_lower = random.choice(LOWERCASE_CHARACTERS)
  rand_symbol = random.choice(SYMBOLS)

  temp_password = rand_digit  + rand_lower + rand_upper + rand_symbol
  TEMP_PASS_LIST.append(temp_password)

for i in range(4):
  temp_pass()

for x in TEMP_PASS_LIST:
  password = password + x

shuffled = list(password)
random.shuffle(shuffled)
shuffled = ''.join(shuffled)
print(shuffled)