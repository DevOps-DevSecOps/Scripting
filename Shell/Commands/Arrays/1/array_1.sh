$ distros=(Ubuntu Fedora SUSE "Arch Linux" Nix)

$ echo ${distros[2]}
SUSE

$ echo ${distros[3]}
Arch Linux

$ echo ${distros[*]}
Ubuntu Fedora SUSE Arch Linux Nix

length elements of an array
$ echo Total distros are ${#distros[@]}
Total distros are 5

add additional elements to an array
$ distros+=(void)
$ echo ${distros[*]}
Ubuntu Fedora SUSE Arch Linux Nix void

$ distros[7]=Slackware
$ echo ${distros[*]}
Ubuntu Fedora SUSE Arch Linux Nix void Slackware

$ distros[2]=Debian
$ echo ${distros[*]}
Ubuntu Fedora Debian Arch Linux Nix void Slackware

remove an array element
$ unset distros[3]
$ echo ${distros[*]}
Ubuntu Fedora Debian Nix void Slackware


[LINK]
https://itsfoss.com/bash-arrays/
