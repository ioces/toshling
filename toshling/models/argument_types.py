from typing import Any, List

from statham.schema.constants import Maybe
from statham.schema.elements import (
    Array,
    Boolean,
    Element,
    Integer,
    Number,
    Object,
    String,
)
from statham.schema.property import Property


class AccountsListArgument(Object):

    ids: Maybe[str] = Property(String())

    include_deleted: bool = Property(Boolean(default=False))

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    since: Maybe[str] = Property(String(format='date-time'))

    status: Maybe[str] = Property(String(enum=['active', 'inactive', 'archived']))


class AccountsMergeArgument(Object):

    account: Maybe[str] = Property(String())

    accounts: List[Any] = Property(Array(Element()), required=True)

    currency: Maybe[str] = Property(String())

    sync: Maybe[List[Any]] = Property(Array(Element()))

    title: Maybe[str] = Property(String())


class AccountsReorderArgument(Object):

    order: List[Any] = Property(Array(Element()), required=True)


class AccountsDeleteArgument(Object):

    id: str = Property(String(), required=True)


class AccountsGetArgument(Object):

    id: str = Property(String(), required=True)


class AccountsForceDeleteArgument(Object):

    id: str = Property(String(), required=True)


class AccountsMoveArgument(Object):

    position: int = Property(Integer(minimum=0), required=True)


class BudgetsListArgument(Object):

    accounts: Maybe[str] = Property(String())

    categories: Maybe[str] = Property(String())

    expand: bool = Property(Boolean(default=False))

    from_: str = Property(String(format='date'), required=True, source='from')

    has_problem: Maybe[bool] = Property(Boolean())

    include_deleted: bool = Property(Boolean(default=False))

    one_iteration_only: bool = Property(Boolean(default=False))

    page: int = Property(Integer(default=0, minimum=0))

    parent: Maybe[str] = Property(String())

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    search: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    tags: Maybe[str] = Property(String())

    to: str = Property(String(format='date'), required=True)


class BudgetsReorderArgument(Object):

    order: List[Any] = Property(Array(Element()), required=True)


class BudgetsDeleteArgument(Object):

    id: str = Property(String(), required=True)


class BudgetsGetArgument(Object):

    id: str = Property(String(), required=True)


class BudgetsHistoryArgument(Object):

    from_: Maybe[str] = Property(String(format='date'), source='from')

    id: str = Property(String(), required=True)

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    to: str = Property(String(format='date'), required=True)


class BudgetsMoveArgument(Object):

    position: int = Property(Integer(minimum=0), required=True)


class CategoriesListArgument(Object):

    ids: Maybe[str] = Property(String())

    include_deleted: bool = Property(Boolean(default=False))

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    search: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    type: Maybe[str] = Property(String(enum=['expense', 'income']))


class CategoriesMergeArgument(Object):

    categories: List[Any] = Property(Array(Element()), required=True)

    category: str = Property(String(), required=True)


class CategoriesSumsListArgument(Object):

    accounts: Maybe[str] = Property(String())

    categories: Maybe[str] = Property(String())

    currency: str = Property(String(pattern='[A-Z_]{2,10}'), required=True)

    from_: str = Property(String(format='date'), required=True, source='from')

    locations: Maybe[str] = Property(String())

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    required_tags: Maybe[str] = Property(String())

    search: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    tags: Maybe[str] = Property(String())

    to: str = Property(String(format='date'), required=True)

    type: Maybe[str] = Property(String(enum=['expense', 'income']))

    not_categories: Maybe[str] = Property(String(), source='!categories')

    not_locations: Maybe[str] = Property(String(), source='!locations')

    not_tags: Maybe[str] = Property(String(), source='!tags')


class CategoriesDeleteArgument(Object):

    id: str = Property(String(), required=True)


class CategoriesGetArgument(Object):

    id: str = Property(String(), required=True)


class CurrenciesListArgument(Object):

    currencies: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    types: Maybe[str] = Property(String(enum=['fiat', 'commodity', 'crypto', 'deprecated']))


