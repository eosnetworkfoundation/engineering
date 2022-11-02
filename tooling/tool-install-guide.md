# Tool Install Guide
This guide will walk you through installing common engineering tools on your system. If you haven't read the [computer setup](./computer-setup.md) guide yet, start there. This guide is written for Ubuntu derivatives using the BASH shell.

1. Update your system.
    ```bash
    sudo apt-get update
    sudo apt-get upgrade -y
    sudo apt-get autoremove
    ```
1. [Terminator](https://gnome-terminator.org) - iTerm2-like terminal emulator for Linux
    ```bash
    sudo apt-get install -y terminator
    ```
    1. Check `Terminator` > right-click > `Preferences` > `Profiles` > `Scrolling` > `Infinite Scrollback`.
    1. I like to invert the titlebar colors so "focused" is blue (`#0076C9`) or green (`#3FBC6C`), and "receiving" is red (`#C80003`). It is just less aggressive and more plesant to look at. These settings are in `Terminator` > right-click > `Preferences` > `General` > `Terminal Titlebar`.
1. [Vim](https://www.vim.org) - CLI text editor and related utilities
    ```bash
    sudo apt-get install -y vim vim-common
    ```
1. [VScode](https://code.visualstudio.com) - GUI text editor
    ```bash
    sudo apt-get install -y code
    ```
    1. [GitLens](https://marketplace.visualstudio.com/items?itemName=eamodio.gitlens) - VScode extension to view files in the context of their `git` history
    1. [Dark+ Pure Black (OLED)](https://marketplace.visualstudio.com/items?itemName=ChadBaileyVh.oled-pure-black---vscode) - _Optional_ extension to make the existing Dark+ theme distributed with VScode use true black, for OLED displays
1. [Zap](https://github.com/srevinsaju/zap) - a package manager for `*.AppImage` programs
    ```bash
    sudo wget https://github.com/srevinsaju/zap/releases/download/continuous/zap-amd64 -O /usr/local/bin/zap
    sudo chmod +x /usr/local/bin/zap
    ```
1. [Bitwarden](https://bitwarden.com) - secure, open-source password manager
    ```bash
    curl -fSL 'https://vault.bitwarden.com/download/?app=desktop&platform=linux&variant=appimage' -o ~/Downloads/Bitwarden.AppImage
    zap install bitwarden ~/Downloads/Bitwarden.AppImage
    ```
    Fix missing logo.
    ```bash
    sed -E "s_(Icon=).*$$_\1/home/$USERNAME/.local/share/zap/v2/icons/bitwarden.png_" -i ~/.local/share/applications/bitwarden.desktop
    ```
1. [Joplin](https://joplinapp.org) - open-source, Evernote-like note taking app
    ```bash
    zap install --from 'https://github.com/laurent22/joplin/releases/download/v2.8.8/Joplin-2.8.8.AppImage' joplin
    ```
    Fix missing logo.
    ```bash
    sed -E "s_(Icon=).*$$_\1/home/$USERNAME/.local/share/zap/v2/icons/joplin.png_" -i ~/.local/share/applications/joplin.desktop
    ```
1. [Telegram Desktop](https://desktop.telegram.org) - psuedo-secure instant messaging application
    ```bash
    sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo
    flatpak install flathub org.telegram.desktop
    ```
    Log into and configure Telegram Desktop.
1. [Brave](https://brave.com) - privacy-focused Chromium-based web browser with builtin ad and tracker blocking
    ```bash
    sudo apt-get install -y apt-transport-https curl
    sudo curl -fsSLo /usr/share/keyrings/brave-browser-archive-keyring.gpg https://brave-browser-apt-release.s3.brave.com/brave-browser-archive-keyring.gpg
    ```
    Configure Brave, including logging into or creating a work sync profile, if you wish.
1. [Firefox](https://www.mozilla.org/en-US/firefox/new) - a privacy-focused web browser not built on software from an advertisement juggernaut
    ```bash
    sudo apt-get install -y firefox
    ```
    Configure Firefox, including logging into or creating a work Mozilla account, if you wish.
1. [pip](https://pypi.org/project/pip) - package manager for Python
    ```bash
    sudo apt-get install -y python3-pip python3-venv
    ```
1. [docker](https://www.docker.com) - container engine, like virtual machines but lighter
    ```bash
    sudo apt-get install -y ca-certificates curl gnupg lsb-release
    sudo mkdir -p /etc/apt/keyrings
    curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o ~/Downloads/docker.gpg
    cat ~/Downloads/docker.gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
    # note: this command will only work on Ubuntu and Ubuntu derivatives
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(source /etc/upstream-release/lsb-release 2>/dev/null && echo "$DISTRIB_CODENAME" || lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
    sudo apt-get update
    sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-compose-plugin
    sudo service docker start
    sudo docker run hello-world
    ```
    1. Download Ubuntu docker images.
        ```bash
        docker pull ubuntu:18.04
        docker pull ubuntu:20.04
        docker pull ubuntu:22.04
        ```
1. [VirtualBox](https://www.virtualbox.org) - type 2 hypervisor for running computers inside computers as a program
    ```bash
    sudo apt-get install -y virtualbox
    ```
1. [qBittorrent](https://www.qbittorrent.org) - open-source bittorrent client
    1. Optionally, install [this](https://gitlab.com/qbittorrent-black-theme/client) OLED-dark theme.
    1. Download [Ubuntu `*.iso` images](https://ubuntu.com/download/alternative-downloads) for VirtualBox.
1. [Caffeine](https://launchpad.net/caffeine) - keep your computer awake
    ```bash
    sudo apt-get install -y caffeine
    ```
    Make the caffeine indicator appear in the system tray on startup.
    ```bash
    ln -s /usr/share/applications/caffeine-indicator.desktop ~/.config/autostart/caffeine-indicator.desktop
    ```
1. [git](https://git-scm.com) - open-source, distributed version control software
    ```bash
    sudo apt-get install -y git
    ```
    1. Install git.
        ```bash
        brew install git
        ```
    1. Generate an SSH Key and associate it with your GitHub account.
        1. Generate an ed25519 SSH key using your work email.
            ```bash
            ssh-keygen -t ed25519 -f ~/.ssh/github.key -C first.last@eosnetwork.com
            ```
        1. Enter a [strong passphrase](https://www.eff.org/dice).
            - Convenient local JavaScript [diceware generator](https://www.rempe.us/diceware/#eff), trust at your own risk. We recommend using Bitwarden to generate the password or passphrase.
        1. Check that SSH daemon is running
            ```bash
            ssh-agent -s 1>/dev/null && echo 'SSH daemon is running' || echo 'SSH daemon is not running'
            ```
        1. Add new key to keystore.
            ```bash
            ssh-add ~/.ssh/github.key
            ```
        1. Copy your public key to clipboard.
            ```bash
            cat ~/.ssh/github.key.pub
            ```
        1. In your browser, go to:
           [GitHub](https://github.com/) > [Settings](https://github.com/settings/profile) > [SSH and GPG keys](https://github.com/settings/keys) > [New SSH key](https://github.com/settings/ssh/new)
        1. Paste your public key into `Key`.
        1. Give your SSH key a meaningful title, for example "ENF" followed by your computer hostname.
        1. Click `Add SSH Key`.
        1. Test it.
            1. Connect to GitHub via SSH.
                ```bash
                ssh -T git@github.com
                ```
            1. Accept the GitHub RSA fingerprint.
                ```
                yes
                ```
            1. You should see:
                ```
                You've successfully authenticated, but GitHub does not provide shell access.
                ```
    1. Generate an ed25519 GPG Key and associate it with your GitHub account.
        1. Generate the key using your work email.
            1. Start GPG.
                ```bash
                gpg --expert --full-generate-key
                ```
            1. Select `ECC (Sign Only)`.  
               `10`, `[Enter]`
            1. Use an ed25519 key.  
               `1`, `[Enter]`
            1. Set your desired key expiration period.  
               `0`, `[Enter]`  
               `y`, `[Enter]`
            1. Enter your name as you want it to appear next to your contributions in our open-source commit history.
            1. Enter either your work email address, or your [GitHub no-reply email address](https://help.github.com/en/articles/setting-your-commit-email-address).
                - This email address MUST match one of the emails attached to your GitHub account.
            1. Enter your computer's hostname for the comment.
            1. Confirm the settings.  
               `o` (letter 'o' key)
            1. Enter a [strong passphrase](https://www.eff.org/dice), twice.
                - Convenient local JavaScript [diceware generator](https://www.rempe.us/diceware/#eff), trust at your own risk. We recommend using Bitwarden to generate the password or passphrase.
        1. Associate your GPG key with your GitHub account.
            1. Copy your public key to the clipboard.
                ```bash
                gpg --armor --export "$(gpg --list-secret-keys --keyid-format LONG | grep sec | awk '{print $2}' | cut -d '/' -f '2')"
                ```
            1. In your browser, go to:
               [GitHub](https://github.com/) > [Settings](https://github.com/settings/profile) > [SSH and GPG keys](https://github.com/settings/keys) > [New GPG key](https://github.com/settings/gpg/new)
            1. Paste your public key into `Key`.
            1. Click `Add GPG Key`.
    1. Configure your shell.
        1. Configure `gpg` to use `gpg-agent`, similar to `ssh-agent`.
            ```bash
            echo 'use-agent' > ~/.gnupg/gpg.conf
            ```
        1. Configure `gpg-agent` to use the keychain to store the GPG passphrase.
            ```bash
            echo 'pinentry-program /usr/bin/pinentry-gnome3' > ~/.gnupg/gpg-agent.conf
            ```
        1. Reload the `gpg-agent` daemon with the new settings.
            ```bash
            echo RELOADAGENT | gpg-connect-agent
            ```
        1. Load your keys in all shells.
            ```bash
            cat << 'BASH' >> ~/.bashrc
            ### GitHub ###
            export GPG_TTY=$(tty)

            BASH
            source ~/.bashrc
            ```
    1. Store your GPG passphrase in the keyring.
        1. Invoke a `pinentry-gnome3` password prompt.
            ```bash
            echo '1234' | gpg -o /dev/null --local-user "$(gpg --list-secret-keys --keyid-format LONG | grep sec | awk '{print $2}' | cut -d '/' -f '2')" -as - && echo 'Looks good! Can we sign code next time?' || echo 'Oh noes! We could not authenticate!'
            ```
        1. Check `Save in Keychain`.
        1. Enter your GPG passphrase created earlier.
        1. Click `OK`.
    1. Configure git.
        1. Add your work email address.
            ```bash
            git config --global user.email first.last@eosnetwork.com
            ```
        1. Add your real name.
            ```bash
            git config --global user.name 'First Last'
            ```
        1. Point git to your GPG key.
            ```bash
            git config --global user.signingkey "$(gpg --list-secret-keys --keyid-format LONG | grep sec | awk '{print $2}' | cut -d '/' -f '2')"
            ```
        1. Configure git to sign all commits pushed from this user account on this computer.
            ```bash
            git config --global commit.gpgsign true
            ```
        1. Configure git to use your preferred editor.
            ```bash
            git config --global core.editor 'vim'
            ```
        1. Configure git to use SSH for all submodules, even if the repo defines them with HTTPS.
            ```
            cat << 'BASH' >> ~/.gitconfig
            [url "ssh://git@github.com/"]
                    insteadOf = https://github.com/
            BASH
            ```
    1. Verify that your work email is associated with your GitHub account.
       [GitHub](https://github.com/) > [Settings](https://github.com/settings/profile) > [Emails](https://github.com/settings/emails)
        - If your work email is not associated with your GitHub account, your activity on GitHub (pull requests, issues, comments) will appear to come from a different account than your commits and pushes made from this device.
        - Performing this association later can retroactively associate commits with your account.
1. [Beyond Compare](https://www.scootersoftware.com/features.php) - side-by-side comparison, editing, and merging of text, hex, binaries, Office documents, pictures, MP3s, archives, and folders; with support for git integration and cloud locations such as FTP, SFTP, Dropbox, or buckets
    1. Install Beyond Compare.
        ```bash
        sudo apt-get install -y bcompare
        ```
    1. Configure git for diffs with Beyond Compare.
        ```bash
        git config --global diff.tool bc3
        git config --global difftool.bc3.trustExitCode true
        ```
            - The behavior of `git diff` cannot be changed, you use `git difftool` to diff with Beyond Compare.
    1. Configure git for resolving merge conflicts with Beyond Compare.
        ```bash
        git config --global merge.tool bc3
        git config --global mergetool.bc3.trustExitCode true
        ```
            - Invoke `git mergetool` when you want to use Beyond Compare to resolve merge conflicts.

1. [git-imerge](https://github.com/mhagger/git-imerge) - branch merge conflict resolution tool
    ```bash
    pip install git-imerge
    ```
1. Make a work directory.
    ```bash
    mkdir -p ~/Work
    ```
