def leap_year(year):
    """
    Determines if a given year is a leap year according to the Gregorian calendar rules:
    - The year must be evenly divisible by 4.
    - If it's also divisible by 100, it must be divisible by 400 to be a leap year.
    
    Parameters:
    year (int): The year to check (e.g., 1997, 1900, 2000).
    
    Returns:
    bool: True if it's a leap year, False otherwise.
    """
    if year % 4 == 0:
        if year % 100 == 0:
            return year % 400 == 0
        return True
    return False
