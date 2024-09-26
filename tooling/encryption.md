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

## See Also
Internal resources.
- [./Tooling](./README.md) ⤴
- [../Engineering](../README.md) ⤴⤴

---
> **_Legal Notice_**  
> This document was created in collaboration with a large language model, machine learning algorithm, or weak artificial intelligence (AI). This notice is required in some countries.

