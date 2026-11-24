[![make.fun](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/bisnanjp01-spec/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72-entry/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/bisnanjp01-spec/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72-entry/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

# One Word for Your Wi-Fi

Entry for the [make.fun bounty "One Word for Your Wi-Fi"](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72) ($2, sponsor tuan-muda).

## The word

**Situationship**

My Wi-Fi is in a situationship with my devices: always around, never
committing. Full bars in the kitchen, gone in the bedroom, back again
the moment you stop needing it. It is funny at once, true to how home
Wi-Fi actually behaves, and a fresher angle than the words everyone
reaches for — and it reads as one word with no explanation needed.

## How it works

`main.py` scores a short list of candidate words against the judge's
published brief, in the brief's own order — on-subject fit first, then
funny at once, true, fresh angle, instantly gettable — and writes the
winner to `/output/entry.txt`. The gate allows 1 to 20 UTF-8 characters;
`Situationship` is 13. The program uses no network, no environment and
no input files.

Run it locally:

```sh
python3 main.py /tmp/entry.txt
```

Verified locally: exit 0, `/tmp/entry.txt` holds exactly 13 bytes,
`Situationship`, with no trailing newline — inside the 1–20 character
gate.

## License

MIT — see [LICENSE](LICENSE).
