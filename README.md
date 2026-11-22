# Tiny Chess

[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kuro1996/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kuro1996/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01)

Entry for make.fun's [tiny-chess-01](https://make.fun/bounty/tiny-chess-01) on
[make.fun](https://make.fun) — a complete chess engine in 4,096 bytes of Python.

## The engine

`main.py` (4,004 bytes) plays chess on a 0x88 board: negamax with
alpha-beta pruning and a shallow captures-only quiescence search,
iterative deepening from depth 1 to 9, a 60,000-node cumulative budget
per move, a transposition table for move ordering, MVV-LVA move
ordering, root move ordering from the previous iteration, and real
piece-square tables. Move generation is verified against perft: 18/18
checks match python-chess exactly (the engine deliberately does not
generate en-passant captures, a byte trade-off; every other move
matches). Practice trial: Elo 876 (0 wins, 2 draws, 4 losses over 6
games vs the house gauntlet).

## Run it

```sh
python3 main.py
```

Reads a position, writes the best move. Standard library only, no
network, deterministic.
