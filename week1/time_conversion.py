time = input()

mode = time[-2:]
h, m, s = [int(t) for t in time[:-2].split(':')]

if mode == 'AM':
  if h == 12:
    h = 0
else:
  if h < 12:
    h += 12

print(f'{h:02d}:{m:02d}:{s:02d}')
