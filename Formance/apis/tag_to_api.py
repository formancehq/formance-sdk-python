import typing_extensions

from Formance.apis.tags import TagValues
from Formance.apis.tags.accounts_api import AccountsApi
from Formance.apis.tags.balances_api import BalancesApi
from Formance.apis.tags.clients_api import ClientsApi
from Formance.apis.tags.mapping_api import MappingApi
from Formance.apis.tags.payments_api import PaymentsApi
from Formance.apis.tags.scopes_api import ScopesApi
from Formance.apis.tags.script_api import ScriptApi
from Formance.apis.tags.search_api import SearchApi
from Formance.apis.tags.server_api import ServerApi
from Formance.apis.tags.stats_api import StatsApi
from Formance.apis.tags.transactions_api import TransactionsApi
from Formance.apis.tags.users_api import UsersApi
from Formance.apis.tags.webhooks_api import WebhooksApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.BALANCES: BalancesApi,
        TagValues.CLIENTS: ClientsApi,
        TagValues.MAPPING: MappingApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.SCOPES: ScopesApi,
        TagValues.SCRIPT: ScriptApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SERVER: ServerApi,
        TagValues.STATS: StatsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.USERS: UsersApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ACCOUNTS: AccountsApi,
        TagValues.BALANCES: BalancesApi,
        TagValues.CLIENTS: ClientsApi,
        TagValues.MAPPING: MappingApi,
        TagValues.PAYMENTS: PaymentsApi,
        TagValues.SCOPES: ScopesApi,
        TagValues.SCRIPT: ScriptApi,
        TagValues.SEARCH: SearchApi,
        TagValues.SERVER: ServerApi,
        TagValues.STATS: StatsApi,
        TagValues.TRANSACTIONS: TransactionsApi,
        TagValues.USERS: UsersApi,
        TagValues.WEBHOOKS: WebhooksApi,
    }
)
