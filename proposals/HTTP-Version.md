# Proposal for Versioning HTTP API

| Name         | Value         |
|--------------|---------------|
| Moderator    | Eric Passmore |
| Date Created | Feb 26 2023   |
| GH Issue     | [25](https://github.com/eosnetworkfoundation/engineering/issues/25) |
| Date Revised | Mar 08 2023   |
| Revision     | Shift to JSON RPC |

## Version API

### `Problem Statement`
The HTTP API should be used for the URL organization, standardization of return codes, and standardization for rarely used methods like PATCH.

### `Quick Example`
Our API is HTTP/2.0, and we would use POST for almost everything. For example
`get_account` would be a POST to `example.com/antelope/account` with JSON
```jsonc
{
  "jsonrpc": "2.0",
  "method": "get_account",
  "params": "enfsession11",
  "id": "my-memo-or-ref-id"
}
```

We don't use DELETE, GET, PATCH, PUT. There a limited uses for HEAD.

Later in this doc we discuss why you might want to have `antelope` or `account` in the URL. Strictly speaking for JSON-RPC 2.0 neither of these are required in the URL.

Here is an example of an error response. 
```jsonc
{
  "error": {
    "code": -1,
    "message": "Path not valid - unknown element 'somethingwrong'. Options are [features, trace-options, management, configuration, aaa, authentication, warm-reboot, boot, l2cp-transparency, lacp, lldp, mtu, name, dhcp-server, event-handler, ra-guard-policy, gnmi-server, tls, json-rpc-server, bridge-table, license, dns, ntp, clock, ssh-server, ftp-server, snmp, sflow, load-balancing, banner, information, logging, mirroring, network-instance, maintenance, app-management]"
  },
  "id": 0,
  "jsonrpc": "2.0"
}
```

### `Solution Overview`
We should settle on HTTP/2.0. We should use standard methods, return codes and headers. We should stay away from grey areas like PATCH.

We need a leading directory name for URL namespace organization.  

### `Implementation`
URL namespaces are long lived. We should use the current project iteration of `antelope` to start URLs
- https://example.com/antelope/transaction

The leading project name in the URL will be changed when a major reorganization of the URL structure occurs, or when the project iteration changes.

Error codes for unsupported versions are not needed because we are using standard HTTP.

## Version Schema

### `Problem Statement`
Changes may occur at the content and schema level, below the API. For example the JSON for greylist accounts may add an additional mandatory field, while the URL path, HTTP Methods, HTTP Header, and return code remain the same. We don't want to version the entire API for this isolated change.

Types of changes
- Mandatory changes, adding or removing a field uses as a key, or a significant behavior change
- Optional changes, optional parameters provided or returned
We tend to care only about the Mandatory changes. Clients do not validate schemas. Mandatory changes are rare, and they tend to have a clear purpose. Clients do not validate schemas. Mandatory changes are rare, and they tend to have a clear purpose.

### `Solution Overview`
We shift to an RPC style payloads using `method` and `parameters`. The method name acts like function calls. We deal with version management by updated the method name.

### `Survey of Usage` circa 2023
Blockchains use jsonrpc as for the schema version. Across ETH, AVAX, and NEAR they all use the [jsonrpc spec](https://www.jsonrpc.org/specification).

### `Implementation`
[jsonrpc](https://www.jsonrpc.org/specification)

## Serialization Version

### `Problem Statement`
This is a nice to address problem; it is not a must solve problem. The key take away, if protocol serialization options are supported do not use the [`Accept` Header for content negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation#the_accept_header). The `Accept` Header is used for well know MIME types.

Protocol for serialization and deserialization is a separate layer of functionality. It is separate from the HTTP API, and separate from the schema. Yet serialization and deserialization may change in a way that breaks previous client implementations. Or we may want to offer multiple types of serialization across our API. Admittedly serialization is a low level part of the protocol, and we don't want every API call to specify a serialization protocol.

### `Solution Overview`
Strike the right balance. The default serialization protocol is set API wide. Some API endpoints, specific URL paths, may be configured to change their serialization protocol. Changing the serialization protocol requires updating configuration settings per instance. Ideally serialization protocol changes could be made dynamically while the service was running.  

### `Implementation`
Items numbers for ease of reference
1. Peer to Peer communication must be interoperable. Best to enforce a serialization protocol for everyone.
- If there is a choice on serialization protocols, it must be implicit or it must be negotiated between peers
2. URL organization for specific content types. For example the two cases below:
- Raw Block and Raw Block headers just need their own URL. That URL implicitly provides byte output.
- Nodes configuration is implicitly JSON

Item `3` is an interesting case that does not exist today.
3. Nodes configuration by URL when multi-serialization protocols are offered
- For example if there was an option to switch between protobuff and abieos
- Or if there was an option to configure nodeos with JSON or YAML

For best use, the URL would be organized into groups by primary customer. Each group could be configured to use a specific serialization protocol This may result the following organizational structure
- producers - for block producers
- transactions or accounts - for customer facing endpoints like accounts, transactions, etc
- block - for L2 applications wanting a raw interface  

Historical note, in the past it was fairly common to put the protocol serialization as a [`Accept` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept). W3C did not officially add protobuffer or any serialization protocol to the official MIME types, and the practice of using `Accept` header stopped. Custom headers also fell out of practice. That left the service side configuration and the remaining practice for configurable serialization. See working example from [Kafka Serialization Part of Message Schema](https://docs.confluent.io/platform/current/schema-registry/serdes-develop/serdes-protobuf.html#protobuf-schema-serializer-and-deserializer)

## Endpoints

### `What Are Endpoints`
Function calls are placed inside the json metadata, and there is no need for a URL structure. To encourage proper organization of service side functionality, and to group together similar functions it is nice to have specific endpoints. The endpoints should be a set of features or a group of consumers.

### `Layer 7`
The only reason that requires endpoints is routing or securing URLs by their path. For example if you wanted to restrict `antelope/producer` URLs to originate from a specific IP range you could configure that in an HTTP Proxy.

### `EOS Examples`
In EOS we currently have the following
- chain
- producer
- net
- db_size
- trace

Full URL examples with JSON request
- http://example.com/antelope/chain
```
{
  "jsonrpc": "2.0",
  "id": "dontcare",
  "method": "get_account",
  "params": {
    "account_name": "enfsession11",
  }
}
```

### `Recomendation`
Create endpoints that match usage patterns. This might be the following:  
- accounts
- contracts
- blocks
- resources or fees
- protocol
- network or peers
- transactions

## State Management

### `Problem Statement`
Blockchain as a distributed ledger solves this problem. There are cases where configuration is managed outside of the blockchain, where order of operations is needed.

With HTTP API it is possible for multiples clients to send updates that conflict with each other. Both clients make different updates based on the current state. The last update in will win. The client with the first-to-be-consumed update will have no idea their change is no longer valid.

There is a common error pattern where clients send an empty state or zero-length update, and effectively delete their own content.   

### `Solution Overview`
Utilize a hash or weak key, `E-Tag` for the content state along with a `If-Match` directive. Updates are only allowed when the `E-Tag` on the request matches with the content.

This is useful for nodeos configuration changes.

### `Implementation`
Details of are outlined under [HTTP If-Match Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). Failures on Read request return 304 *Not Modified*. Failures on Write request return 412 *Precondition Failed*

## Vary Header
The [`Vary` Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary) indicates the parts of the message the influence the content outside of the URL and method. All versioning changes outside of the URL and method must be specified in the `Vary` Header.
