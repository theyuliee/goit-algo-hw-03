import random
def get_numbers_ticket(min: int, max: int, quantity: int) :
    if min >= 1 and max <= 1000 and min < max and (max - min) >= quantity:
       lottery_numbers = {}
       lottery_numbers = random.sample(range(min, max + 1), quantity)
       lottery_numbers.sort(key = None, reverse = False )
       return lottery_numbers
    else :
        print ('Введіть значення від 1 до 1000')
        return []



print (get_numbers_ticket(1, 10, 2))
