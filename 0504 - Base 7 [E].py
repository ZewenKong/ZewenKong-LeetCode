# class Solution(object):
#     def convertToBase7(self, num):
#         """
#         :type num: int
#         :rtype: str
#         """
#         if num == 0:
#             return "0"
#
#         is_negative = num < 0
#
#         if is_negative:
#             num = -num
#
#         base_7 = ""
#
#         while num > 0:
#             remainder = num % 7
#
#             base_7 = str(remainder) + base_7
#
#             num //= 7
#
#         # If num was originally negative, add a '-' sign to the base 7 representation
#         if is_negative:
#             base_7 = '-' + base_7
#
#         # Return the base 7 representation
#         return base_7