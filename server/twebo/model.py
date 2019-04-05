# -*- python -*-
######################################################################
# Copyright (C) 2017
######################################################################


class User:
    def __init__(self):
        self.nick = ''
        self.login = ''
        self.status = ''  # 'typing', 'active', 'idle', 'offline'
        self.groups = {}  # group: sub
        self.users = {}
        self.queue = []  # Delivery instances
        return


class Group:
    def __init__(self):
        self.name = ''
        return


class GroupSubscription:
    def __init__(self):
        self.user = None
        self.group = None
        self.start = 0
        return


class Presence:
    def __init__(self):
        self.user = None
        self.status = None
        return


class PresenceSubscription:
    def __init__(self):
        self.subscriber = None
        self.target = None
        return


class Message:
    def __init__(self):
        self.timestamp = 0
        self.message_id = None
        self.group = None
        self.from_ = None
        self.message = ''
        self.in_reply_to = None
        self.timeout = 0
        return


class Delivery:
    def __init__(self):
        self.user = None
        self.subscription = None
        self.message = None
        self.read = False
        self.killed = False
        return


class Server:
    def __init__(self):
        self.users = {}
        self.groups = {}
        self.messages = {}
        return


