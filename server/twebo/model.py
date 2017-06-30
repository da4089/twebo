# -*- python -*-
######################################################################
# Copyright (C) 2017
######################################################################


class User(object):
    def __init__(self):
        self.nick = ''
        self.login = ''
        self.subscriptions = []
        return


class Channel(object):
    def __init__(self):
        self.name = ''
        return


class Subscription(object):
    def __init__(self):
        self.user = None
        self.channel = None
        self.last_seq = 0
        self.last_read = 0
        return


class Message(object):
    def __init__(self):
        self.time = 0
        self.channel = None
        self.user = None
        self.message = ''
        self.in_reply_to = None
        return


class Database(object):
    def __init__(self):
        self.users = {}
        self.channels = {}
        self.messages = {}
        return
