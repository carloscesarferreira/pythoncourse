n = int(input("Enter a number: "))

odds = []
odds2 = []

def perfect_square(n):
    for i in range(1,n+1):
        if i%2 != 0:
            odds.append(i)

    def sum_odds(odds):
        result = 0
        for k in odds:
            result = result + k
            odds2.append(k)
            if result == n:
                break
        return result
    if sum_odds(odds) == n:
        return "TRUE"
    else:
        return "FALSE"

if perfect_square(n) == "TRUE":
    print(f"TRUE: The number {n} is a perfect square since it is the sum of the {len(odds2)} first odds numbers {odds2}")
else:
    print(f"FALSE: The number {n} is not a perfect square")
