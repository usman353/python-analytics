# a, b = 0, 1
# for i in range(1, 10):
#     print(a)
#     a, b = b, a + b

# x = [1, [1, ['a', 'b']]]
# print(x)


# def search_list(list_of_tuples, value):
#     for comb in list_of_tuples:

#         for x in comb:
#             if x == value:
#                 print(x)
#                 return comb
#     else:
#         return 0


# prices = [('AAPL', 96.43), ('IONS', 39.28), ('GS', 159.53)]
# ticker = 'GS'
# print(search_list(prices, ticker))
import datetime
date = '01-Apr-03'
date_object = datetime.datetime.strptime(date, '%d-%b-%y')
print((date_object).date())
