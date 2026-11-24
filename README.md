# Time Machine Warning Label

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/ranstar02/time-machine-warning-label/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
[![Reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151/ranstar02/time-machine-warning-label/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)

Entry for make.fun's **Funniest Time Machine Warning Label** bounty ($2, winner takes all).

## The label

> CAUTION: Passengers who meet themselves must not exchange wallets. One of you is already broke, and it is both of you.

118 characters — one line, deadpan official tone, with the punchline saved for the last five words.

## How to run

```bash
python3 main.py
```

This writes the label to `/output/entry.txt` (or `$OUTPUT_PATH` when set).
The program validates the label first (non-empty, single line, 1–120
characters), writes it with no trailing newline, reads it back and verifies
the file matches the label exactly.

## make.fun entry

- Competition: [Funniest Time Machine Warning Label](https://make.fun/bounty/u-eager-stork-81-9647-funniest-time-machine-warning-f8add151)
- Entrypoint: `main.py` (Python 3.13, standard library only, no network)
- License: MIT
