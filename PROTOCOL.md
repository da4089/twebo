WebSockets Protocol
===================

- Connect WebSocket.
- Send Login Request
  - Include list of channels and last-seen sequence numbers for this
    client
- Receive Login Response
  - If bad result, disconnect web socket, and try new auth.
- Receive sequence of missed messages
  - Limit this to most recent n or something, so you don't get swamped
    after a year.


Login Request
{
    "MessageType": "v1.login_request",
    "RequestId": string,
    "UserId": string,
    "Password": string
    "Channels": [
        {
            "Channel": string,
            "LastSequence": int64_t
        }
    ]
}

Login Response
{
    "MessageType": "v1.login_response",
    "RequestId": string,
    "Result": int32_t,
    "Channels": [
        {
            "Channel": string,
            "LastSequence": int64_t,
            "Active": bool
        }
    ]
}

Create Channel Request
{
    "MessageType": "v1.create_channel_request",
    "RequestId": string,
    "Channel": string
}

Create Channel Response
{
    "MessageType": "v1.create_channel_response",
    "RequestId": string,
    "Result": int32_t,
    "Channel": string
}

Modify Channel Request
{
    "MessageType": "v1.modify_channel_request",
    "RequestId": string,
    "Channel": string,
    "Active": bool
}

Modify Channel Response
{
    "MessageType": "v1.modify_channel_response",
    "RequestId": string,
    "Result": int32_t,
    "Channel": string,
    "Active": bool
}

Subscription Request
{
    "MessageType": "v1.subscription_request",
    "RequestId": string,
    "Channel": string
}

Subscription Response
{
    "MessageType": "v1.subscription_response",
    "RequestId": string,
    "Channel": string,
    "Result": int32_t,
    "LastSequence": uint64_t
}

Messages Request
{
    "MessageType": "v1.messages_request",
    "RequestId": string,
    "Channel": string,
    "FirstSequence": int64_t,
    "LastSequence": int64_t,
    "MaxCount": int64_t,
}

Message
{
    "MessageType": "v1.message",
    "Channel": string,
    "Sequence": int64_t,
    "Timestamp": int64_t,
    "MessageId": string, (????)
    "InReplyTo": string, (????)
    "FollowupsTo": string, (????)
    "Text": string,
    "Attachments": [
        "ContentType": string,
        "ContentTransferEncoding": string,
        "ContentDisposition": string,
        "Body": string
    ]
}

Message Acknowledgement
{
    "MessageType": "v1.message_ack",
    "Channel": string,
    "Sequence": int64_t
}

Heartbeat
{
    "MessageType": "v1.heartbeat"
}
