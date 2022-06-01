import datetime
# import pytz

# datetime commands
#print(dir(datetime))


# ------------------------------------------------------------------------------
#
# --------------------------------- date ---------------------------------------

# date commands
#print(dir(datetime.date))

d = datetime.date(2000, 1, 1)
bday = datetime.date(2022, 10, 14)

today = datetime.date.today()
#print(today.year)

dayid = today.weekday()     # Monday is 0 and Sunday is 6
#print(dayid)

dayid = today.isoweekday()  # Monday is 1 and Sunday is 7
#print(dayid)

def days_to_bday(bday):
    today = datetime.date.today()
    to_bday = bday - today
    return to_bday.days

dtb = days_to_bday(bday)
#print(dtb)


# ------------------------------------------------------------------------------
#
# ------------------------------ timedelta -------------------------------------

# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, 
#                   minutes=0, hours=0, weeks=0)

hrs = datetime.timedelta(hours=12)
#print(today + hrs)

# d2 = d + hrs
# timedelta = d + d2


# ------------------------------------------------------------------------------
#
# --------------------------------- time ---------------------------------------

# time commands
#print(dir(datetime.time))

# function to set the time
t = datetime.time(9, 30, 45, 100000)
#print(t)


# ------------------------------------------------------------------------------
#
# ------------------------------- datetime -------------------------------------

# datetime commands
#print(dir(datetime.datetime))

dt = datetime.datetime.today()
dtnow = datetime.datetime.now()
print(dt)
print(dtnow)

# dt = datetime.datetime(2016, 7, 24, 12, 30, 45, tzinfo=pytz.UTC)
# print(dir(dt))

# dt_utcnow = datetime.datetime.now(tz=pytz.UTC)
# print(dt_utcnow)

# dt_utcnow2 = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt_utcnow2)

# dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
# print(dt_mtn)

dt_mtn = datetime.datetime.now()

# mtn_tz = pytz.timezone('US/Mountain')
# dt_mtn = mtn_tz.localize(dt_mtn)

print(dt_mtn)

# dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
# print(dt_east)

# strftime - Datetime to String
dt_str = dt_mtn.strftime('%B %d, %Y')
#print(dt_str)     

# strptime - String to Datetime
dt_str = 'July 24, 2016'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
#print(dt)


