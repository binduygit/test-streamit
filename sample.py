def is_leap_year(year):
    """
    Determine if a given year is a leap year.

    Parameters:
    - year (int): The year to be checked.

    Returns:
    - bool: True if the year is a leap year, False otherwise.
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Example usage:
year_to_check = 2020
if is_leap_year(year_to_check):
    print(f"{year_to_check} is a leap year.")
else:
    print(f"{year_to_check} is not a leap year.")