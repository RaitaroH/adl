# adl
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)

This is wrapper for [vn-ki/anime-downloader](https://github.com/vn-ki/anime-downloader) + [z411/trackma](https://github.com/z411/trackma). The goal? Type `adl`, hit enter, choose show, watch show, update episode number with as little input as possible.

![](./images/terminal.svg)

### Features

+ fetch currently watching anime from your account;
+ option to change account used by trackma;
+ option to update local list;
+ select multiple anime to be watched in sequence;
+ watch any episode from the anime chosen, default is the next episode;
+ easily watch all available episodes after last watched, in order to catch up. Also update list accordingly;
+ prompt user for watching another show;
+ prompt user to add a score to an anime if the anime in question will be set as completed;
+ option to skip all user input - works in combination with the other options as well;
+ download instead of watching; everything from above still applies;
+ use local media instead of streaming. Requires identical folder name to anilist anime title, ex: `Fruits Basket: 2nd Season` should be a folder in `animedir` variable, otherwise `adl` will **not** find the anime folder. Considering random episode numbering, `fzf` is used for episode selecting.
+ download covers from anilist and show them in the terminal;
+ do not display verbose vlc output;
+ warn user if episode wasn't found.

### Requirements
+ [vn-ki/anime-downloader](https://github.com/vn-ki/anime-downloader/wiki/Installation) - make sure this works. [Git version](https://github.com/vn-ki/anime-downloader/issues/226) required for `$adl -y`. Settings for `anime-downloader`, such as provider, need to be placed in your [configuration file](https://github.com/vn-ki/anime-downloader/wiki/Config), as instructed in the documentation.
+ [z411/trackma](https://github.com/z411/trackma) - tested with anilist (you need to set up trackma before using adl). Also adl now needs the following [PR merge](https://github.com/z411/trackma/commit/020c0a25637f7368e6c075bcbe67cd938a51b818) that fixes issue [#9](https://github.com/RaitaroH/adl/issues/9);
+ [junegunn/fzf](https://github.com/junegunn/fzf) - needed for show selection.**Linux users should install fzf from [git](https://github.com/junegunn/fzf/#Using-git),as the it is outdated on package installers**.
+ [MPV](https://mpv.io/) - used to play the anime (better integration with anime-downloader). [VLC](https://www.videolan.org/vlc/) can also be used: `$adl -p vlc`.
+ **perl** - for regular expressions;
+ [frece](https://github.com/SicariusNoctis/frece) - *optional* - `$adl -f` will show most watched anime at the top of the list. By default frece is not used;
+ [ueberzug](https://github.com/seebye/ueberzug) - *optional* - `$adl -c` will download covers from anilist to `/tmp/`, then will display the covers using `ueberzug` in the fzf anime selection window. Alternatively, the script `adl_covers.py` in this repo also downloads covers.
+ [nodejs](https://nodejs.org/en/download/package-manager/) required by many anime providers,including the default one.


## Installation
### Windows
+ First install [Chocolatey](https://chocolatey.org/install) package manager.
+ Install [git-for-windows](https://gitforwindows.org/).
+ Now open cmd/powershell as administrator and install dependencies for anime-downloader and adl,i.e copy-paste following commands:
```
choco install -y python3 aria2 mpv fzf nodejs
refreshenv
```
+ Install trackma and anime-downloader using pip,i.e:
```
pip install -U git+https://github.com/anime-dl/anime-downloader Trackma
```
**If you already have trackma Setup,then skip following step**
+ Now we need to setup trackma,which is pretty straight-forward.type trackma in cmd/powershell.type a to add an account.now type the site that you want to connect trackma with(i.e:anilist,etc).after entering your user-name you will be given a link,paste that link in the browser and give permissions to trackma.you will be given a pin,copy that pin and paste it in the prompt asking for the pin.trackma has been initialized at this point.

**Note:if you update your anime watch-list on anilist or any other site,then you will have to update it in trackma using the ```retrieve``` command.**
+ Now we can use our bash script using ```bash.exe```,which in many cases will be present in "C:\Program Files\Git\bin\",if you have changed the installation directory then change to "that-directory\Git\bin\".we can use bash.exe as it is,but for convinience we will add this directory to [PATH](https://www.architectryan.com/2018/03/17/add-to-the-path-on-windows-10/).after that use ```refreshenv``` to reload the environment variables.
+ Now that all of you dependencies have been installed,we can download adl using git and cd into it,i.e:
```
git clone https://github.com/RaitaroH/adl.git
cd adl
```
+ If you added "Installation Dir\Git\bin" on PATH,then use following to run adl
```
bash.exe .\adl
```
otherwise if you didn't add the directory on PATH ,then
```
"Installation Dir\Git\bin\bash.exe" .\adl
```
### Linux
+ Install all the dependencies from above.
+ Simply download the script in your `~/bin` folder and make it executable.

**Be sure that ~/bin is on [PATH](https://linuxize.com/post/how-to-add-directory-to-path-in-linux/),otherwise you will need to cd to ~/bin everytime.**
```
mkdir -p "$HOME/bin"
wget https://raw.githubusercontent.com/RaitaroH/adl/master/adl -O "$HOME/bin/adl"
chmod +x "$HOME/bin/adl"
```
If you are using Arch Linux you can install from the [Arch Linux User Repository (AUR)](https://aur.archlinux.org/packages/adl-git/) thanks to [@Baitinq](https://github.com/Baitinq).

### Updating

`adl` also has a function for updating itself from source. To use it run `adl -u` or `adl --update` and follow the prompts.

### Issues

If the show doesn't start for you, the script will inform you of this. If you are positive that the episode number has aired, then most likely the provider you are using is NOT yet up-to-date. If you want to try every provider to see where your show is hosted you can try this bash code to cycle through all of them.

```
adlwrap() {
  declare -a provider=(animepahe animeflix animefreak animeflv anistream gogoanime kissanime kisscartoon twist.moe itsaturday)
  for k in $provider; do
    printf "\n\033[0;31m%s\n" "PROVIDER: $k"
    anime dl "$1" --episodes "$2" --provider "$k" --play mpv
  done
}
```

The function above can be used like so: `$ adlwrap "SHOW" "EPISODE"`:

```
$ adlwrap "Gundam: The Origin" "1"
```

The providers there can be found with `anime dl --help`.

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

