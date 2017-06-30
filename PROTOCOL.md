WebSockets Protocol
===================

Login Request
{
    "Request-Id": string,
    "User-Id": string,
    "Password": string
}

Login Response
{
    "Request-Id": string,
    "Result": int32_t,
    "Channels": [
        {
            "Channel": string,
            "Last-Sequence": int64_t,
            "Active": bool
        }
    ]
}

Create Channel Request
{
    "Request-Id": string,
    "Channel": string
}

Create Channel Response
{
    "Request-Id": string,
    "Result": int32_t,
    "Channel": string
}

Modify Channel Request
{
    "Request-Id": string,
    "Channel": string,
    "Active": bool
}

Modify Channel Response
{
    "Request-Id": string,
    "Result": int32_t,
    "Channel": string,
    "Active": bool
}

Subscription Request
{
    "Request-Id": string,
    "Channel": string
}

Subscription Response
{
    "Request-Id": string,
    "Channel": string,
    "Result": int32_t,
    "Last-Sequence": uint64_t
}

Messages Request
{
    "Request-Id": string,
    "Channel": string,
    "First-Sequence": int64_t,
    "Last-Sequence": int64_t,
    "Max-Count": int64_t,
}

Message
{
    "Channel": string,
    "Sequence": int64_t,
    "Timestamp": int64_t,
    "Message-Id": string, (????)
    "In-Reply-To": string, (????)
    "Followups-To": string, (????)
    "Text": string,
    "Attachments": [
        "Content-Type": string,
        "Content-Transfer-Encoding": string,
        "Content-Disposition": string,
        "Body": string
    ]
}

Message-Ack
{
    "Channel": string,
    "Sequence": int64_t
}
