from datetime import datetime
def daysBetweenDates(date1, date2):
    """
    :type date1: str
    :type date2: str
    :rtype: int
    """
    return abs((datetime.strptime(date1, "%Y-%m-%d") - datetime.strptime(date2, "%Y-%m-%d")).days)