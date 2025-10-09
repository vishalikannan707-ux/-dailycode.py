# 1. Define if Pac-Man eats a ghost
def eat_ghost(has_power_pellet, touching_ghost):
    """
    Returns True if Pac-Man eats a ghost.

    Parameters:
    - has_power_pellet (bool): Whether Pac-Man has a power pellet.
    - touching_ghost (bool): Whether Pac-Man is touching a ghost.

    Returns:
    - bool: True if Pac-Man can eat the ghost, otherwise False.
    """
    return has_power_pellet and touching_ghost


# 2. Define if Pac-Man scores
def score(touching_power_pellet, touching_dot):
    """
    Returns True if Pac-Man scores by touching a dot or power pellet.

    Parameters:
    - touching_power_pellet (bool): Whether Pac-Man is touching a power pellet.
    - touching_dot (bool): Whether Pac-Man is touching a dot.

    Returns:
    - bool: True if Pac-Man scores, otherwise False.
    """
    return touching_power_pellet or touching_dot


# 3. Define if Pac-Man loses
def lose(has_power_pellet, touching_ghost):
    """
    Returns True if Pac-Man loses by touching a ghost without a power pellet.

    Parameters:
    - has_power_pellet (bool): Whether Pac-Man has a power pellet.
    - touching_ghost (bool): Whether Pac-Man is touching a ghost.

    Returns:
    - bool: True if Pac-Man loses, otherwise False.
    """
    return not has_power_pellet and touching_ghost


# 4. Define if Pac-Man wins
def win(eaten_all_dots, has_power_pellet, touching_ghost):
    """
    Returns True if Pac-Man wins by eating all dots and not losing.

    Parameters:
    - eaten_all_dots (bool): Whether Pac-Man has eaten all the dots.
    - has_power_pellet (bool): Whether Pac-Man has a power pellet.
    - touching_ghost (bool): Whether Pac-Man is touching a ghost.

    Returns:
    - bool: True if Pac-Man wins, otherwise False.
    """
    return eaten_all_dots and not (touching_ghost and not has_power_pellet)
print(eat_ghost(False, True))   # Output: False
print(score(True, True))    # Output: True
print(lose(False, True))        # Output: True
print(win(False, True, False))   # Output: False