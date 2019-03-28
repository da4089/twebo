




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


Roadmap
=======

Phase 1
-------

* Subscribe by groups
* Subscriptions are persistent
* “Delivery” is a match between a published message and an active
  subscription
  * The result is that your queue gets a pointer/handle/id for the
    message
* Any message that matches at least one subscription is persisted
  indefinitely
  * Corollary: any message that doesn’t match a subscription can be
    discarded immediately
* When you delete a message, it’s flagged, but not (yet) removed from
  your queue
  * You might one day be able to, eg.. search deleted messages,
    un-delete a message, etc.
* When you kill a thread, you flag the Message-Ids for things killed,
  and delete replies before display
  * In fact, is the “thread-killed” just a flag on the messages in your
    history?
* You can attach from multiple devices.
  * Things you’ve seen on one device are marked as seen on another.
* UI
  * Login
  * History window
    * Thread view, like XTickertape
    * Compose pane (top? Bottom? configurable?)
    * Timestamp (configurable zone; maybe two zones one day?)
    * Show all groups by default
      * Allow filtering of both group and content (phase 2)
    * Unread messages are bold (?)
    * Attachments are underlined (?)
    * Secure messages have a padlock (?)
  * Scroller window
    * Very like XTickertape
    * Can set per-group maximum timeout
      * Including zero, meaning not shown in scroller
  * Preferences page
    * Subscribed groups
    * Keys
    * Maximum timeout
* Clients
  * WebSockets HTML client
  * XTickertape port to new backend
* MongoDB or Postgres backend

Phase 2
-------

* Multi-server
  * Configuration download
  * Multiple connections

Phase 3
-------

* Filters on subscriptions
  * Add to subscripton preferences
  * Messages that don't match the filter expression are killed
  * Needs to support both "subscribe" and "filter" models

Phase 4
-------

* Encryption of message text and attachments


When you log in, you get a dump of your subscribed groups (since this
might be altered by other of your clients, it should be maintained by
the server.

You then get a dump of all unread messages, ultimately ordered by time.
For each channel, unless there's some heuristic number of new messages,
the client will also request the most recent n messages for that group.

When a client requests a new subscription, or deletes an existing one,
a broadcast message to all clients for that user enables each client to
update itself in real time.

How does the client know what server(s) to connect to?  This will depend
on what the end user has requested.  How is this shared between clients?
I don't think it makes sense for server's to keep track of "foreign"
subscriptions for their clients?

Can't really use DNS or LDAP or anything.  So perhaps there needs to be
a configuration server as a first step?  Perhaps you log in there, and
get a list of server URLs?  Or group URLs?


Issues
======

When / how are older messages downloaded?  When you scroll to the top?
We kinda want to get n messages for the *user*, not per *group*.  That
has major impact on the API.

Presence.  And/or typing indication.

Garbage collection of deleted and/or thread-killed messages.

Subscription permissions, with consequences for group creation.


Data Model
==========

User / Account
- Login + password
- List of subscriptions
  - With maybe some local/remote differences

Subscription
- User reference
- Group name

Message
- From, Group, Message, Attachments, Id, In-Reply-To, etc

Delivery
- Message reference
- User reference
- Subscripton reference?
  - This could go away, if it's subsequently unsubscribed

Queries
-------

- Insert new user
- Disable user
- Enable user
- Set user's password
- Delete user

- Insert subscription
- Delete subscription
- Get subscriptions for group
- Get subscriptions for user

- Insert new message

- Insert delivery record
- Get delivered messages
- Read delivered message
- Delete delivered message
- Kill delivered thread
- Delete delivery
- Get un-read deliveries for user

