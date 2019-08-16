# adl

This is wrapper for ![vn-ki/anime-downloader](https://github.com/vn-ki/anime-downloader) + ![z411/trackma](https://github.com/z411/trackma). The goal? Type `adl`, hit enter, choose show, watch show, update episode number with as little input as possible.

![](./images/terminal.svg)

### Features

+ fetch currently watching anime from your account;
+ watch any episode from the anime chosen, default is the next episode;
+ easily watch all available episodes after last watched, in order to catch up. Also update list accordingly;
+ promt user for watching another show without fetching list again;
+ promt user to add a score to an anime if the anime in question will be set as completed;
+ do not display verbose vlc output;
+ warn user if episode wasn't found.

### Requirements

+ anime-donwloader;
+ trackma - tested with Anilist;
+ fzf.

### Installation

Simply download the script in your `~/bin` folder and make it executable.

```
mkdir -p "$HOME/bin"
wget https://raw.githubusercontent.com/RaitaroH/adl/master/adl -O "$HOME/bin/adl"
chmod +x "$HOME/bin/adl"
```