class EntriesListArgument(Object):

    accounts: Maybe[str] = Property(String())

    categories: Maybe[str] = Property(String())

    expand: bool = Property(Boolean(default=False))

    from_: str = Property(String(format='date'), required=True, source='from')

    include_deleted: bool = Property(Boolean(default=False))

    locations: Maybe[str] = Property(String())

    page: int = Property(Integer(default=0, minimum=0))

    parent: Maybe[str] = Property(String())

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    repeat: Maybe[str] = Property(String())

    search: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    tags: Maybe[str] = Property(String())

    to: str = Property(String(format='date'), required=True)

    type: Maybe[str] = Property(String(enum=['expense', 'income', 'transaction']))

    not_categories: Maybe[str] = Property(String(), source='!categories')

    not_locations: Maybe[str] = Property(String(), source='!locations')

    not_tags: Maybe[str] = Property(String(), source='!tags')


class EntriesLocationsListArgument(Object):

    accounts: Maybe[str] = Property(String())

    categories: Maybe[str] = Property(String())

    from_: Maybe[str] = Property(String(format='date'), source='from')

    include_unused: bool = Property(Boolean(default=False))

    latitude: Maybe[float] = Property(Number())

    longitude: Maybe[float] = Property(Number())

    near: Maybe[str] = Property(String())

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    radius: Maybe[float] = Property(Number())

    search: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    tags: Maybe[str] = Property(String())

    to: Maybe[str] = Property(String(format='date'))

    type: Maybe[str] = Property(String(enum=['expense', 'income']))

    not_categories: Maybe[str] = Property(String(), source='!categories')

    not_tags: Maybe[str] = Property(String(), source='!tags')


class EntriesLocationsGetArgument(Object):

    id: str = Property(String(), required=True)


class EntriesSplitArgument(Object):

    id: str = Property(String(), required=True)


class EntriesSumsListArgument(Object):

    accounts: Maybe[str] = Property(String())

    categories: Maybe[str] = Property(String())

    currency: str = Property(String(pattern='[A-Z_]{2,10}'), required=True)

    from_: str = Property(String(format='date'), required=True, source='from')

    locations: Maybe[str] = Property(String())

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    range: str = Property(String(default='day', enum=['day', 'week', 'month']))

    search: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    tags: Maybe[str] = Property(String())

    to: str = Property(String(format='date'), required=True)

    type: Maybe[str] = Property(String(enum=['expense', 'income']))

    not_categories: Maybe[str] = Property(String(), source='!categories')

    not_locations: Maybe[str] = Property(String(), source='!locations')

    not_tags: Maybe[str] = Property(String(), source='!tags')


class EntriesDeleteArgument(Object):

    id: str = Property(String(), required=True)


class EntriesGetArgument(Object):

    id: str = Property(String(), required=True)


class ExportsListArgument(Object):

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    status: Maybe[str] = Property(String(enum=['sending', 'sent', 'error', 'generating', 'generated']))

    type: Maybe[str] = Property(String(enum=['export', 'attachments', 'user_data']))


class ExportsGetArgument(Object):

    id: str = Property(String(), required=True)


class ExportsUpdateArgument(Object):

    modified: str = Property(String(), required=True)

    seen: Maybe[bool] = Property(Boolean())


class ImagesListArgument(Object):

    include_deleted: bool = Property(Boolean(default=False))

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    since: Maybe[str] = Property(String(format='date-time'))

    status: Maybe[str] = Property(String(enum=['new', 'uploaded', 'error', 'deleting']))


class ImagesDeleteArgument(Object):

    id: str = Property(String(), required=True)


class ImagesGetArgument(Object):

    id: str = Property(String(), required=True)


class MeAdjustCampaignArgument(Object):

    adgroup: str = Property(String(), required=True)

    campaign: str = Property(String(), required=True)

    creative: str = Property(String(), required=True)

    network: str = Property(String(), required=True)


class MeNotificationsListArgument(Object):

    include_deleted: bool = Property(Boolean(default=False))

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    since: Maybe[str] = Property(String(format='date-time'))


class MeNotificationsDeleteArgument(Object):

    id: str = Property(String(), required=True)


class MeNotificationsGetArgument(Object):

    id: str = Property(String(), required=True)


class MePushArgument(Object):

    token: str = Property(String(), required=True)

    type: str = Property(String(enum=['apple', 'apple_fcm', 'google', 'windows']), required=True)


class MeRevertArgument(Object):

    password: str = Property(String(), required=True)


class TagsListArgument(Object):

    categories: Maybe[str] = Property(String())

    ids: Maybe[str] = Property(String())

    include_deleted: bool = Property(Boolean(default=False))

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=50, minimum=10, maximum=500))

    search: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    type: Maybe[str] = Property(String(enum=['expense', 'income']))

    used_with_categories: Maybe[str] = Property(String())

    used_with_tags: Maybe[str] = Property(String())

    used_with_tags_min: int = Property(Integer(default=1, minimum=1))


