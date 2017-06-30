In light of Slack, and Twist, I think there's life in this old dog ...

WebSockets is pretty easy.
A fairly minimal VanillaJS client should be ok.





Publishing
----------

Essentially, this is an insert operation on the channel's message
table.  It should allocate a sequence number, and trigger all
subscribers.

Subscription
------------
For each subscription created in the UI, the attached server must
maintain the client's identifier, and their last-seen sequence number.

Newly published messages are forwarded to clients, and the sequence
number acknowledged.

If the client is disconnected, the last-seen sequence number is not
updated, and so all channel messages in the gap can be retransmitted
following a reconnection.
