import math

def is_twodigit_odd(number):
    if number % 2 == 0:
        return False
    else:
        if (int(math.log10(number)) + 1) == 2:
            return True
        else:
            return False


def has_access(user, users_groups, file_owner, writable_by_owner, file_group, writable_by_group, writable_by_others, sudo_mode):
    if sudo_mode:
        return True
    elif writable_by_others:
        return True
    elif file_group in users_groups:
        if writable_by_group:
            return True
    elif user == file_owner:
        if writable_by_owner:
            return True
        else:
            return False
    return False


def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False



def is_sunday(day, weekday_of_first):
    pass


def should_bring_umbrella(rains, wind_scale, cloudy, red_sky, strong_flower_smell, spiders_down, lying_cattle, strong_sunshine):
    pass


def should_take_a_nap(want_to, trouble_sleeping, after_4pm, at_work, mad_boss, have_30m, have_10m):
    if want_to:
        if trouble_sleeping:
            return False
        if after_4pm:
            return False
        if at_work:
            if mad_boss:
                return False
        if not have_30m:
            if have_10m:
                return True
        else:
            return True
    return False
