# Computer Setup
This guide walks you through your options to keep work and personal content separate. There are a variety of reasons to keep your work and personal computing domains separate. Legal reasons include being asked to erase ENF intellectual property or being subpoenaed for work content. Practical reasons include protecting yourself from personal content inadvertently being shared on video calls, or being able to "disconnect" from work in your free time.

### Options
You have three primary options.
1. [Multiple Computers](#multiple-computers)
1. [Virtual Machines](#virtual-machines)
1. [User Accounts](#user-accounts)

## Multiple Computers
This is the most straightforward, but most expensive, option. You have one or more computers for personal use, and one or more computers for work use that are physically distinct. This is simple to implement and very secure.

## Virtual Machines
You can also use a virtual machine for work. This is cheaper than having multiple physical computers, is almost as secure, and is more convenient. However, you won't be able to use all of your computer's resources for work tasks such as compiling code.

Check out the [virtual machine setup guide](./vm-setup.md) for more information on this.

## User Accounts
You can have a work user account and a personal user account on the same physical computer. This is somewhat less secure than the other options because developers and engineers will need their work account to have administrator or super user permissions to do their job. However, this option is great because it allows you to use all the resources on your computer for work, makes it easy to switch back and forth, allows you to use your existing machines, enables you to work on _any_ machine you own, and provides a sufficient degree of separation.

### LightDM
These instructions are written for Linux Mint (Debian-family, Ubunut-based), but should work for any Linux distribution using [LightDM](https://wiki.archlinux.org/title/LightDM) as the display manager.

This guide will walk you through provisioning a separate user account for work, then logging into both _simultaneously_. Your personal account will exist on TTY7 (`[Ctrl] + [Alt] + [F7]`), and your work account will exist on TTY8 (`[Ctrl] + [Alt] + [F8]`). You can be logged into only one or the other, both simultaneously, have one or both locked, switch back and forth instantaneously, and run apps in both at the same time while still keeping them decently isolated. Programs running under either account will have access to their share of the entire computer's physical resources.

1. Create a new user account in Linux that will show up on the login screen. Be sure to replace `$username` with the desired username. The author uses `zach` as his personal username, and chose `zach-enf` as his work username.
    ```bash
    # create a new user account with home folders, default shell, and default password
    sudo useradd -m -p "$(perl -e 'print crypt("password", "salt")')" -s /bin/bash $username  # crypt(password, salt)
    # force the user to reset their password on next login
    sudo chage -d 0 username
    ```
    - ⚠️ **Warning** ⚠️  
      DO NOT use the password you set here beyond logging in to the new user account for the first time (step 4 below)! The `perl` `crypt()` command uses [DES](https://en.wikipedia.org/wiki/Data_Encryption_Standard) to hash your password, a _50 year old_ algorithm [broken in 1998 by the Electronic Frontier Foundation](https://en.wikipedia.org/wiki/EFF_DES_cracker). It would be trivial for anyone who legitimately or illegitimately gains access to any account on your computer to obtain this password. The time, expense, and difficulty to break this is essentially zero. When you log into the new user account for the first time and change your password, Linux will use a secure, modern algorithm to protect it. For example, Linux Mint uses SHA-512 designed by the NSA, ratified by NIST, and which has no known practical attacks.
1. Give the new user sudo permissions. This step is **_optional_**, but engineers will likely need this. You may consider doing this _after_ logging in for the first time and chaging your password.
    ```bash
    sudo usermod -a -G sudo $username
    ```
1. Start a new LightDM session.
    ```bash
    dm-tool switch-to-greeter
    ```
    This will drop you in a new LightDM session on TTY8 with a login screen.
1. Login using the password you created in step 1. Linux should promt you to immediately change your password. If it doesn't, immediately change your password! See the warning above.
1. Change desktop background, layout, and color scheme to make it visually distinctive from your personal account.
    - For example, if you use a green desktop background and iconography in your personal account, consider a blue desktop background and iconography in your work account so you can immediately tell which user you are on.

At this point, your personal account will exist at `[Ctrl] + [Alt] + [F7]` (TTY7), and your work account will exist at `[Ctrl] + [Alt] + [F8]` (TTY8). Try it.

When you boot your computer, you will be on TTY7 by default (`[Ctrl] + [Alt] + [F7]`). Whatever account you login to here will be on TTY7. To log into the other user simultaneously, you will have to run the command from before to start a second LightDM session on TTY8.
```bash
dm-tool switch-to-greeter
```

Once you have a working solution for your work stuff, head to the [tool install guide](./tool-install-guide.md).
