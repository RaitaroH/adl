<div align="center">
  <h1>adl<br>
    <img alt="GitHub Repo stars" src="https://img.shields.io/github/stars/RaitaroH/adl?style=flat-square">
    <a href="#contributors-">
      <img alt="GitHub Repo stars" src="https://img.shields.io/github/all-contributors/RaitaroH/adl/master?color=orange&style=flat-square">
    <a/>
  </h1>
  <p>
    This is wrapper for <a href="https://github.com/justfoolingaround/animdl">animdl</a> +
    <a href="https://github.com/z411/trackma">trackma</a>.<br>
    The goal? Type adl, hit enter, choose show, watch show, update episode number with as little input as possible.
  </p>

  ![](./images/terminal.svg)
</div>

## Features

+ fetch currently watching anime from your account;
+ ability to switch between lists: watching, completed, rewatching, paused, dropped, plantowatch;
+ option to change account used by trackma;
+ option to update local list;
+ select multiple anime to be watched in sequence;
+ watch any episode from the anime chosen, default is the next episode;
+ easily watch all available episodes after last watched, in order to catch up. Also update list accordingly;
+ prompt user for watching another show;
+ prompt user to add a score to an anime if the anime in question will be set as completed;
+ option to skip all user input - works in combination with the other options as well;
+ download instead of watching; everything from above still applies;
+ use local media instead of streaming:
  - requires *identical folder name* to anilist anime title; ex: `Fruits Basket:
    2nd Season` should be a folder inside `animedir` containing the vidoes,
    otherwise `adl` will **not** find the anime folder;
  - considering different naming conventions, `fzf` is used for episode
    selecting and `perl` is used for better matching, but it will search for *0#
    format*;
  - to avoid *Scans* and other such extras, the `find` maxdepth is set to *1*,
    as such don't have folders inside folders; use a *symlink* instead, or change
    the maxdepth value.
+ download covers from anilist and show them in the terminal;
+ do not display verbose vlc output;
+ warn user if episode wasn't found.

