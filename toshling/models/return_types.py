from typing import List

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


class CurrencyElement(Object):

    modified: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String())

    precision: Maybe[int] = Property(Integer(minimum=0, maximum=9))

    symbol: Maybe[str] = Property(String())

    type: Maybe[str] = Property(String(enum=['fiat', 'commodity', 'crypto', 'deprecated']))


class Image(Object):

    deleted: Maybe[bool] = Property(Boolean())

    filename: Maybe[str] = Property(String())

    id: Maybe[str] = Property(String())

    path: Maybe[str] = Property(String())

    status: Maybe[str] = Property(String(enum=['new', 'uploaded', 'error', 'deleting']))

    type: Maybe[str] = Property(String())


class Notification(Object):

    action: Maybe[str] = Property(String())

    date: Maybe[str] = Property(String(format='date-time'))

    deleted: Maybe[bool] = Property(Boolean())

    id: Maybe[str] = Property(String())

    modified: Maybe[str] = Property(String())

    text: Maybe[str] = Property(String())

    type: Maybe[str] = Property(String(enum=['account', 'connection', 'entry', 'budget', 'balance', 'news', 'add_entry', 'add_budget', 'upgrade', 'connections', 'export']))


class EntryRepeat(Object):

    byday: Maybe[str] = Property(String())

    bymonthday: Maybe[str] = Property(String())

    bysetpos: Maybe[str] = Property(String())

    count: Maybe[int] = Property(Integer(minimum=1))

    end: Maybe[str] = Property(String(format='date'))

    entries: Maybe[List[str]] = Property(Array(String()))

    frequency: str = Property(String(enum=['daily', 'weekly', 'monthly', 'yearly']), required=True)

    id: Maybe[str] = Property(String())

    interval: int = Property(Integer(minimum=1, maximum=255), required=True)

    iteration: Maybe[int] = Property(Integer(minimum=0))

    start: str = Property(String(format='date'), required=True)

    template: Maybe[bool] = Property(Boolean())

    template_end: Maybe[str] = Property(String(format='date'))

    template_start: Maybe[str] = Property(String(format='date'))

    type: Maybe[str] = Property(String(enum=['automatic', 'confirm', 'confirmed']))


class AccountAvg(Object):

    expenses: float = Property(Number(default=0, minimum=0, exclusiveMaximum=1000000000000000))

    incomes: float = Property(Number(default=0, minimum=0, exclusiveMaximum=1000000000000000))


class AccountBilling(Object):

    byday: Maybe[str] = Property(String())

    bymonthday: Maybe[str] = Property(String())

    bysetpos: Maybe[str] = Property(String())


class AccountConnection(Object):

    id: Maybe[str] = Property(String())

    logo: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String())

    status: Maybe[str] = Property(String(enum=['connected', 'disconnected', 'inactive', 'error']))


class Currency(Object):

    code: Maybe[str] = Property(String(pattern='[A-Z_]{2,10}'))

    fixed: bool = Property(Boolean(default='false'))

    main_rate: Maybe[float] = Property(Number())

    rate: Maybe[float] = Property(Number(exclusiveMinimum=0))


class AccountMedian(Object):

    expenses: float = Property(Number(default=0, minimum=0, exclusiveMaximum=1000000000000000))

    incomes: float = Property(Number(default=0, minimum=0, exclusiveMaximum=1000000000000000))


class Extra(Object):

    pass


class AccountGoal(Object):

    amount: Maybe[float] = Property(Number(exclusiveMinimum=0, exclusiveMaximum=1000000000000000))

    end: Maybe[str] = Property(String(format='date'))

    start: Maybe[str] = Property(String(format='date'))


class AccountSettle(Object):

    byday: Maybe[str] = Property(String())

    bymonthday: Maybe[str] = Property(String())

    bysetpos: Maybe[str] = Property(String())


