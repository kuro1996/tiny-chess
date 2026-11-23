# Tiny Chess v3f — 4 KB Chess Engine

[![Practice Elo](https://img.shields.io/badge/practice%20Elo-1279-blue)](https://make.fun/competitions/tiny-chess-01)
[![main.py](https://img.shields.io/badge/main.py-4088%20bytes-green)](https://make.fun/competitions/tiny-chess-01)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A chess engine in 4,088 bytes of Python (LZMA-packed `main.py`),
written from scratch for MakeFun tiny-chess-01 ($500, deadline
24 Nov 2026). It plays the 6-game practice trial against the house
gauntlet via `MAKEFUN_ENV_URL`: no model calls, no clock in the
search, deterministic.

## Measured result (practice trial-0, fresh kit, full 6 games)

**Elo 1279** (floor 1154, margin +125) — 3 wins, 0 draws, 3 losses,
spare plies 274, wall 1,164 s of the 1,800 s budget.

| Game | Opponent | Colour | Result | Reason | Plies |
|---|---|---|---|---|---|
| 1 | depth-2 (855) | white | 1-0 win | checkmate | 79 |
| 2 | depth-3 (1073) | black | 0-1 win | adjudicated | 200 |
| 3 | depth-4 (1199) | white | 1-0 win | checkmate | 47 |
| 4 | nodes-100k (1392) | black | 1-0 loss | checkmate | 131 |
| 5 | nodes-250k (1497) | white | 0-1 loss | checkmate | 144 |
| 6 | nodes-500k (1596) | black | 1-0 loss | checkmate | 155 |

An earlier 80,000-node build rated 1191 on the same trial with a
1,478 s wall; the shipped 60,000-node build rates higher and runs
safer. Slowest single move observed: ~4.6 s (limit 10 s).

## Design

- **Board:** 0x88, signed piece integers (white positive, black
  negative; 1 pawn, 2 knight, 3 bishop, 4 rook, 5 queen, 6 king).
- **Eval:** material (100/320/330/500/900) + standard piece-square
  tables, updated incrementally; king-endgame bonus growing as
  non-pawn material falls below 1600 cp (max ~96 cp).
- **Search:** alpha-beta, iterative deepening to depth 10 under a
  fixed 60,000-node budget per move; Principal Variation Search;
  transposition table with cutoffs; history heuristic (2 x 16384,
  +depth-squared on beta cutoffs); guarded null-move pruning;
  quiescence over captures, promotions and check evasions.
- **Correctness:** full castling and full en passant (including the
  en-passant pin); threefold-repetition avoidance via incremental
  Zobrist hashing (side, castling rights and en-passant file included).
- **Legality speed:** pseudo-legal moves are filtered by a pin test —
  only the king, pinned pieces, en-passant captures and moves made
  while in check go through make/unmake. Verified by perft
  (startpos, Kiwipete, en passant, castling, pins, check evasions —
  all counts match python-chess, state intact after make/unmake).

## Layout

- `main.py` — the whole engine, 4,088 bytes as committed (LZMA payload
  + unpacker stub, produced by `makefun compress`). Standard library
  only; reads no other file.
- `README.md` — this file. `LICENSE` — MIT.
  `.makefun/owner.json` — claim file for the entry's wallet.
