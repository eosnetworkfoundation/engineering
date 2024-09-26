# Encryption
Various techniques for securely working with sensitive data on Linux.

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

1. [Asymmetric Encryption](#asymmetric-encryption)
    1. [Create a PGP Key Pair](#create-a-pgp-key-pair)
    1. [View Your Key Pair](#view-your-key-pair)
    1. [Share Your Public Key](#share-your-public-key)
    1. [Import a Public Key](#import-a-public-key)
    1. [Encrypt a Message](#encrypt-a-message)
    1. [Decrypt a Message](#decrypt-a-message)
1. [Symmetric Encryption](#symmetric-encryption)
    1. [Encrypt](#encrypt)
    1. [Decrypt](#decrypt)
1. [See Also](#see-also)

<!-- contents markdown end -->
<p/>
</td>
</tr>
</table>
<!-- contents box end -->

## Asymmetric Encryption
Asymmetric encryption uses a pair of keys to encrypt and decrypt data, a public key that can be shared with anyone and a private key that needs to be kept secret. The public key is used to encrypt secret data, resulting in cyphertext that can be sent over the Internet. The recipient uses their private key to decrypt it. This is useful for securely sharing data with others.

To securely share secrets with others, for example to send service account credentials with a colleague on your team who does not use a [password manager](https://bitwarden.com), you can use PGP.

### Create a PGP Key Pair
Before you can send or receive PGP messages, you need to create a key pair. You can do this with [GnuPG](https://gnupg.org).
1. Install `gpg` if you don't already have it.
    - On Debian-family Linux:
        ```bash
        sudo apt-get install -y gpg
        ```
    - On macOS, you can install it using [Homebrew](https://brew.sh):
        ```bash
        brew install gnupg
        ```
    - On Windows, you can install it using [Chocolatey](https://chocolatey.org):
        ```powershell
        choco install gpg
        ```
1. Use your [password manager](https://bitwarden.com) to generate a strong, unique passphrase for your key pair. You will need this passphrase to decrypt messages.
1. Generate a new key pair.
    > When you run this next command, it will ask you for a passphrase to protect your key...and you will not be able to click outside the dialogue box. So, if you use a password manager, copy your passphrase to your clipboard before running this command.
    ```bash
    gpg --batch --gen-key <<TXT
    Key-Type: RSA
    Key-Length: 4096
    Subkey-Type: RSA
    Subkey-Length: 4096
    Name-Real: Bill Gates
    Name-Email: someone@example.com
    Expire-Date: 2024-10-01
    TXT
    ```
    If that command doesn't work for you then you can generate a key pair manually by answering some questions. Pick either "RSA and RSA" and use a key length of at least 2048 bits, or pick "ECC and ECC" and use `ed25519` or any `NSIT` curve with a key length of at least 256 bits.
    ```bash
    gpg --full-generate-key
    ```
    On the last step, be sure to press `o` for "okay" to generate the key pair.

### View Your Key Pair
You can see what key pairs you have on your computer using this command.
```bash
gpg --list-keys
```

### Share Your Public Key
You need to share your public key to receive encrypted messages. This command will print it out:
```bash
gpg --armor --export someone@example.com
```
You can then copy and paste the output into an email or IM, including the `-----BEGIN PGP PUBLIC KEY BLOCK-----` and `-----END PGP PUBLIC KEY BLOCK-----` lines. Alternatively, you can save it to a file and attach that to your message.
```bash
gpg --armor --export someone@example.com > public-key.asc
```

### Import a Public Key
If someone sends you their public key, you can import it using this command:
```bash
gpg --import public-key.asc
```
Or, if you are copying and pasting it from an email or IM, you can do this:
```bash
gpg --import <<TXT
```
Then paste the key block, and finish with:
```bash
TXT
```
You will see their name, email, and key here:
```bash
gpg --list-keys
```

### Encrypt a Message
You can encrypt a message using someone's public key. This command will encrypt a file:
```bash
gpg --encrypt --recipient someone@example.com message.txt
```
This will create a new file in the current directory called `message.txt.gpg` which you can send to the recipient.

You can encrypt any file, such as an archive.
```bash
gpg --encrypt --recipient someone@example.com archive.tar.gz
```
This would create `archive.tar.gz.gpg`.

You can also encrypt text directly:
```bash
echo 'Hello, World!' | gpg --encrypt --armor --recipient someone@example.com
```
This will print out the encrypted message, which you can copy and paste into an email or IM.

### Decrypt a Message
If someone sends you a PGP message, you can decrypt it using your private key and passphrase.

To decrypt a file:
```bash
gpg --decrypt message.txt.gpg
```
Or an archive:
```bash
gpg --decrypt archive.tar.gz.gpg
```
This will leave the file in the current directory.

To decrypt text directly:
> When you run this command, it will ask you for your passphrase to decrypt the message...and you will not be able to click outside the dialogue box. So, if you use a password manager, copy your passphrase to your clipboard before running this command.
```bash
echo '-----BEGIN PGP MESSAGE-----' | gpg --decrypt
```
This will print out the message in your terminal.

## Symmetric Encryption
Symmetric encryption uses the same key to encrypt and decrypt data. This is useful for encrypting data at rest, such as a backup file or a database dump.

### Encrypt
You can compress and encrypt a file using a symmetric key like this:
```bash
gpg --quiet --symmetric --cipher-algo AES256 --s2k-digest-algo SHA512 --s2k-mode 3 --s2k-count 65011712 --compression bzip2 --bzip2-compress-level 9 example.txt
```
This will leave a file called `example.txt.gpg` in the current directory.

You can encrypt an archive like this. We will leave off the compression this time.
```bash
gpg --quiet --symmetric --cipher-algo AES256 --s2k-digest-algo SHA512 --s2k-mode 3 --s2k-count 65011712 example.tar.gz
```
The output file would be `example.tar.gz.gpg`.

### Decrypt
Decryption is trivial with `gpg`.
```bash
gpg --output example.tar.gz --decrypt example.tar.gz.gpg
```
You don't have to specify the cipher or digest algorithms, or the compression level, because `gpg` will figure that out from the encrypted file.

## See Also
Internal resources.
- [./Tooling](./README.md) ⤴
- [../Engineering](../README.md) ⤴⤴

External resources.
- [Bitwarden](https://bitwarden.com) - password manager
- [GnuPG](https://gnupg.org) - the GNU Privacy Guard encryption, decryption, and signing tool

---
> **_Legal Notice_**  
> This document was created in collaboration with a large language model, machine learning algorithm, or weak artificial intelligence (AI). This notice is required in some countries.
