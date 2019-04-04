# -*- python -*-
######################################################################
# Copyright (C) 2017
######################################################################


class User:
    def __init__(self):
        self.nick = ''
        self.login = ''
        self.subscriptions = {}  # group: sub
        self.queue = []  # Delivery instances
        return


class Group:
    def __init__(self):
        self.name = ''
        return


class Subscription:
    def __init__(self):
        self.user = None
        self.group = None
        self.timestamp = 0
        return


class Message:
    def __init__(self):
        self.timestamp = 0
        self.group = None
        self.from_ = None
        self.message = ''
        self.in_reply_to = None
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
