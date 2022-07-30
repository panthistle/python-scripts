
import datetime
import pytz     # pip install pytz

# datetime commands
#print(dir(datetime))


# ------------------------------------------------------------------------------
#
# --------------------------------- date ---------------------------------------

# date commands
#print(dir(datetime.date))

#help(datetime.date)
# datetime.date(year, month, day) --> date object

d = datetime.date(2000, 1, 25)
bday = datetime.date(2022, 10, 14)

today = datetime.date.today()
#print(today.year)

dayid = today.weekday()     # Monday is 0 and Sunday is 6
#print(dayid)

dayid = today.isoweekday()  # Monday is 1 and Sunday is 7
#print(dayid)

def days_between(fromdate, todate):
    td = todate - fromdate
    return td.days

dtb = days_between(today, bday)
#print(dtb)


# ------------------------------------------------------------------------------
#
# ------------------------------ timedelta -------------------------------------

# timedelta commands
#print(dir(datetime.timedelta))

#help(datetime.timedelta)
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, 
#                   minutes=0, hours=0, weeks=0) --> timedelta object

# timedelta is the difference between two datetime values
# if we add/subtract timedelta to/from date, we get another date
tdelta = datetime.timedelta(days=7)
newdate = today + tdelta
#print(newdate)
# if we add/subtract date to/from date, we get timedelta
tdelta = newdate - today
#print(tdelta)


# ------------------------------------------------------------------------------
#
# --------------------------------- time ---------------------------------------

# time commands
#print(dir(datetime.time))

#help(datetime.time)
# datetime.time(hour=12, minute=0, second=0, microsecond=0, 
#               tzinfo=None) --> time object

# example
t = datetime.time(3, 12, 45, 100000)
#print(t)
#print(t.hour)


# ------------------------------------------------------------------------------
#
# ------------------------------- datetime -------------------------------------

# datetime commands
#print(dir(datetime.datetime))

help(datetime.datetime)
# datetime.datetime(year, month, day, hour=0, minute=0, second=0, 
#                   microsecond=0, tzinfo=None) --> datetime object

# not timezone aware
dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
#print(dt_today)
#print(dt_now)
#print(dt_utcnow)

# using pytz module
dt = datetime.datetime(2000, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
# print(dt)

dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow2)

dt_ath = dt_utcnow.astimezone(pytz.timezone('Europe/Athens'))
# print(dt_ath)

# timezones info
# for tz in pytz.all_timezones:
    # print(tz)

# convert from naive to timezone aware
dt_athens = datetime.datetime.now()
athens_tz = pytz.timezone('Europe/Athens')
dt_athens = athens_tz.localize(dt_athens)
# print(dt_athens)

# convert between different timezones
dt_paris = dt_athens.astimezone(pytz.timezone('Europe/Paris'))
# print(dt_paris)

# strftime - Datetime to String
dt_str = dt_paris.strftime('%B %d, %Y')
#print(dt_str)     

# strptime - String to Datetime
dt_str = 'May 31, 2022'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
#print(dt)
