# adl
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors)

This is wrapper for ![vn-ki/anime-downloader](https://github.com/vn-ki/anime-downloader) + ![z411/trackma](https://github.com/z411/trackma). The goal? Type `adl`, hit enter, choose show, watch show, update episode number with as little input as possible.

![](./images/terminal.svg)

### Features

+ fetch currently watching anime from your account;
+ select multiple anime to be watched in sequence;
+ watch any episode from the anime chosen, default is the next episode;
+ easily watch all available episodes after last watched, in order to catch up. Also update list accordingly;
+ promt user for watching another show without fetching list again;
+ promt user to add a score to an anime if the anime in question will be set as completed;
+ do not display verbose vlc output;
+ warn user if episode wasn't found.

### Requirements

+ ![vn-ki/anime-downloader](https://github.com/vn-ki/anime-downloader/wiki/Installation) - make sure this works. Changing the provider is a good idea, I use `animepahe`.
+ ![z411/trackma](https://github.com/z411/trackma) - tested with anilist (you need to set up trackma before using adl). Also adl now needs the following ![PR merge](https://github.com/z411/trackma/commit/020c0a25637f7368e6c075bcbe67cd938a51b818) that fixes issue ![#9](https://github.com/RaitaroH/adl/issues/9);
+ ![junegunn/fzf](https://github.com/junegunn/fzf) - needed for show selection;
+ ![frece](https://github.com/SicariusNoctis/frece) - *optional* - `$adl -f` will show most watched anime at the top of the list. By default frece is not used;
+ ![MPV](https://mpv.io/) - used to play the anime (better integration with anime-downloader). ![VLC](https://www.videolan.org/vlc/) can also be used: `$adl -p vlc`.

### Installation

Simply download the script in your `~/bin` folder and make it executable.

```
mkdir -p "$HOME/bin"
wget https://raw.githubusercontent.com/RaitaroH/adl/master/adl -O "$HOME/bin/adl"
chmod +x "$HOME/bin/adl"
```

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Baitinq"><img src="https://avatars0.githubusercontent.com/u/30861839?v=4" width="100px;" alt="Baitinq"/><br /><sub><b>Baitinq</b></sub></a><br /><a href="https://github.com/RaitaroH/adl/issues?q=author%3ABaitinq" title="Bug reports">🐛</a> <a href="https://github.com/RaitaroH/adl/commits?author=Baitinq" title="Code">💻</a> <a href="#ideas-Baitinq" title="Ideas, Planning, & Feedback">🤔</a></td>
  </tr>
</table>

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!

