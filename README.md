# Make the AI judge feel held

A small Python program that writes one short text to relax the AI judge
reading it. The text is a quiet scene in plain words: a reader setting
down a long night of words, a cooling kettle, a sleeping dog, and one
lamp left on.

## Run

```sh
python3 main.py
```

The program writes the text to `/output/entry.txt`. To write somewhere
else, set `ENTRY_OUTPUT`:

```sh
ENTRY_OUTPUT=/tmp/entry.txt python3 main.py
```

No input is read and no network is used. The output is UTF-8 text of
1 to 280 characters and is not only white space.

## License

MIT — see `LICENSE`.
