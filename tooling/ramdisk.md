# RAMdisk
You can mount some of your computer's memory to your filesystem in order to perform read/write intensive tasks very, very quickly such as processing large JSON files, or to [work with sensitive documents](./encryption.md) that you don't want to risk writing to disk. This is called a RAM disk.

<!-- contents box begin -->
<table>
<tr/>
<tr>
<td>
<p/>
<div align="center">
<b>Contents</b>
</div>
<p/>
<!-- contents markdown begin -->

1. [Preparation](#preparation)
1. [Creation](#creation)
1. [Destruction](#destruction)
1. [See Also](#see-also)

<!-- contents markdown end -->
<p/>
</td>
</tr>
</table>
<!-- contents box end -->

## Preparation
Make a folder to mount the RAM disk to.
```bash
sudo mkdir -p /mnt/ram
```
Take ownership of that folder.
```bash
sudo chown "$USER:$USER" /mnt/ram
```
Put a file there so you can tell whether or not a RAM disk is mounted.
```bash
echo 'WARNING: If you can see this, there is currently no RAM disk mounted!' > /mnt/ram/STOP.txt
```

Optionally, install `wipe` if you want to delete the contents of your RAM disk immediately instead of waiting for the system to overwrite it.
```bash
sudo apt-get update
sudo apt-get install -y wipe
```

## Creation
Mount a 16 GB RAM disk.
```bash
sudo mount -o size=16G -t tmpfs none /mnt/ram
```
Verify your `STOP.txt` file is gone.
```bash
ls -la /mnt/ram
```
Now you can work there.

## Destruction
Optionally, you can overwrite the contents of your RAM disk immediately instead of waiting on your system to do it after unmounting.
```bash
wipe -fr /mnt/ram/*
```
Unmount the RAM disk.
```bash
sudo umount /mnt/ram
```
Verify your `STOP.txt` file is back.
```bash
ls -la /mnt/ram
```

## See Also
Internal resources.
- [./Tooling](./README.md) ⤴
- [../Engineering](../README.md) ⤴⤴

---
> **_Legal Notice_**  
> This document was created in collaboration with a large language model, machine learning algorithm, or weak artificial intelligence (AI). This notice is required in some countries.
