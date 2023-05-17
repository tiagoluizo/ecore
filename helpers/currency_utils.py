import locale

def format_usd_currency(value):
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Set the locale to en_US
    formatted_value = locale.currency(value, grouping=True)
    return formatted_value
