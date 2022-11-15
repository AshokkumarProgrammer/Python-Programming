import re

for i in range(int(input())):
  number = input()
  match = re.match('^[789][0-9]{9}$', number)
  if match:
    print('YES')
  else:
    print('NO')