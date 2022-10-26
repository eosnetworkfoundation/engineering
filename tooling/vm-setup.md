# Ubuntu Virtual Machine Setup Guide
Virtual machines allow you to run a computer inside a computer as an app or program. This can be extremely helpful testing Leap or other ENF applications in a clean environment or using an operating system different than what you have installed. This guide, written while I was waiting on three permutations of Ubuntu to install in VMs on two different host machines, will walk you though setting up Ubuntu virtual machines assuming you know nothing about virtual machines.

Note there is a host, your physical computer, and a guest, the virtual machine running as a program on your computer.

### Index
1. [VirtualBox](#virtualbox)
    1. [Install VirtualBox](#install-virtualbox)
    1. [Create a Virtual Machine](#create-a-virtual-machine)
    1. [Install Ubuntu](#install-ubuntu)
    1. [Snapshot of a Clean Install](#snapshot-of-a-clean-install)
    1. [Snapshot with Guest Additions](#snapshot-with-guest-additions)
    1. [Restore from a Snapshot](#restore-from-a-snapshot)
1. Security Concerns

## VirtualBox
[VirtualBox](https://www.virtualbox.org) is a free and open source [type 2 hypervisor](https://en.wikipedia.org/wiki/Hypervisor#Classification) that lets you run virtual machines. If you are using Windows or Linux, we recommend using VirtualBox. It is free, capable, and runs very fast on Windows and Linux. If you are using macOS then you can try VirtualBox. It works okay for some people, but most users report very poor performance and graphical bugs on macOS.

### Install VirtualBox
Download and install VirtualBox, if you haven't already.

On Debian-family Linux, run the following.
```bash
sudo apt-get update
sudo apt-get upgrade -y virtualbox
```
Note that the package `virtualbox-guest-utils` is _not_ free and open-source software, this package is licensed by Oracle. You will probably never need it. If you do, consult the license terms and ENF leadership to determine if we need to buy a license or if we can use it for free.

### Create a Virtual Machine
Follow these steps to create a new virtual machine.
1. Open VirtualBox
2. Create a new virtual machine
	1. Machine > New
	2. Click `Expert Mode` at the bottom
	3. Give your virtual machine a name, like "Ubuntu 22.04.1"
	4. Make sure `Type` is `Linux`
	5. Make sure `Version` is `Ubuntu (64-bit)`
	6. Set the memory size to between 8192 MB and half your system memory
	7. Ensure `Create a virtual hard disk now` is selected under `Hard disk`
	8. Click `Create`
	9. Change `File size` to at least 64 GB, 128 GB would be better.
		1. It will not use this much space on your actual hard drive.
	10. Ensure `Dynamically allocated` is selected on the right under `Storage on physical hard disk`
	11. Click `Create`
3. Configure the virtual machine
	1. Click `Settings`
	2. General
		1. Advanced
			1. Consider setting `Shared Clipboard` to `Bidirectional`
			2. Consider setting `Drag'n'Drop` to `Bidirectional`
		2. Description - provide a useful description
	3. System
		1. Motherboard
			1. Uncheck `Floppy` because this isn't 2001
			2. Uncheck `Hardware Clock in UTC Time`
		2. Processor
			1. Set `Processor(s)` to some portion of your physical CPU cores. If you have a lot then you really don't need more than four. Put another way, the slider should be in the green part as far to the right as you can without touching the red part. For example:
				- If it says that you have 8 CPUs and four of them are green, choose 1, 2, or 3.
				- If it says you have sixteen CPUs and all of them are green, you can choose up to 15, but four is plenty and I really wouldn't exceed 14.
				- If it says you have two CPUs, choose one.
			2. Check any of the `Extended Features` that are available to you
	4. Display
		1. Screen
			1. Turn `Video Memory` all the way up no matter how bad your computer is
			2. Check `Acceleration: Enable 3D Acceleration` at the bottom
	5. Storage
		1. Click `Empty` with the little blue disk next to it
		2. Click the little blue disk with the down arrow on the far-right
		3. Click `Choose a disk file...`
		4. Select the `*.iso` file on your host (computer) for the operating system you are installing
		5. Click `Open`
	6. You can share folders between the host and guest under `Shared Folders` if you wish
	7. Click `OK`

### Install Ubuntu
Install Ubuntu using the default installation options.
1. Click `Start` for your virtual machine
2. Click `Install Ubuntu`
3. Click `Continue`
4. Click `Continue`
5. Click `Install Now`
6. Click `Continue`
	1. This will only effect the guest virtual machine, not your host computer
7. Click `Continue`
8. Enter stuff here. The hostname or computer name *must* be unique from every other computer or virtual machine in your house.
	```
	Name: Zach
	Computer name: enf-jammy-vm
	Username: zach
	```
   - Enter a password, as well. I honestly use a simple password that is the same for all of my virtual machines because the virtual machine disk image is stored in your user/home folder so it is behind the security of your host, hopefully including full disk encryption and a strong password.
9. Check `Log in automatically`
10. Click `Continue`
11. Once the installation finishes, follow the instructions to restart. For older versions of Ubuntu, you may have to use Machine > Reset

### Snapshot of a Clean Install
We will take a snapshot of a "clean install" with nothing installed or upgraded, and only minor setup. This will allow you to instantly revert to a "clean install" for testing later, if you need to.
1. If prompted to upgrade anything, decline.
1. Click through any welcome wizards until they are gone. Don't install anything.
1. Change apps pinned to taskbar as desired.
   - Un-pin any items on the left that aren't useful to you by right-clicking > `Remove from Favorites`.
   - Likewise, pin any items there that are useful to you by hitting Start/Windows/Super, typing the name of the application, right-clicking, then selecting `Add to Favorites`. Hit `Escape` to get out of the start menu or launcher.
   - Arrange the icons on the left taskbar as you like.
1. Shut down the guest (virtual machine).
1. Select your new virtual machine on the left.
1. Machine > Tools > Snapshots
1. Click `Take`
1. Name it something useful, like "Ubuntu 22.04.1 clean install"
1. Give it a useful description explaining what you have done so far. For exmaple:
	```
	A clean install of Ubuntu 22.04.1 with default settings. Icons were rearranged.
	```
1. Click `OK`.

### Snapshot with Guest Additions
We will install "guest additions," a suite of basic tools that will allow you to copy and paste between your host and guest, drag-and-drop, use "seamless" integration where you can have programs running on your guest appear in your taskbar like they are running on your host, and, most importantly, it allows you to easily resize your guest window instead of it being tiny. We will take a snapshot with this setup so that, if you bork your virtual machine, you can just restore it to a point where all this stuff is already setup but you haven't done anything to it yet.

1. Click `Start` to boot the guest back up.
1. Once it has started, open a terminal in the guest.
   ```
   [Ctrl] + [Alt] + [T]
   ```
1. Update the guest.
	```bash
	sudo apt-get update
	sudo apt-get upgrade -y
	```
1. Install programs required by VirtualBox guest additions.
	```bash
	sudo apt-get install -y gcc make perl
	```
1. Select `Devices` > `Insert Guest Additions CD Image...`.
   - Some versions of Ubuntu might prompt you to select `Run` or `Cancel`. `Run` might work, but I always just click `Cancel` and run the command in the next step.
1. Install VirtualBox guest additions.
	```bash
	/media/$USER/VBox_GAs_6.1.38/autorun.sh
	```
   - This will prompt you for your guest password. If you run this script with `sudo`, it doesn't work for some reason.
1. Once this finishes, press `[Enter]`.
1. Install caffeine, a program that allows you to keep the virtual machine from going to sleep or locking by clicking a little coffee cup in the system tray by the clock.
	```bash
	sudo apt-get install -y caffeine
	mkdir -p ~/.config/autostart/
	ln -s /usr/share/applications/caffeine-indicator.desktop ~/.config/autostart/caffeine-indicator.desktop
	```
1. Make a work folder for your code, and make the terminal open there by default.
	```bash
	mkdir -p ~/Work
	echo 'cd ~/Work' >> ~/.bashrc
	```
1. Install any additional tools you want baked-in for developer work. Don't install too much, you probably want this to be as close to a clean install as possible for debugging. Don't forget that these tools weren't installed by default when you write documentation.
	```bash
	sudo apt-get install -y curl git jq
	```
1. Reboot the guest (virtual machine).
	- Now you should be able to do things like resize your virtual machine window.
1. After it reboots, right-click the CD icon on the desktop or in the taskbar and select `Eject`.
	- If it isn't there, look in the file manager. On some versions of Ubunut, it may no longer be in the pretend CD ROM drive.
1. Shut down the guest.
1. Select your new virtual machine on the left.
1. Machine > Tools > Snapshots
1. Click `Take`
1. Name it something useful, like "Ubuntu 22.04.1 + guest additions + caffeine, curl, gcc, git, jq, make, perl"
1. Give it a useful description explaining what you have done so far. For exmaple:
	```
	A clean install of Ubuntu 22.04.1 with default settings. I installed caffeine, curl, gcc, git, jq, make, and perl. Then I installed VirtualBox guest additions and created a Work folder. Icons were rearranged.
	```
1. Click `OK`.

### Restore from a Snapshot
If you followed the whole guide, you can now restore any of your Ubuntu virtual machines to the state of a clean install with no modifications, an installation with guest additions and minimal tools, or any other point in time where you took a snapshot. You can use the snapshot process described previously to create as many snapshots at different points in time as you want.

1. Select the virtual machine on the left
1. Machine > Tools > Snapshots
1. Click the snapshot you wish to restore from
1. Click `Restore`
1. Choose whether or not to take a snapshot of the current state
   - If you don't create a snapshot of the current state of your virtual machine, it will be gone forever
1. Click `Restore`
1. If you left `Create a snapshot of the current virtual machine state` checked, follow the steps to create a new snapshot with a useful name and description
1. Click `Current State`
   - Sometimes it says `Current State (changed)`, don't worry about it...this will be the machine restored from your snapshot
1. Click `Start`

## Security Concerns
Resuming a virtual machine from a snapshot or copying your virtual machine in any way (to another computer or on the same computer) has security implications. Mainly, the random number generator used for stuff like HTTPS or SSH could re-use the same random numbers. If you copy your virtual machine or resume from a snapshot then should assume none of those connections are actually safe. If you need them to be secure, do not restore snapshots, do not copy your virtual machine files (e.g. to another computer), and do not use virtual machines that you recovered from a hard drive backup like Apple Time Machine, Carbonite, Backup Tool, or similar.

While your host is mostly (but not entirely) protected from what happens in the guest, the guest is never more secure or safe than your host.
