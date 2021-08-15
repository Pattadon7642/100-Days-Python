print('Welcome to the secret auction program.')
program_stop = True
dic = {}

def find_highest(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f'The winner is {winner} with a bid of {highest_bid}')

while program_stop:
    name = input('What is your name?: ')
    bid = int(input('What\'s your bid?: THB '))
    dic[name] = bid
    ask = input('Are there any other bidders? Type \'yes\' or \'no\'\n')
    if ask == 'no':       
        program_stop = False
        break
find_highest(dic)




