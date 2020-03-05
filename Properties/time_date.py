from datetime import datetime
import pytz

tz_NY = pytz.timezone("America/New_York")
datetime_NY = datetime.now(tz_NY)
print("NY time:", datetime_NY.strftime("%H:%M:%S"))

tz_London = pytz.timezone("Europe/London")
datetime_London = datetime.now(tz_London)
print("London time:", datetime_London.strftime("%H:%M:%S"))

tz_India = pytz.timezone("Asia/Kolkata")
datetime_India = datetime.now(tz_India)
print("India time:", datetime_India.strftime("%H:%M:%S"))

