

A Twebo server maintains a collection of messages, a collection of user
accounts, and a collection of associations between them.  If a user was
registered and subscribed when a matching messages was submitted, the
association between them is made.

Federation establishes connections between servers.  Each server can
subscribe to the union set of its local subscriptions from its
federated peer.

This means that there are two copies of the message kept: one at the
"source", associated with the "destination" server, and one at the
destination, associated with one or more of its local subscribers.

Should the servers become disconnected, the subscriptions persist, and
thus any matching messages will be delivered once they are
reconnected.

Scaling this out however, means that every server tends towards having
at least one subscriber to every channel, and thus, will receive every
message.  That doesn't work.

What's the alternative?

If a client didn't rely on federation to receive its "remote" traffic,
but instead connected directly to the source and registered its
subscription, the client would be naturally limited in its number of
subscriptions.  Servers then have to scale by number of subscribers,
which can be done basically using web-style load-balancers, with
messages broadcast to all replicas.  Clients need a persistent context
such that their history follows them as replicas change.

This would require identifying the "host" server for a group.  A domain
name is not unreasonable here: it can represent a cluster of replicas
as required.

So, group names should have a short form, eg. "Chat" which defaults to
being locally resolved.  In their long form, the domain name should be
included, eg. "Chat.example.com" or "Chat@example.com".

While there is some precedent for the dotted from with the old
"chat.world" naming from DSTC, I think I lean more towards the @ form,
as it makes clear the difference between the group name and the host
server identification.

