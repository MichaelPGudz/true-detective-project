import math

def is_twodigit_odd(number):
    return not number % 2 == 0 and (int(math.log10(number)) + 1) == 2


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    return sudo_mode or writable_by_others or \
           (file_group in users_groups and writable_by_group) or\
           (user == file_owner and writable_by_owner)


def is_leap_year(year):
    return year % 4 == 0 or (year % 400 == 0 or year % 100 != 0)


def is_sunday(day, weekday_of_first):
    pass


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    pass


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    pass
