""""ไพ่ 44 ใบ"""
def main():
    """ไพ่ 44 ใบ"""
    cards = input().upper()
    ranks = {'A': 'ace', 'K': 'king', 'Q': 'queen', 'J': 'jack'}
    suits = {'C': 'clubs', 'D': 'diamonds', 'H': 'hearts', 'S': 'spades'}

    rank = cards[:-1]
    suit = cards[-1]

    front = ranks.get(rank, rank)
    end = suits.get(suit, "")

    print(f"{front} of {end}")

main()
