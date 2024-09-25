import random
def get_numbers_ticket(min, max, quantity) :
    if min >= 1 and max <= 1000 :
       lottery_numbers = {}
       lottery_numbers = random.sample(range(min, max + 1), quantity)
       return number_ticket
    else :
        print ('Введіть значення від 1 до 1000')