class TagsMergeArgument(Object):

    account: Maybe[str] = Property(String())

    category: Maybe[str] = Property(String())

    tag: Maybe[str] = Property(String())

    tags: List[Any] = Property(Array(Element()), required=True)


class TagsSumsListArgument(Object):

    accounts: Maybe[str] = Property(String())

    categories: Maybe[str] = Property(String())

    currency: str = Property(String(pattern='[A-Z_]{2,10}'), required=True)

    from_: str = Property(String(format='date'), required=True, source='from')

    locations: Maybe[str] = Property(String())

    page: int = Property(Integer(default=0, minimum=0))

    per_page: int = Property(Integer(default=200, minimum=10, maximum=500))

    search: Maybe[str] = Property(String())

    since: Maybe[str] = Property(String(format='date-time'))

    tags: Maybe[str] = Property(String())

    to: str = Property(String(format='date'), required=True)

    type: Maybe[str] = Property(String(enum=['expense', 'income']))

    not_categories: Maybe[str] = Property(String(), source='!categories')

    not_locations: Maybe[str] = Property(String(), source='!locations')

    not_tags: Maybe[str] = Property(String(), source='!tags')


class TagsDeleteArgument(Object):

    id: str = Property(String(), required=True)


class TagsGetArgument(Object):

    id: str = Property(String(), required=True)


class Currency(Object):

    code: str = Property(String(pattern='[A-Z_]{2,10}'), required=True)

    fixed: bool = Property(Boolean(default='false'))

    main_rate: Maybe[float] = Property(Number())

    rate: Maybe[float] = Property(Number(exclusiveMinimum=0))


class Extra(Object):

    pass


