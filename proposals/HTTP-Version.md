# Proposal for Versioning HTTP API

| Issue Owner  | Eric Passmore |
| Date Created | Feb 26 2023   |
| GH Issue     | [25](https://github.com/eosnetworkfoundation/engineering/issues/25) |

## Version API

### Problem Statment
Currently the nodeos HTTP APIs are tightly bound to the release version of leap. There may be cases where multiple versions of the HTTP API may need to co-exist during a period of transition, or it might be useful to separate the semantic versioning of the HTTP API from nodeos versioning.
- breaking API changes
- signal new features of functionality
- reorganization URL structure to group feature sets or differentiate between feature sets

### General Solution
Every client HTTP call should specify the version of the API they would like to use. Clients would receive an HTTP error if they requested an API which is no longer supported.

### Implementation Options
1. Place Version Inside the URL Path, default to latest API when version not provided
   - http://example.com/service/v1/info
2. **Recommended** Version is Request Parameter to URL, default to latest API  
   - http://example.com/service/into?version=1

Recommend `#2`. Easier to for clients to assemble URLs, no positional and often there are helper libraries. Request parameters are easier to change overtime. General accepted that URL encoded characters may be placed in request params allowing for something like (v1%2E0%2E0 which is v1.0.0)
- Downside of `#2` proxies and intermediates can accidently strip request parameters.
- Clients may view request parameters as optional.

Error codes for unsupported versions
1. **Recommended** 400 - simple, client error, return error message
2. 301 - redirect to correct version

Recommend 400 `#1`. Simple and effective. Redirecting clients to proper URL doesn't not mean clients are ready to handled the updated version. A redirect may cause other issues are clients operate in a semi-working state.

Note: error code 426 is used for HTTP protocol. It should not be used for service version level support.


## Version Schema

## Serialization Version

## State Management  
