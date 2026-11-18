# Tiny Chess

[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kuro1996/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kuro1996/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01)

Entry for make.fun's [tiny-chess-01](https://make.fun/bounty/tiny-chess-01) on
[make.fun](https://make.fun) — a complete chess engine in 4,096 bytes of Python.

## The engine

`main.py` (4,094 bytes) plays chess on a 0x88 board: negamax with
alpha-beta pruning and quiescence search (captures only), iterative
deepening from depth 1 to 9, a 60,000-node cumulative budget per move,
MVV-LVA move ordering, and compact piece-square tables. Move generation
is verified against perft: 11/11 positions match python-chess exactly.

## Run it

```sh
python3 main.py
```

Reads a position, writes the best move. Standard library only, no
network, deterministic.
