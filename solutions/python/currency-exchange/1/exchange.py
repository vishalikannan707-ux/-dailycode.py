def exchange_money(budget, exchange_rate):
    """
    Exchange the budget for foreign currency at the given exchange rate.
    :param budget: float or int, the amount of money planned for exchange
    :param exchange_rate: float, the amount of domestic currency equal to 1 unit of foreign currency
    :return: float, the value of the exchanged currency
    """
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """
    Calculate the amount of money left after exchanging.
    :param budget: float or int, the original amount
    :param exchanging_value: float or int, the amount taken out to exchange
    :return: float, the remaining budget
    """
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total value of the received bills.
    :param denomination: int, the value of a single bill
    :param number_of_bills: int, how many bills received
    :return: int, the total value of the bills
    """
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    """
    Calculate how many whole bills one can get from the amount.
    :param amount: float or int, original amount of money
    :param denomination: int, value of a single bill
    :return: int, number of bills
    """
    return int(amount // denomination)

def get_leftover_of_bills(amount, denomination):
    """
    Calculate the leftover amount that cannot be converted to a whole bill.
    :param amount: float or int, original amount of money
    :param denomination: int, value of a single bill
    :return: float, remaining money after taking bills
    """
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum value of the new currency (in whole bills),
    after including the exchange spread and considering denominations.
    :param budget: float or int, the amount of money to exchange
    :param exchange_rate: float, exchange rate (domestic per 1 foreign)
    :param spread: int, percentage fee
    :param denomination: int, denomination of bills
    :return: int, the maximum exchangeable value in foreign currency denominations
    """
    # add spread (percentage fee) to the exchange rate
    actual_rate = exchange_rate + (exchange_rate * spread / 100)
    exchanged_amount = budget / actual_rate
    num_bills = int(exchanged_amount // denomination)
    return num_bills * denomination
    

    