class Account(Object):

    avg: Maybe[AccountAvg] = Property(AccountAvg)

    balance: Maybe[float] = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    billing: Maybe[AccountBilling] = Property(AccountBilling)

    connection: Maybe[AccountConnection] = Property(AccountConnection)

    count: Maybe[int] = Property(Integer())

    currency: Maybe[Currency] = Property(Currency)

    daily_sum_median: Maybe[AccountMedian] = Property(AccountMedian)

    deleted: Maybe[bool] = Property(Boolean())

    extra: Maybe[Extra] = Property(Extra)

    goal: Maybe[AccountGoal] = Property(AccountGoal)

    id: Maybe[str] = Property(String())

    initial_balance: float = Property(Number(default=0, exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    limit: float = Property(Number(default=None, exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    modified: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String(maxLength=100))

    name_override: bool = Property(Boolean(default=False))

    order: Maybe[int] = Property(Integer(minimum=0, maximum=255))

    parent: Maybe[str] = Property(String())

    recalculated: Maybe[bool] = Property(Boolean())

    review: Maybe[int] = Property(Integer())

    settle: Maybe[AccountSettle] = Property(AccountSettle)

    status: Maybe[str] = Property(String(enum=['active', 'inactive', 'archived']))

    type: Maybe[str] = Property(String(enum=['custom', 'depository', 'credit_card', 'loan', 'mortgage', 'brokerage', 'investment', 'savings', 'other']))


class BudgetProblem(Object):

    deleted_accounts: Maybe[List[str]] = Property(Array(String()))

    deleted_categories: Maybe[List[str]] = Property(Array(String()))

    deleted_tags: Maybe[List[str]] = Property(Array(String()))

    description: Maybe[str] = Property(String())

    id: Maybe[str] = Property(String())


class Recurrence(Object):

    byday: Maybe[str] = Property(String())

    bymonthday: Maybe[str] = Property(String())

    bysetpos: Maybe[str] = Property(String())

    end: Maybe[str] = Property(String(format='date'))

    frequency: Maybe[str] = Property(String(enum=['one-time', 'daily', 'weekly', 'monthly', 'yearly']))

    interval: Maybe[int] = Property(Integer(minimum=1, maximum=127))

    iteration: Maybe[int] = Property(Integer(minimum=0))

    start: Maybe[str] = Property(String(format='date'))


class Budget(Object):

    exclamation_mark_accounts: Maybe[List[str]] = Property(Array(String()), source='!accounts')

    exclamation_mark_categories: Maybe[List[str]] = Property(Array(String()), source='!categories')

    exclamation_mark_tags: Maybe[List[str]] = Property(Array(String()), source='!tags')

    accounts: Maybe[List[str]] = Property(Array(String()))

    amount: Maybe[float] = Property(Number(minimum=0, exclusiveMaximum=1000000000000000))

    categories: Maybe[List[str]] = Property(Array(String()))

    currency: Maybe[Currency] = Property(Currency)

    deleted: Maybe[bool] = Property(Boolean())

    delta: Maybe[float] = Property(Number())

    extra: Maybe[Extra] = Property(Extra)

    from_: Maybe[str] = Property(String(format='date'), source='from')

    history_amount_median: Maybe[float] = Property(Number(minimum=0, exclusiveMaximum=1000000000000000))

    id: Maybe[str] = Property(String())

    limit: Maybe[float] = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    limit_planned: Maybe[float] = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    modified: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String(maxLength=300))

    order: Maybe[int] = Property(Integer(minimum=0, maximum=255))

    parent: Maybe[str] = Property(String())

    percent: Maybe[float] = Property(Number(exclusiveMinimum=0))

    planned: Maybe[float] = Property(Number(minimum=0, exclusiveMaximum=1000000000000000))

    problem: Maybe[BudgetProblem] = Property(BudgetProblem)

    recalculated: Maybe[bool] = Property(Boolean())

    recurrence: Maybe[Recurrence] = Property(Recurrence)

    rollover: bool = Property(Boolean(default=False))

    rollover_amount: float = Property(Number(default=0, exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    rollover_amount_planned: float = Property(Number(default=0, exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    rollover_override: bool = Property(Boolean(default=False))

    status: Maybe[str] = Property(String(enum=['active', 'inactive', 'archived']))

    tags: Maybe[List[str]] = Property(Array(String()))

    to: Maybe[str] = Property(String(format='date'))

    type: Maybe[str] = Property(String(enum=['regular', 'delta', 'percent']))


class CategoryCounts(Object):

    budgets: Maybe[int] = Property(Integer())

    entries: Maybe[int] = Property(Integer())

    expense_entries: Maybe[int] = Property(Integer())

    expense_tags: Maybe[int] = Property(Integer())

    expense_tags_used_with_category: Maybe[int] = Property(Integer())

    income_entries: Maybe[int] = Property(Integer())

    income_tags: Maybe[int] = Property(Integer())

    income_tags_used_with_category: Maybe[int] = Property(Integer())

    tags: Maybe[int] = Property(Integer())

    tags_used_with_category: Maybe[int] = Property(Integer())


class Category(Object):

    counts: Maybe[CategoryCounts] = Property(CategoryCounts)

    deleted: Maybe[bool] = Property(Boolean())

    extra: Maybe[Extra] = Property(Extra)

    id: Maybe[str] = Property(String())

    modified: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String(minLength=1, maxLength=100))

    name_override: bool = Property(Boolean(default=False))

    type: Maybe[str] = Property(String(enum=['expense', 'income', 'system']))


class CategorySumExpenses(Object):

    count: int = Property(Integer(minimum=0), required=True)

    sum: float = Property(Number(minimum=0, exclusiveMaximum=1000000000000000), required=True)


class CategorySumIncomes(Object):

    count: int = Property(Integer(minimum=0), required=True)

    sum: float = Property(Number(minimum=0, exclusiveMaximum=1000000000000000), required=True)


class CategorySum(Object):

    category: Maybe[str] = Property(String())

    category_name: Maybe[str] = Property(String())

    category_type: Maybe[str] = Property(String(enum=['expense', 'income', 'system']))

    expenses: Maybe[CategorySumExpenses] = Property(CategorySumExpenses)

    incomes: Maybe[CategorySumIncomes] = Property(CategorySumIncomes)

    modified: Maybe[str] = Property(String())


class EntryImage(Object):

    filename: Maybe[str] = Property(String())

    id: str = Property(String(), required=True)

    path: Maybe[str] = Property(String())

    status: Maybe[str] = Property(String(enum=['new', 'uploaded', 'error', 'deleting']))

    type: Maybe[str] = Property(String())


class EntryImport(Object):

    connection: Maybe[str] = Property(String())

    id: Maybe[str] = Property(String())

    memo: Maybe[str] = Property(String())

    payee: Maybe[str] = Property(String())

    pending: Maybe[bool] = Property(Boolean())


class EntryLocation(Object):

    id: Maybe[str] = Property(String())

    latitude: float = Property(Number(), required=True)

    longitude: float = Property(Number(), required=True)

    venue_id: Maybe[str] = Property(String())


class Reminder(Object):

    at: str = Property(String(format='time'), required=True)

    number: int = Property(Integer(minimum=0, maximum=255), required=True)

    period: str = Property(String(enum=['day', 'week', 'month', 'year']), required=True)


class EntryReview(Object):

    completed: Maybe[bool] = Property(Boolean())

    id: Maybe[str] = Property(String())

    type: Maybe[str] = Property(String(enum=['expense', 'income', 'transfer', 'repeat']))


class EntrySettle(Object):

    id: Maybe[str] = Property(String())


class EntrySplit(Object):

    children: Maybe[List[str]] = Property(Array(String()))

    parent: Maybe[str] = Property(String())


class EntryTransaction(Object):

    account: str = Property(String(), required=True)

    amount: Maybe[float] = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    currency: Currency = Property(Currency, required=True)

    id: Maybe[str] = Property(String())


class Entry(Object):

    account: Maybe[str] = Property(String())

    amount: Maybe[float] = Property(Number(exclusiveMinimum=-1000000000000000, exclusiveMaximum=1000000000000000))

    category: Maybe[str] = Property(String())

    completed: bool = Property(Boolean(default=False))

    created: Maybe[str] = Property(String(format='date-time'))

    currency: Maybe[Currency] = Property(Currency)

    date: Maybe[str] = Property(String(format='date'))

    deleted: Maybe[bool] = Property(Boolean())

    desc: Maybe[str] = Property(String(maxLength=3072))

    extra: Maybe[Extra] = Property(Extra)

    id: Maybe[str] = Property(String())

    images: Maybe[List[EntryImage]] = Property(Array(EntryImage, maxItems=4, uniqueItems=True))

    import_: Maybe[EntryImport] = Property(EntryImport, source='import')

    location: Maybe[EntryLocation] = Property(EntryLocation)

    modified: Maybe[str] = Property(String())

    readonly: Maybe[List[str]] = Property(Array(String()))

    reminders: Maybe[List[Reminder]] = Property(Array(Reminder, maxItems=5, uniqueItems=True))

    repeat: Maybe[EntryRepeat] = Property(EntryRepeat)

    review: Maybe[EntryReview] = Property(EntryReview)

    settle: Maybe[EntrySettle] = Property(EntrySettle)

    split: Maybe[EntrySplit] = Property(EntrySplit)

    tags: Maybe[List[str]] = Property(Array(String()))

    transaction: Maybe[EntryTransaction] = Property(EntryTransaction)


class DayExpenses(Object):

    count: int = Property(Integer(minimum=0), required=True)

    sum: float = Property(Number(minimum=0, exclusiveMaximum=1000000000000000), required=True)


class DayIncomes(Object):

    count: int = Property(Integer(minimum=0), required=True)

    sum: float = Property(Number(minimum=0, exclusiveMaximum=1000000000000000), required=True)


class Day(Object):

    day: Maybe[str] = Property(String(format='date'))

    expenses: Maybe[DayExpenses] = Property(DayExpenses)

    incomes: Maybe[DayIncomes] = Property(DayIncomes)

    modified: Maybe[str] = Property(String())


class ExportFile(Object):

    filename: Maybe[str] = Property(String())

    filesize: Maybe[float] = Property(Number())

    format: Maybe[str] = Property(String(enum=['csv', 'xls', 'pdf', 'ofx']))


class ExportData(Object):

    filename: Maybe[str] = Property(String())

    files: Maybe[List[ExportFile]] = Property(Array(ExportFile))

    filesize: Maybe[float] = Property(Number())

    path: Maybe[str] = Property(String())

    valid_until: Maybe[str] = Property(String(format='date-time'))


class Export(Object):

    exclamation_mark_accounts: Maybe[List[str]] = Property(Array(String(), uniqueItems=True), source='!accounts')

    exclamation_mark_categories: Maybe[List[str]] = Property(Array(String(), uniqueItems=True), source='!categories')

    exclamation_mark_locations: Maybe[List[str]] = Property(Array(String(), uniqueItems=True), source='!locations')

    exclamation_mark_tags: Maybe[List[str]] = Property(Array(String(), uniqueItems=True), source='!tags')

    accounts: Maybe[List[str]] = Property(Array(String(), uniqueItems=True))

    categories: Maybe[List[str]] = Property(Array(String(), uniqueItems=True))

    created: Maybe[str] = Property(String(format='date-time'))

    data: Maybe[ExportData] = Property(ExportData)

    emails: Maybe[List[str]] = Property(Array(String(format='email'), uniqueItems=True))

    formats: Maybe[List[str]] = Property(Array(String(enum=['csv', 'xls', 'pdf', 'ofx']), additionalItems=False, uniqueItems=True))

    from_: Maybe[str] = Property(String(format='date'), source='from')

    id: Maybe[str] = Property(String())

    locations: Maybe[List[str]] = Property(Array(String(), uniqueItems=True))

    modified: Maybe[str] = Property(String())

    resources: Maybe[List[str]] = Property(Array(String(enum=['expenses', 'incomes', 'budgets', 'summary', 'attachments', 'attachments_grid', 'balances']), additionalItems=False, uniqueItems=True))

    seen: Maybe[bool] = Property(Boolean())

    status: Maybe[str] = Property(String(enum=['sending', 'sent', 'error', 'generating', 'generated']))

    tags: Maybe[List[str]] = Property(Array(String(), uniqueItems=True))

    to: Maybe[str] = Property(String(format='date'))

    type: Maybe[str] = Property(String(enum=['export', 'attachments', 'user_data']))


class Expenses(Object):

    count: Maybe[int] = Property(Integer(minimum=0))

    sum: Maybe[float] = Property(Number(minimum=0, exclusiveMaximum=1000000000000000))


class Incomes(Object):

    count: Maybe[int] = Property(Integer(minimum=0))

    sum: Maybe[float] = Property(Number(minimum=0, exclusiveMaximum=1000000000000000))


class Location(Object):

    address: Maybe[str] = Property(String(maxLength=255))

    amount: Maybe[float] = Property(Number(minimum=0, exclusiveMaximum=1000000000000000))

    chain_id: Maybe[str] = Property(String())

    city: Maybe[str] = Property(String(maxLength=100))

    expenses: Maybe[Expenses] = Property(Expenses)

    id: Maybe[str] = Property(String())

    incomes: Maybe[Incomes] = Property(Incomes)

    latitude: Maybe[float] = Property(Number())

    longitude: Maybe[float] = Property(Number())

    modified: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String(maxLength=255))

    used: Maybe[bool] = Property(Boolean())

    venue_id: Maybe[str] = Property(String())

    visits: Maybe[int] = Property(Integer(minimum=0))


class TagCounts(Object):

    budgets: int = Property(Integer(), required=True)

    entries: int = Property(Integer(), required=True)

    unsorted_entries: Maybe[int] = Property(Integer())


class Tag(Object):

    category: Maybe[str] = Property(String())

    counts: Maybe[TagCounts] = Property(TagCounts)

    deleted: Maybe[bool] = Property(Boolean())

    extra: Maybe[Extra] = Property(Extra)

    id: Maybe[str] = Property(String())

    meta_tag: Maybe[bool] = Property(Boolean())

    modified: Maybe[str] = Property(String())

    name: Maybe[str] = Property(String(minLength=1, maxLength=100))

    name_override: bool = Property(Boolean(default=False))

    type: Maybe[str] = Property(String(enum=['expense', 'income']))


class TagSumExpenses(Object):

    categories: Maybe[List[str]] = Property(Array(String()))

    count: int = Property(Integer(minimum=0), required=True)

    sum: float = Property(Number(minimum=0, exclusiveMaximum=1000000000000000), required=True)


class TagSumIncomes(Object):

    categories: Maybe[List[str]] = Property(Array(String()))

    count: int = Property(Integer(minimum=0), required=True)

    sum: float = Property(Number(minimum=0, exclusiveMaximum=1000000000000000), required=True)


class TagSum(Object):

    expenses: Maybe[TagSumExpenses] = Property(TagSumExpenses)

    incomes: Maybe[TagSumIncomes] = Property(TagSumIncomes)

    modified: Maybe[str] = Property(String())

    tag: Maybe[str] = Property(String())


class CustomCurrency(Object):

    code: Maybe[str] = Property(String(pattern='[A-Z_]{2,10}'))

    fixed: bool = Property(Boolean(default='false'))

    rate: Maybe[float] = Property(Number(minimum=0))

    reference_currency: Maybe[str] = Property(String(pattern='[A-Z_]{2,10}'))


class UserCurrency(Object):

    custom: Maybe[CustomCurrency] = Property(CustomCurrency)

    custom_exchange_rate: Maybe[float] = Property(Number(minimum=0))

    main: Maybe[str] = Property(String(pattern='[A-Z_]{2,10}'))

    update: Maybe[str] = Property(String(enum=['historical', 'custom', 'sign']))

    update_accounts: Maybe[bool] = Property(Boolean())


class UserLimits(Object):

    accounts: Maybe[bool] = Property(Boolean())

    bank: Maybe[bool] = Property(Boolean())

    budgets: Maybe[bool] = Property(Boolean())

    export: Maybe[bool] = Property(Boolean())

    images: Maybe[bool] = Property(Boolean())

    import_: Maybe[bool] = Property(Boolean(), source='import')

    locations: Maybe[bool] = Property(Boolean())

    passcode: Maybe[bool] = Property(Boolean())

    planning: Maybe[bool] = Property(Boolean())

    pro_share: Maybe[bool] = Property(Boolean())

    reminders: Maybe[bool] = Property(Boolean())

    repeats: Maybe[bool] = Property(Boolean())


class UserMigration(Object):

    date_migrated: Maybe[str] = Property(String(format='date-time'))

    finished: Maybe[bool] = Property(Boolean())

    revert_until: Maybe[str] = Property(String(format='date-time'))


class UserPartner(Object):

    end: Maybe[str] = Property(String(format='date-time'))

    name: Maybe[str] = Property(String())

    start: Maybe[str] = Property(String(format='date-time'))


class UserProPayment(Object):

    id: Maybe[str] = Property(String())

    next: Maybe[str] = Property(String(format='date-time'))

    provider: Maybe[str] = Property(String(enum=['apple', 'google', 'microsoft', 'g2s', 'adyen', 'amazon', 'bitpay', 'paypal', 'unknown']))

    trial: bool = Property(Boolean(default='false'))


class UserProTrial(Object):

    end: Maybe[str] = Property(String(format='date-time'))

    start: Maybe[str] = Property(String(format='date-time'))


class UserProVAT(Object):

    address: str = Property(String(), required=True)

    city: str = Property(String(), required=True)

    country: str = Property(String(), required=True)

    name: str = Property(String(), required=True)

    post: str = Property(String(), required=True)

    state: Maybe[str] = Property(String())

    vat: str = Property(String(), required=True)


class UserPro(Object):

    level: Maybe[str] = Property(String(enum=['pro', 'medici']))

    partner: Maybe[List[UserPartner]] = Property(Array(UserPartner))

    payment: Maybe[UserProPayment] = Property(UserProPayment)

    remaining_credit: Maybe[float] = Property(Number(minimum=0, maximum=1000))

    since: Maybe[str] = Property(String(format='date-time'))

    trial: Maybe[UserProTrial] = Property(UserProTrial)

    until: Maybe[str] = Property(String(format='date-time'))

    vat: Maybe[UserProVAT] = Property(UserProVAT)


class User(Object):

    country: Maybe[str] = Property(String(pattern='[A-Z]{2}'))

    currency: Maybe[UserCurrency] = Property(UserCurrency)

    email: Maybe[str] = Property(String(format='email', maxLength=254))

    extra: Maybe[Extra] = Property(Extra)

    first_name: Maybe[str] = Property(String(maxLength=100))

    flags: Maybe[List[str]] = Property(Array(String()))

    id: Maybe[str] = Property(String())

    joined: Maybe[str] = Property(String(format='date-time'))

    language: Maybe[str] = Property(String())

    last_name: Maybe[str] = Property(String(maxLength=100))

    limits: Maybe[UserLimits] = Property(UserLimits)

    locale: Maybe[str] = Property(String())

    migration: Maybe[UserMigration] = Property(UserMigration)

    modified: Maybe[str] = Property(String())

    notifications: Maybe[int] = Property(Integer())

    otp_enabled: Maybe[bool] = Property(Boolean())

    pro: Maybe[UserPro] = Property(UserPro)

    social: Maybe[List[str]] = Property(Array(String(enum=['toshl', 'google', 'facebook', 'twitter', 'evernote', 'foursquare', 'etalio', 'flickr', 'apple']), additionalItems=False, uniqueItems=True))

    start_day: int = Property(Integer(default=1, minimum=1, maximum=31))

    steps: Maybe[List[str]] = Property(Array(String(enum=['income', 'expense', 'budget', 'budget_category']), additionalItems=False, uniqueItems=True))

    timezone: Maybe[str] = Property(String())

    trial_eligible: bool = Property(Boolean(default=False))
