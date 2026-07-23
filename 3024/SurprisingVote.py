"""SurprisingVote"""
allvote = float(input())
highestvote = float(input())
lowestpossible = allvote - highestvote - highestvote
if lowestpossible < 0:
    lowestpossible = 0
issurprising = highestvote - lowestpossible
if issurprising > 2:
    print("Surprising")
else:
    print("Not surprising")