class BudgetsUpdateArgument(Object):

    accounts: Maybe[List[Any]] = Property(Array(Element()))

    categories: Maybe[List[Any]] = Property(Array(Element()))

    currency: Currency = Property(Currency, required=True)

    delta: Maybe[float] = Property(Number())

    extra: Maybe[Extra] = Property(Extra)

    id: str = Property(String(), required=True)

    limit: float = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000), required=True)

    modified: str = Property(String(), required=True)

    name: str = Property(String(maxLength=255), required=True)

    percent: Maybe[float] = Property(Number(exclusiveMinimum=0))

    rollover: bool = Property(Boolean(default=False))

    rollover_amount: float = Property(Number(default=0, exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    rollover_override: bool = Property(Boolean(default=False))

    tags: Maybe[List[Any]] = Property(Array(Element()))

    type: str = Property(String(enum=['regular', 'delta', 'percent']), required=True)

    start: Any = Property(Element(), required=True)

    period: Any = Property(Element(), required=True)

    frequency: Any = Property(Element(), required=True)

    not_accounts: Maybe[List[Any]] = Property(Array(Element()), source='!accounts')

    not_categories: Maybe[List[Any]] = Property(Array(Element()), source='!categories')

    not_tags: Maybe[List[Any]] = Property(Array(Element()), source='!tags')


class CategoriesCreateArgument(Object):

    extra: Maybe[Extra] = Property(Extra)

    name: str = Property(String(minLength=1, maxLength=255), required=True)

    type: str = Property(String(enum=['expense', 'income']), required=True)


class CategoriesUpdateArgument(Object):

    extra: Maybe[Extra] = Property(Extra)

    id: str = Property(String(), required=True)

    modified: str = Property(String(), required=True)

    name: str = Property(String(minLength=1, maxLength=255), required=True)

    name_override: bool = Property(Boolean(default=False))

    type: str = Property(String(enum=['expense', 'income']), required=True)


class TagsCreateArgument(Object):

    category: Maybe[str] = Property(String())

    extra: Maybe[Extra] = Property(Extra)

    name: str = Property(String(minLength=1, maxLength=255), required=True)

    type: str = Property(String(enum=['expense', 'income']), required=True)


class TagsUpdateArgument(Object):

    category: Maybe[str] = Property(String())

    extra: Maybe[Extra] = Property(Extra)

    id: str = Property(String(), required=True)

    modified: str = Property(String(), required=True)

    name: str = Property(String(minLength=1, maxLength=255), required=True)

    name_override: bool = Property(Boolean(default=False))

    type: str = Property(String(enum=['expense', 'income']), required=True)


class SavingsGoal(Object):

    amount: float = Property(Number(exclusiveMinimum=0, exclusiveMaximum=1000000000000000), required=True)

    end: str = Property(String(format='date'), required=True)

    start: str = Property(String(format='date'), required=True)


class AccountsCreateArgument(Object):

    currency: Currency = Property(Currency, required=True)

    extra: Maybe[Extra] = Property(Extra)

    goal: Maybe[SavingsGoal] = Property(SavingsGoal)

    initial_balance: float = Property(Number(default=0, exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    name: str = Property(String(maxLength=255), required=True)

    parent: Maybe[str] = Property(String())

    type: Maybe[str] = Property(String(enum=['custom', 'depository', 'credit_card', 'loan', 'mortgage', 'brokerage', 'other']))


class AccountsUpdateArgument(Object):

    currency: Currency = Property(Currency, required=True)

    extra: Maybe[Extra] = Property(Extra)

    goal: Maybe[SavingsGoal] = Property(SavingsGoal)

    id: str = Property(String(), required=True)

    initial_balance: float = Property(Number(default=0, exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    modified: str = Property(String(), required=True)

    name: str = Property(String(maxLength=255), required=True)

    name_override: bool = Property(Boolean(default=False))

    parent: Maybe[str] = Property(String())

    type: Maybe[str] = Property(String(enum=['custom', 'depository', 'credit_card', 'loan', 'mortgage', 'brokerage', 'other']))


class Recurrence(Object):

    byday: Maybe[str] = Property(String())

    bymonthday: Maybe[str] = Property(String())

    bysetpos: Maybe[str] = Property(String())

    end: Maybe[str] = Property(String(format='date'))

    frequency: Maybe[str] = Property(String(enum=['one-time', 'daily', 'weekly', 'monthly', 'yearly']))

    interval: Maybe[int] = Property(Integer(minimum=1, maximum=127))

    start: Maybe[str] = Property(String(format='date'))


class BudgetsCreateArgument(Object):

    accounts: Maybe[List[Any]] = Property(Array(Element()))

    categories: Maybe[List[Any]] = Property(Array(Element()))

    currency: Currency = Property(Currency, required=True)

    delta: Maybe[float] = Property(Number())

    extra: Maybe[Extra] = Property(Extra)

    limit: float = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000), required=True)

    name: str = Property(String(maxLength=255), required=True)

    percent: Maybe[float] = Property(Number(exclusiveMinimum=0))

    recurrence: Maybe[Recurrence] = Property(Recurrence)

    rollover: bool = Property(Boolean(default=False))

    rollover_amount: float = Property(Number(default=0, exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    rollover_override: bool = Property(Boolean(default=False))

    tags: Maybe[List[Any]] = Property(Array(Element()))

    type: str = Property(String(enum=['regular', 'delta', 'percent']), required=True)

    start: Any = Property(Element(), required=True)

    period: Any = Property(Element(), required=True)

    frequency: Any = Property(Element(), required=True)

    not_accounts: Maybe[List[Any]] = Property(Array(Element()), source='!accounts')

    not_categories: Maybe[List[Any]] = Property(Array(Element()), source='!categories')

    not_tags: Maybe[List[Any]] = Property(Array(Element()), source='!tags')


class EntryImage(Object):

    id: str = Property(String(), required=True)


class EntryLocation(Object):

    id: Maybe[str] = Property(String())

    latitude: float = Property(Number(), required=True)

    longitude: float = Property(Number(), required=True)

    venue_id: Maybe[str] = Property(String())


class Reminder(Object):

    at: str = Property(String(format='time'), required=True)

    number: int = Property(Integer(minimum=0, maximum=255), required=True)

    period: str = Property(String(enum=['day', 'week', 'month', 'year']), required=True)


class EntryRepeat(Object):

    byday: Maybe[str] = Property(String())

    bymonthday: Maybe[str] = Property(String())

    bysetpos: Maybe[str] = Property(String())

    count: Maybe[int] = Property(Integer(minimum=1))

    end: Maybe[str] = Property(String(format='date'))

    frequency: str = Property(String(enum=['daily', 'weekly', 'monthly', 'yearly']), required=True)

    id: Maybe[str] = Property(String())

    interval: int = Property(Integer(minimum=1, maximum=127), required=True)

    iteration: Maybe[float] = Property(Number(minimum=0))

    start: str = Property(String(format='date'), required=True)


class EntrySplit(Object):

    parent: str = Property(String(), required=True)


class EntryTransaction(Object):

    account: str = Property(String(), required=True)

    currency: Currency = Property(Currency, required=True)

    id: Maybe[str] = Property(String())


class EntriesCreateArgument(Object):

    account: str = Property(String(), required=True)

    amount: float = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000), required=True)

    category: str = Property(String(), required=True)

    completed: bool = Property(Boolean(default=False))

    currency: Currency = Property(Currency, required=True)

    date: str = Property(String(format='date'), required=True)

    desc: Maybe[str] = Property(String(maxLength=255))

    extra: Maybe[Extra] = Property(Extra)

    images: Maybe[List[EntryImage]] = Property(Array(EntryImage, maxItems=4))

    location: Maybe[EntryLocation] = Property(EntryLocation)

    reminders: Maybe[List[Reminder]] = Property(Array(Reminder, maxItems=5))

    repeat: Maybe[EntryRepeat] = Property(EntryRepeat)

    split: Maybe[EntrySplit] = Property(EntrySplit)

    tags: Maybe[List[Any]] = Property(Array(Element()))

    transaction: Maybe[EntryTransaction] = Property(EntryTransaction)


class EntriesUpdateArgument(Object):

    account: str = Property(String(), required=True)

    amount: float = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000), required=True)

    category: str = Property(String(), required=True)

    completed: bool = Property(Boolean(default=False))

    currency: Currency = Property(Currency, required=True)

    date: str = Property(String(format='date'), required=True)

    desc: Maybe[str] = Property(String(maxLength=255))

    extra: Maybe[Extra] = Property(Extra)

    id: str = Property(String(), required=True)

    images: Maybe[List[EntryImage]] = Property(Array(EntryImage, maxItems=4))

    location: Maybe[EntryLocation] = Property(EntryLocation)

    modified: str = Property(String(), required=True)

    reminders: Maybe[List[Reminder]] = Property(Array(Reminder, maxItems=5))

    repeat: Maybe[EntryRepeat] = Property(EntryRepeat)

    tags: Maybe[List[Any]] = Property(Array(Element()))

    transaction: Maybe[EntryTransaction] = Property(EntryTransaction)


class Export(Object):

    pass


class ExportsCreateArgument(Object):

    filters: Maybe[Export] = Property(Export)

    formats: Maybe[Export] = Property(Export)

    from_: Maybe[str] = Property(String(format='date'), source='from')

    resources: Maybe[Export] = Property(Export)

    seen: Maybe[bool] = Property(Boolean())

    to: Maybe[str] = Property(String(format='date'))

    type: str = Property(String(enum=['export', 'attachments', 'user_data']), required=True)


class CustomCurrency(Object):

    code: Maybe[str] = Property(String(pattern='[A-Z_]{2,10}'))

    fixed: bool = Property(Boolean(default='false'))

    rate: Maybe[float] = Property(Number(minimum=0))

    reference_currency: Maybe[str] = Property(String(pattern='[A-Z_]{2,10}'))


class CurrencySettings(Object):

    custom: Maybe[CustomCurrency] = Property(CustomCurrency)

    custom_exchange_rate: Maybe[float] = Property(Number(minimum=0))

    main: str = Property(String(pattern='[A-Z_]{2,10}'), required=True)

    update: Maybe[str] = Property(String(enum=['historical', 'custom', 'sign']))

    update_accounts: Maybe[bool] = Property(Boolean())


class UserMigrationDetails(Object):

    finished: Maybe[bool] = Property(Boolean())


class MeUpdateArgument(Object):

    country: Maybe[str] = Property(String(pattern='[A-Z]{2}'))

    currency: CurrencySettings = Property(CurrencySettings, required=True)

    extra: Maybe[Extra] = Property(Extra)

    first_name: Maybe[str] = Property(String(maxLength=150))

    id: str = Property(String(), required=True)

    last_name: Maybe[str] = Property(String(maxLength=150))

    locale: Maybe[str] = Property(String())

    migration: Maybe[UserMigrationDetails] = Property(UserMigrationDetails)

    modified: str = Property(String(), required=True)

    start_day: int = Property(Integer(default=1, minimum=1, maximum=31))

    timezone: Maybe[str] = Property(String())
