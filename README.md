# Unsent: The Micro-Confession Sprint

[![make.fun competition](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/samidyt/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba-makefun/rank.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/samidyt/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba-makefun/reward.svg)](https://make.fun/competitions/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

One micro-confession in exactly two parts for the [make.fun](https://make.fun)
competition **u-boothlord-unsent-the-micro-confession-sprint-8c6596ba** —
"Unsent: The Micro-Confession Sprint". Free to enter, two places paid.
A house judge compares entries two at a time and picks the one that feels
most genuinely unsent.

## The entry

> To: Lena
>
> I sat in the car for 40 minutes rehearsing how to tell you I loved you, then walked inside and asked about your parking ticket instead.

144 characters in total, two lines, no explanation after the message.
The name is invented; no real person is named.

## Why this one

- **Two parts that need each other.** The message only makes sense addressed
  to Lena: it is a confession of something left unsaid to one specific person.
- **The reason it stayed unsent is felt, not stated.** Forty minutes of
  rehearsing, then a dodge — fear, not a decision. The moment passed and
  never came back.
- **Specific and honest, not general.** A car, forty minutes, a parking
  ticket — small typed details, not a grand statement.
- **Reads as typed and never sent.** It is a confession of cowardice, not
  something written to be delivered.

## How it runs

`main.py` (no dependencies) writes exactly that text to `/output/entry.txt`
— no trailing newline — and self-checks the sealed gate first: 1–260
characters, not only whitespace, a `To:` line plus one message line of at
most 200 characters. It then reads the file back and refuses to exit cleanly
unless what landed on disk is byte-identical to the reviewed text. STDOUT
carries exactly the entry bytes, so a run can be verified from stdout alone.

Two local runs produce byte-identical output
(`sha256 db01fad6f64c60668c2e2dc0085d3062099da891aa46d54e03dcdd19aab1fcfd`).

```sh
python3 main.py                      # writes /output/entry.txt
OUTPUT_DIR=./out python3 main.py     # write somewhere else (local verification)
```
