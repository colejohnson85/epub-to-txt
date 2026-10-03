![EPUB to TXT](assets/hero.png)

# EPUB to TXT

*A book file you can grep.*

## Overview

This repository is **EPUB to TXT**, a document utility. A book file you can grep.

You want the words, not a reader app.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## What's included

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## Features

- Chapter separators
- UTF-8 output
- Optional per-chapter files
- Keeps the EPUB

## Requirements

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Usage

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/colejohnson85/epub-to-txt

MIT license. See `LICENSE`.
