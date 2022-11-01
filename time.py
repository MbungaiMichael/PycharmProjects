# greeting at a any point of the day

import time

present_time = int(time.strftime('%H'))
if present_time >= 00 and present_time <= 11:
    print('good morning')
elif present_time == int(12):
    print('midday')
elif present_time >=  12 and present_time <= 16:
    print('good afternoon')
else:
    print('good night')
