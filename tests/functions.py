
# ------------------------------------------------------------------------------
#
# ------------------------- function calls -------------------------------------

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    # year : int
    # return True for leap years, False for non-leap years

    return year%4 == 0 and (year%100 != 0 or year%400 == 0)

def days_in_month(year, month=2):
    # year : int
    # month : int in [1, 12]
    # return number of days in a month of a year

    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]


# TEST
print(days_in_month(2022, 2))


# ------------------------------------------------------------------------------
#
# ------------------ positional/keyword arguments ------------------------------

def func(*args, **kwargs):
    # args = tuple , kwargs = dict
    print(args)
    print(kwargs)


# TEST
order = ['clamps', 'shrimps']
customer = {'name': 'Joe', 'age': 34}
func(*order, **customer)
# OR
func('haddock', 'salad', name='Jim', age=28)


# ------------------------------------------------------------------------------
#
# -------------------------- function nesting ----------------------------------

def func(a1, a2, a3):

    asum = a1 + a2
    def subfunc(exp=2):
        return asum**exp
    return subfunc() - a3


# TEST
print(func(1,4,30))
