# -*- coding: utf-8 -*-


from typing import List, NewType, Tuple


class Player(object):

    def __init__(self, no, rate) -> None:
        self.no = no
        self.rate = rate


Winner = NewType("Winner", Player)
Loser = NewType("Loser", Player)


def match(p1: Player, p2: Player) -> Tuple[Winner, Loser]:
    return (p1, p2) if p1.rate > p2.rate else (p2, p1)


def _get_answer(l_player: List[Player]):

    # まずm回戦実施
    next_l_player = []
    if len(l_player) == 2:
        winner, loser = match(l_player[0], l_player[1])
        return loser.no
    else:
        for j in range(0, len(l_player), 2):
            winner, loser = match(l_player[j], l_player[j+1])
            next_l_player.append(winner)

    # 残った人を次の回線に
    return _get_answer(next_l_player)


def get_answer(n: int, l_a: List[int]):
    center_index = 1 << (n-1)

    winnere_rate = max(l_a)
    winner_idx = l_a.index(winnere_rate)

    if winner_idx >= center_index:
        semi_winners_block = l_a[:center_index]
    else:
        semi_winners_block = l_a[center_index:]

    semi_winner_rate = max(semi_winners_block)
    semi_winner_idx = l_a.index(semi_winner_rate)
    return semi_winner_idx + 1


if __name__ == "__main__":
    # S = input()
    # N = int(input())
    # S = input().split()
    # A, B, C = input().split()
    # L = list(map(int, input().split()))
    # H, N = map(int, input().split())

    N = int(input())
    L_A = list(map(int, input().split()))


    print(get_answer(N, L_A))
