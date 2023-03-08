# Proposal for Versioning HTTP API

| Name         | Value         |
|--------------|---------------|
| Moderator    | Eric Passmore |
| Date Created | Feb 26 2023   |
| GH Issue     | [25](https://github.com/eosnetworkfoundation/engineering/issues/25) |

## Version API

### `Problem Statement`
The HTTP API should be used for the URL organization, standardization of return codes, and standardization for rarely used methods like PATCH. The relationship between the HTTP API and the json schema is limited. It is true to say the HTTP API requires the schema to have a version.

The current API has a version embedded inside the URL. Most clients have hardcoded the version id and it would be difficult for them to switch to the latest version.
- [Eosio Core needs a new release](https://github.com/greymass/eosio-core/tree/master/src/api/v1)
- Developers needs to pick up the new eosio-core release
- Developers need to go through all their calls and change `client.v1.` to `client.v2`

### `Solution Overview`
Move the version string to a URL parameter. Leaving off the version will default to the latest API. Clients will receive an HTTP error if they requested an API version which is not supported.

### `Implementation Options`
1. Place Version Inside the URL Path, mandatory not optional
   - http://example.com/v1/service/info
2. ![#Rec](https://placehold.co/120x25/c5f015/000000/png?text=Recommended) Version is Request Parameter to URL, default to latest API  
   - http://example.com/service/into?eosapi=v1

Recommend `#2`. Leaving off the URL parameter, clients will be automatically upgraded to the latest version. It is easier for clients to assemble URL parameters. The parameter name adds additional context for the client. URL parameters as name value pairs are easier to parse on the service side. Versions can be any string, and by tradition URL encoded values are acceptable in parameter values.
- Downside of `#2` proxies and intermediates must be configured to respect request parameters.
- Depending on your point of view the auto version upgrade that occurs when leaving off the parameter is a downside or an upside.

*Question: when was the last time we changed the API version?*

Error codes for unsupported versions
1. ![#Rec](https://placehold.co/120x25/c5f015/000000/png?text=Recommended) 400 - simple, client error, return error message
2. 301 - redirect to correct version

Recommend 400 `#1`. Simple and effective. Redirecting clients to proper URL doesn't mean clients are ready to handle the updated version. A redirect may cause other issues and push clients into an undefined or unexpected state.

Note: error code 426 is used for HTTP protocol. It should not be used for service version level support.

Note: Options not considered. Versions in Custom HTTP Header, or Version in Accept header. These are opaque, difficult to switch between versions, and simple things like logging, routing, and proxying require additional configuration.

## Version Schema

### `Problem Statement`
Changes may occur at the content and schema level, below the API. For example the JSON for greylist accounts may add an additional mandatory field, while the URL path, HTTP Methods, HTTP Header, and return code remain the same. We don't want to version the entire API for this isolated change.

Types of changes
- Mandatory changes, adding or removing a field uses as a key, or a significant behavior change
- Optional changes, optional parameters provided or returned
We tend to care only about the Mandatory changes. Clients do not validate schemas. Mandatory changes are rare, and they tend to have a clear purpose. Clients do not validate schemas. Mandatory changes are rare, and they tend to have a clear purpose.

### `Solution Overview`
JSON schema's need their own version. We assume each distinct URL has one JSON schema. In addition, for simplicity we assume the client understands the requirements for the schema they are utilizing; therefore there is no schema negotiation between client and server.

### `Survey of Usage` circa 2023
Blockchains use jsonrpc as for the schema version. Across ETH, AVAX, and NEAR they all use the [jsonrpc spec](https://www.jsonrpc.org/specification). This indicates the method name in the URL is changing, and the jsonrpc field isn't used.

### `Implementation Options`
1. Place the Schema Name inside a customer HTTP Header
- X-EOS-Schema-Version: greylist-1.0.0
2a. ![#Rec](https://placehold.co/120x25/c5f015/000000/png?text=Recommended) Wrap the JSON in the Schema Name
- `greylist{}`
- `greylistwithstrikelimit{}`
2b. Follow [JSON-RPC](https://www.jsonrpc.org/specification) and put `method` name in the schema
3. Overload Method Name in URL with Schema Name
- HTTP PUT https://example.com/client/config
- HTTP PUT https://example.com/client/update_greylist
- HTTP PUT https://example.com/client/update_greylist_with_strike_limit

Recommend `#2a` wrap JSON with Schema Name. The Schema name would only change when mandatory fields were added/removed, or there was a significant change in behavior. Mandatory field changes are not common, and the schema name would be fairly stable. Optional field changes should be both backwards and forwards compatible. For that reason, optional field changes would keep the same schema name. `#2a` is simple, effective, and human readable.

Using JSON-RPC `#2b` is less obvious. The `method` name is at the same level as other less important fields.

Some consideration should be given to the style of the version name. This author prefers human readable names, and likes to stay away from embedding version numbers into schema names.

Option `#1` custom headers aren't part of most APIs. It would be difficult to onboard new clients. Consider the burden of calling URLs on the command line with HTTP headers.

Option `#3` is a legit option when URL and Schema have a 1-to-1 relationship. Option `#3` doesn't support multiple schemas in the same URL. In addition, `#3` can pollute the URL namespace with bad, poorly named URLs, as each new schema or experimental behavior requires a new URL. Putting the Schema Version or Schema Name inside the JSON payload is easier for rapid development or trying out features.

## Serialization Version

### `Problem Statement`
This is a nice to address problem; it is not a must solve problem. The key take away, if protocol serialization options are supported do not use the [`Accept` Header for content negotiation](https://developer.mozilla.org/en-US/docs/Web/HTTP/Content_negotiation#the_accept_header). The `Accept` Header is used for well know MIME types.

Protocol for serialization and deserialization is a separate layer of functionality. It is separate from the HTTP API, and separate from the schema. Yet serialization and deserialization may change in a way that breaks previous client implementations. Or we may want to offer multiple types of serialization across our API. Admittedly serialization is a low level part of the protocol, and we don't want every API call to specify a serialization protocol.

### `Solution Overview`
Strike the right balance. The default serialization protocol is set API wide. Some API endpoints, specific URL paths, may be configured to change their serialization protocol. Changing the serialization protocol requires updating configuration settings per instance. Ideally serialization protocol changes could be made dynamically while the service was running.  

### `Implementation`
For numbers `1` and `2` below tightly couple the serialization protocol to the HTTP API Version.

1. Peer to Peer communication must be interoperable. If there is a choice on serialization protocols, it must be implicit or it must be negotiated between peers
2. URL organization for specific content types
- For example Raw Block and Raw Block headers just need their own URL. That URL implicitly provides byte output.
- Nodes configuration is implicitly JSON

Option `3` is an interesting case that does not exist today.
3. Nodes configuration by URL when multi-serialization protocols are offered
- For example if there was an option to switch between protobuff and abieos
- Or if there was an option to configure nodeos with JSON or YAML

For best use, the URL would be organized into groups by primary customer. Each group could be configured to use a specific serialization protocol This may result the following organizational structure
- config - for block producers
- eos - for customer facing endpoints like accounts, transactions, etc
- raw - for L2 applications wanting a raw interface  

Historical note, in the past it was fairly common to put the protocol serialization as a [`Accept` header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept). W3C did not officially add protobuffer or any serialization protocol to the official MIME types, and the practice of using `Accept` header stopped. Custom headers also fell out of practice. That left the service side configuration and the remaining practice for configurable serialization. See working example from [Kafka Serialization Part of Message Schema](https://docs.confluent.io/platform/current/schema-registry/serdes-develop/serdes-protobuf.html#protobuf-schema-serializer-and-deserializer)

## State Management

### `Problem Statement`
Blockchain as a distributed ledger solves this problem. There are cases where configuration is managed outside of the blockchain, where order of operations is needed.

With HTTP API it is possible for multiples clients to send updates that conflict with each other. Both clients make different updates based on the current state. The last update in will win. The client with the first-to-be-consumed update will have no idea their change is no longer valid.

There is a common error pattern where clients send an empty state or zero-length update, and effectively delete their own content.   

### `Solution Overview`
Utilize a hash or weak key, `E-Tag` for the content state along with a `If-Match` directive. Updates are only allowed when the `E-Tag` on the request matches with the content.

This is useful for nodeos configuration changes. It would be useful for Tables Updates as well.

### `Implementation`
Details of are outlined under [HTTP If-Match Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/If-Match). Failures on Read request return 304 *Not Modified*. Failures on Write request return 412 *Precondition Failed*

## Vary Header
The [`Vary` Header](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Vary) indicates the parts of the message the influence the content outside of the URL and method. All versioning changes outside of the URL and method must be specified in the `Vary` Header.
