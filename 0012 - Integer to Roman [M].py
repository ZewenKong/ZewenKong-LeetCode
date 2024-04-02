def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    intromanmapunits = {1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX'}
    intromanmapdecades = {1: 'X', 2: 'XX', 3: 'XXX', 4: 'XL', 5: 'L', 6: 'LX', 7: 'LXX', 8: 'LXXX', 9: 'XC'}
    intromanmapcents = {1: 'C', 2: 'CC', 3: 'CCC', 4: 'CD', 5: 'D', 6: 'DC', 7: 'DCC', 8: 'DCCC', 9: 'CM'}
    intromanmapthousands = {1: 'M', 2: 'MM', 3: 'MMM'}
    intromanmap = [intromanmapunits, intromanmapdecades, intromanmapcents, intromanmapthousands]
    romanstring = []
    decade = 0
    while num != 0:
        current_digit = num % 10
        if current_digit != 0:
            romanstring.append(intromanmap[decade][current_digit])
        decade += 1
        decade = min(3, decade)
        num //= 10
    romanstring.reverse()
    return ''.join(romanstring)