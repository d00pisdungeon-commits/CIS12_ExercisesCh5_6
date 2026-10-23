from time import time

now = time()
days = now // 86400
today_seconds = now % 86400
hours = int(today_seconds // 3600)
minutes = int((today_seconds % 3600) // 60)
seconds = int(today_seconds % 60)

print(f'Days since Unix Epoch {days}')
print(f'Current Time of Day (UTC): {hours}:{minutes}:{seconds}')

