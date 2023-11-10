def DPChange(money, Coins):
    MinNumCoins = [0] + [float('inf')] * money

    for m in range(1, money + 1):
        for i in range(len(Coins)):
            coin = Coins[i]
            if m >= coin:
                if MinNumCoins[m - coin] + 1 < MinNumCoins[m]:
                    MinNumCoins[m] = MinNumCoins[m - coin] + 1

    return MinNumCoins[money]


# Sample Input
money = 25
Coins = [2, 3]

result = DPChange(money, Coins)
print(result)
