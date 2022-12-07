# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from Formance.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    CLIENTS = "Clients"
    PAYMENTS = "Payments"
    SCOPES = "Scopes"
    SEARCH = "Search"
    USERS = "Users"
    WEBHOOKS = "Webhooks"
    ACCOUNTS = "accounts"
    BALANCES = "balances"
    MAPPING = "mapping"
    SCRIPT = "script"
    SERVER = "server"
    STATS = "stats"
    TRANSACTIONS = "transactions"
