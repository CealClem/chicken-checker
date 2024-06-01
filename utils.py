# import datetime

months = {
    '01': 'janvier',
    '02': 'février',
    '03': 'mars',
    '04': 'avril',
    '05': 'mai',
    '06': 'juin',
    '07': 'juillet',
    '08': 'août',
    '09': 'septembre',
    '10': 'octobre',
    '11': 'novembre',
    '12': 'décembre'
}


def reverse_format_date(input_date):

    # Extract day, month, and year from the input date
    day = input_date.strftime('%d')
    month = input_date.strftime('%m')
    year = input_date.strftime('%Y')

    # Convert numerical month to French month name
    month_name = months[month]

    # Format day and month with leading zeros if necessary
    day_formatted = day if day[0] != '0' else day[1]
    month_formatted = month_name + '.'

    # Construct the formatted date strings
    formatted_date_1 = f"{day_formatted}-{month_formatted}"
    formatted_date_2 = f"{day}-{month}"

    return formatted_date_1, formatted_date_2
