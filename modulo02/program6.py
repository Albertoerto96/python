#Zonas horarias

from datetime import datetime, timedelta
from pytz import timezone
import pytz

print(pytz.all_timezones)
print(datetime.now(pytz.timezone("Asia/Tokyo")))
print(datetime.now(pytz.timezone("Europe/Madrid")))
print(datetime.now(pytz.timezone("US/Alaska")))