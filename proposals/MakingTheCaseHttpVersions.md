# What HTTP Version

standardize on HTTP 2.0

# Capabilities Unique to HTTP 2.0

## Connection Management
Configurable setting to close idle connections. Supported via [`PING`](https://httpwg.org/specs/rfc9113.html#rfc.section.6.7) frame, and graceful connection closure via the [`GOAWAY`](https://httpwg.org/specs/rfc9113.html#rfc.section.9.1) frame. Most HTTP servers support a ReadIdleTimeout used to inform when to close connections.

## Streams
Many HTTP connections over a single TCP. Does is accomplished over a stream which enables both Multiplexing HTTP connections and bidirectional packets. Streams may be prioritized via the [`PRIORITY`](https://httpwg.org/specs/rfc7540.html#PRIORITY) Frame.

## Flow Control
Ability for receivers to advertise their flow control limits via a [`WINDOW_UPDATE`](https://httpwg.org/specs/rfc9113.html#WINDOW_UPDATE) frame on the stream. Servers can asynchronously prefect [`PUSH_PROMISE`](https://httpwg.org/specs/rfc9113.html#PUSH_PROMISE) data.

## Header Compression
[Headers are compressed](https://datatracker.ietf.org/doc/html/rfc7541)

# Advantages of HTTP 2.0
## Better TLS Support
**note need to look into why this is true**
Originally HTTP2 enforced TLS, but that isn't the case in 2023. See [TLS Spec in HTTP2 FAX](https://httpwg.org/specs/rfc9113.html#TLSUsage)

## Lower Latency
SPDY and Reusing TCP connections. Bidirectional packets over streams allows shared TCP for request and response

## Websocket support
Browser support for websockets over HTTP is limited to secure connections using HTTP2. Otherwise websockets are TCP.

## Network Optimization for Mixed Workloads
Can send data up to the limits of the receiving client. Good when network requirements vary by endpoint or request type. These are set via the `WINDOW_UPDATE`, `PUSH_PROMISE`, and `PRIORITY` frames.

# Less network bandwidth
Headers are compressed. Custom client/server implementations can make use of

# Moving to HTTP 2

## TCP
advise setting `TCP_NODELAY` when using HTTP2

## TLS
advise TLS to support websockets

# Reference
- https://web.dev/performance-http2/
- https://http2.github.io/faq/
- https://datatracker.ietf.org/doc/html/rfc7541