## Requirements
**Note**: [vn-ki/anime-downloader](https://github.com/vn-ki/anime-downloader) seems to be depricated. As such I have ported to animdl.
  
+ [animdl](https://github.com/justfoolingaround/animdl) - make sure this works. Settings for animdl, such as provider, need to be placed in your [configuration file](https://github.com/justfoolingaround/animdl#configurations).
+ [z411/trackma](https://github.com/z411/trackma) - tested with anilist (you need to set up trackma before using adl). Also adl now needs the following [PR merge](https://github.com/z411/trackma/commit/020c0a25637f7368e6c075bcbe67cd938a51b818) that fixes issue [#9](https://github.com/RaitaroH/adl/issues/9);
+ [junegunn/fzf](https://github.com/junegunn/fzf) - needed for show selection.
  Make sure you install the latest version from github to prevent issue [#35](https://github.com/RaitaroH/adl/issues/35);
+ [MPV](https://mpv.io/) - used to play the anime (better integration with anime-downloader). [VLC](https://www.videolan.org/vlc/) can also be used: `$adl -p vlc`;
+ **perl** - for regular expressions;
+ [frece](https://github.com/SicariusNoctis/frece) - *optional* - `$adl -f` will show most watched anime at the top of the list. By default frece is not used;
+ [ueberzug](https://github.com/seebye/ueberzug) - *optional* - `$adl -c` will download covers from anilist to `/tmp/` using **cURL** and **wget**, then will display the covers using `ueberzug` in the fzf anime selection window. Alternatively, the script `adl_covers.py` in this repo also downloads covers.

## Installation
### Linux
+ Install all the dependencies from above.
+ Simply download the script into your `~/bin` or `~/local/bin` folder and make it executable. `~/bin` should be added to your $PATH.

```
mkdir -p "$HOME/bin"
wget https://raw.githubusercontent.com/RaitaroH/adl/master/adl -O "$HOME/bin/adl"
chmod +x "$HOME/bin/adl"
```
Or:
```
wget https://raw.githubusercontent.com/RaitaroH/adl/master/adl -O "$HOME/.local/bin/adl"
chmod +x "$HOME/.local/bin/adl"
```

+ If you are using Arch Linux you can install from the [Arch Linux User Repository (AUR)](https://aur.archlinux.org/packages/adl-git/) thanks to [@Baitinq](https://github.com/Baitinq).

+ Setup trackma as seen [below](#trackma-setup). If you already have trackma set up, then skip this step.
+ Change default provider, [Anime Downloader Configuration](#anime-downloader-configuration).

### Windows
Windows platform is not officially supported. User discretion is advised.

+ Install [Chocolatey](https://chocolatey.org/install) package manager (used to install other dependencies).
+ Install [git-for-windows](https://gitforwindows.org/) (used to run the bash script).
+ Should not be needed to be installed separately, but [perl](https://strawberryperl.com/) and [curl](https://curl.se/windows/) are also required.
+ Open CMD/PowerShell as /Administrator/ and run the following dependencies. `nodejs` is not strictly needed, but many providers need it.
```
choco install -y python3 aria2 mpv fzf nodejs
refreshenv
```
+ Install trackma and anime-downloader using pip. **Note**: if needed you may install [youtube-dl](https://github.com/ytdl-org/youtube-dl) as well.
```
pip install -U git+https://github.com/anime-dl/anime-downloader Trackma
```

+ Setup trackma as seen [below](#trackma-setup). If you already have trackma set up, then skip this step.
+ Change default provider, [Anime Downloader Configuration](#anime-downloader-configuration).

+ Download this repository. You will need `adl` and `player_check.bat` at the least. You may download the zip or clone the repository. Be mindful of the folder you are in:
```
git clone https://github.com/RaitaroH/adl.git
cd adl
```

+ To run the script execute the command from below. `C:\Program Files\Git\bin\` should be added to your [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/) to simply use `bash.exe`. You may type `refreshenv` to reload the environment variables after adding to PATH, or reopen the CMD/PowerShell. **Note:** `.\adl` assumes you are currently in the folder where adl is; otherwise specify the full path.
```
bash .\adl
```
  - see `adl -h` for more information.

**Windows sepcific issues**
+ covers don't work;
+ in the event that `adl` cannot count watched episodes:
  1. verify that `mpv.com` exists at `C:\ProgramData\chocolatey\lib\mpv.install\tools`; 
  2. from a CMD run `echo %PATHEXT%` to test if you get `.COM;.EXE;...` and not `.EXE;.COM...`. Change the [PATHEXT](https://www.nextofwindows.com/what-is-pathext-environment-variable-in-windows) if needed.
  3. use `bash .\adl -p 'mpv.com'` as last option. This might break some providers.

### Trackma Setup
Setting up Trackma can be done using the GTK and Qt interfaces. Alternatively:
  + In the CMD/PowerShell/Terminal type `trackma`;
  + Type `a` to add an account;
  + Type anilist/myanimelist etc;
  + Enter your username;
  + Copy the url in a browser and get your token from the anime site;
  + Paste the pin in the CMD/PowerShell/Terminal;
  + Type `retrieve` to get your list. **Note:** you may use `adl -r` to force retrieve before getting the anime list.

### Anime Downloader Configuration
The provider `animdl` is using, may not work for you. As such configure `animdl` by editing the [config file](https://github.com/justfoolingaround/animdl#configurations).

**Note** - adl used to be able to change providers, as "anime dl" had a flag for it; "animdl" does not, so you will ned to modify the file manually.

## Updating

`adl` also has a function for updating itself from source. To use it run `adl -u` or `adl --update` and follow the prompts.

## Issues

If the show doesn't start for you, the script will inform you of this. If you are positive that the episode number has aired, then most likely the provider you are using is NOT yet up-to-date.

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tr>
    <td align="center"><a href="https://github.com/Baitinq"><img src="https://avatars0.githubusercontent.com/u/30861839?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Baitinq</b></sub></a><br /><a href="https://github.com/RaitaroH/adl/issues?q=author%3ABaitinq" title="Bug reports">🐛</a> <a href="https://github.com/RaitaroH/adl/commits?author=Baitinq" title="Code">💻</a> <a href="#ideas-Baitinq" title="Ideas, Planning, & Feedback">🤔</a></td>
    <td align="center"><a href="https://github.com/Justaus3r"><img src="https://avatars.githubusercontent.com/u/72691864?v=4?s=100" width="100px;" alt=""/><br /><sub><b>Justaus3r</b></sub></a><br /><a href="https://github.com/RaitaroH/adl/commits?author=Justaus3r" title="Code">💻</a> <a href="#tutorial-Justaus3r" title="Tutorials">✅</a></td>
  </tr>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
