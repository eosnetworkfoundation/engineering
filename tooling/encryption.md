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

## See Also
Internal resources.
- [./Tooling](./README.md) ⤴
- [../Engineering](../README.md) ⤴⤴

---
> **_Legal Notice_**  
> This document was created in collaboration with a large language model, machine learning algorithm, or weak artificial intelligence (AI). This notice is required in some countries.

