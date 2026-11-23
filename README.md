# Tiny Chess

[![tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/kuro1996/tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/kuro1996/tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01)

Entry for make.fun's [tiny-chess-01](https://make.fun/bounty/tiny-chess-01) on
[make.fun](https://make.fun) — a complete chess engine in 4,096 bytes of Python.

## The engine

`main.py` (3,656 bytes, LZMA-packed from a 12,202-byte source) plays
chess on a 0x88 board: negamax with alpha-beta pruning, principal
variation search at the root and in the search, a history heuristic
for quiet-move ordering, killer moves, null-move pruning, a
transposition table, a captures-only quiescence search, incremental
evaluation with piece-square tables, incremental Zobrist hashing,
anti-repetition play, castling and full en-passant support, a
king-centralisation bonus in the endgame, and iterative deepening to
depth 10 under an 80,000-node budget per move. Move generation is
verified against perft: all checks match python-chess exactly,
including en-passant, castling, promotion and pin positions.

## Results

Practice trial (fresh kit, 6 games vs the house gauntlet): **Elo
1,545** — 4 wins, 1 draw, 1 loss — measured in two independent
trial runs (trial-0 and trial-1, both 1,545), well above the 1,154
practice floor. The previous version (v2) measured Elo 876.

## Run it

```sh
python3 main.py
```

Reads a position, writes the best move. Standard library only, no
network, deterministic.
