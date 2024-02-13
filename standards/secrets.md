# Secrets
We are an open-source software organization making as much code and documentation publicly available on the Internet as possible. Like any other organization, we also handle sensitive information and secrets. This document provides guidelines on what should be reserved from public view, and how to safely make this information available internally.

> [!WARNING]
> The list of examples provided in this document _are **not** exhaustive_!

## Classification
Information can be classified into three categories.
1. [Secret](#secret)
1. [Sensitive](#sensitive)
1. [Public](#public)

### Secret
Most secret information can be immediately used against us by attackers. Secrets should **_never_** be stored in or shared via email, IM, SMS, MMS, voice call, video call, social media, GitHub/GitLab, pastebin-type apps, note apps, cloud storage, text files, Word documents, spreadsheets, or similar. Secrets should never be logged by our code. If secrets are leaked via one of these means, even just a draft document, it needs to be reported and the secret rotated.

#### Storage
Local secrets must be stored in a [password manager](https://bitwarden.com), a [hardware security module](https://en.wikipedia.org/wiki/Hardware_security_module) (HSM) such as a [Yubikey](https://www.yubico.com/product/yubikey-5-series/yubikey-5-nfc) or your TPM chip, or your operating system's keyring. Cloud secrets must be stored in a cloud HSM or a proper secret manager such as [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [Google Cloud Secret Manager](https://cloud.google.com/security/products/secret-manager), the [AWS SSM Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), or equivalent.

#### Sharing
> [!TIP]
> If you find yourself sharing a secret, ask yourself _why_. There are very few legitimate circumstances in which secrets should be shared. For example, instead of sharing an SSH key, ask the recipient to generate their own key and add their public key to the target machine. Instead of generating a service account and sending the credentials to a coworker to put in the cloud, have one person generate and upload the secrets. Better yet, consider a [zero-trust](https://en.wikipedia.org/wiki/Zero_trust_security_model) architecture where there are no secrets.

Secrets can be safely shared using a [password manager](https://bitwarden.com), [PGP](https://en.wikipedia.org/wiki/GNU_Privacy_Guard), an end-to-end encrypted disappearing message on [Signal](https://signal.org) or [Matrix](https://matrix.org), or an end-to-end [encrypted email](https://proton.me/support/password-protected-emails) with a time-limit _and_ a password shared out-of-band.

> [!TIP]
> Take extreme care to verify the identity of your recipient _before_ sharing secrets.

#### Examples
- Access Tokens
- API Keys
- Encryption or Decryption Keys, Passphrases, or Passwords
- Multi-Factor Authentication (MFA) Codes
- Passwords
- Private Keys
- Seed Phrases
- Service Account Credentials
- Severe Security Vulnerabilities
- SSH Keys
- TOTP Secrets and QR Codes
- Two-Factor Authentication (2FA) Codes
- Wallets, Wallet Backups, or Wallet Files

### Sensitive
Information may be sensitive because it makes attacks easier, such as a public IP address to an AWS EC2 instance, or it may be sensitive for non-technical business reasons. Sensitive information may be stored or shared via organization email, internal IMs, private GitHub repos, private note apps, or on calls. While there may be circumstances in which sensitive information must be shared externally, such as while obtaining support from a vendor, it should _never_ be shared in public groups, via social media (public or private), or in a public GitHub repo.

> [!TIP]
> Always verify internal group chats, email chains, or calls do not contain unintended recipients.

#### Examples
- Amazon Web Services (AWS)
    - Account Number
    - Availability Zone (AZ)
    - Billing Information
    - Expenditure
    - Hostname
    - Instance ID
    - IP Address
    - Region
    - Amazon Resource Name (ARN)
- Contact Information of others
- IP Addresses
- Security Vulnerabilities
- Usernames

### Public
As an open-source software organization funded by and with obligations to our community, we strive to make as much information publicly available as is reasonable.

***
> **_Legal Notice_**
> This information is not legal advice and is not being provided on a professional basis. See the [license](../LICENSE) for terms.
