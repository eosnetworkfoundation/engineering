# AWS Account Migration
This document outlines the process to migrate an AWS account from one organization to another.

The EOS Network Foundation (ENF) Automation team had the foresight to create all cloud infrastructure in granular Amazon Web Services (AWS) accounts, one for each system or environment, making this process as straightforward as possible!

<!-- contents box begin -->
<table>
<tr/>
<tr>
<td width="225">
<p/>
<div align="center">
<b>Contents</b>
</div>
<p/>
<!-- contents markdown begin -->

1. [Architecture](#architecture)
1. [See Also](#see-also)

<!-- contents markdown end -->
<p/>
</td>
</tr>
</table>
<!-- contents box end -->

## Architecture
The existing ENF AWS account architecture looks like this.
```mermaid
---
title: AWS Account Architecture
---
flowchart LR
    subgraph enf["`☁️ **ENF AWS**`"]
        subgraph mgmt["`🏛️ **Management Account**`"]
            direction LR
            reports["📊 Cost Reports"]
            billing["💲 Consolidated Billing"]
            policy["📜 Organization Policy"]
            org["🏢 Organization"]

            billing -.-> reports
            billing -.- org
            org -.- policy
        end

        chickens["🐓 chickens-prod Account<br/><br/>Replay Testing"]
        devhub["📚 devhub Account<br/><br/>Learn Portal"]
        docs["📑 docs-prod Account<br/><br/>Docs Portal"]
        mainnet["⛓️ evm-mainnet Account<br/><br/>EVM Mainnet Endpoints"]
        testnet["🛠️ evm-testnet Account<br/><br/>EVM Testnet Endpoints"]
    end

    org ===> chickens
    org ===> devhub
    org ===> docs
    org ===> mainnet
    org ===> testnet
```
Each child account is a "member" of the management account's "organization". The organization policy in the management account enforces consolidated billing, and prevents child accounts from leaving the organization.

## See Also
More resources.
- [./Development Process](./README.md) ⤴
- [../Engineering](../README.md) ⤴⤴
- EOS-EVM Documentation
    - [Cloud Architecture](https://github.com/eosnetworkfoundation/evm-public-docs/blob/main/cloud/README.md)
    - [eos-evm-internal](https://github.com/eosnetworkfoundation/eos-evm-internal) - internal-facing documentation of a [sensitive](https://github.com/eosnetworkfoundation/engineering/blob/main/standards/secrets.md) nature.
    - [Runbooks](https://github.com/eosnetworkfoundation/evm-public-docs/blob/main/runbooks/README.md)

***
> **_Legal Notice_**  
> This document was created in collaboration with a large language model, machine learning algorithm, or weak artificial intelligence (AI). This notice is required in some countries.