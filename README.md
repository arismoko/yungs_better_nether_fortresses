# YUNG's Better Nether Fortresses for Sunrise

Nether fortresses redesigned as a keep with halls, bridges and blaze towers.

A port of [YUNG's Better Nether Fortresses](https://github.com/YUNG-GANG/YUNGs-Better-Fortresses) by YUNGNICKYOUNG and Acarii to [Sunrise](https://playsunrise.net) (Minecraft Java 26.3). It is a content mod: the original's structures, templates, loot tables and strings, upgraded to 26.3, with no code. The 26.3 carry is by AdLf0208 ([AdLf0208/yungs_better_nether_fortresses](https://github.com/AdLf0208/yungs_better_nether_fortresses)); this fork moves it to Sunrise.

## What it adds

- A new Nether fortress: a keep, great halls, battle bridges and blaze towers, 167 templates assembled by YUNG's jigsaw rules with their own terrain fitting.
- Its placement keeps clear of vanilla's other Nether structures.
- Nine chest loot tables and the pillars and stair supports that hold the bridges up.
- Vanilla Nether fortresses no longer generate, as in the original (its "Disable Vanilla Fortresses" option is on by default).

## Differences from the original

- The bridge arches above the bridge piers and the item frames' contents are left out.

## Building

With the Sunrise mod tool (`cargo sunrise-mod`, from the Sunrise SDK):

```sh
cargo sunrise-mod check
cargo sunrise-mod build    # target/sunrise-mod/betterfortresses.smod
```

This version is made for the Sunrise Dev build `dev-2026-11-23-ebd2d22` or newer: earlier builds stop a jigsaw structure deeper than 20 pieces.

## Licence and credits

YUNG's Better Nether Fortresses is by YUNGNICKYOUNG and Acarii (https://github.com/YUNG-GANG/YUNGs-Better-Fortresses). Its structures, templates, loot tables and strings are theirs and are used here under the **GNU LGPL v3.0 only**, the original's licence; `LICENSE` holds the text.

Carried to Minecraft 26.3 by AdLf0208 ([AdLf0208/yungs_better_nether_fortresses](https://github.com/AdLf0208/yungs_better_nether_fortresses)), and ported to Sunrise by arismoko. This port is distributed under the same licence.
