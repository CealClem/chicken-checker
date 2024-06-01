import gspread

from contact_service import ContactService
from email_adapter import EmailAdapter
from log import do_logging
from scheduler import Scheduler

from config import SENDER_EMAIL, SENDER_PASSWORD, SHEET_ID, client


if __name__ == '__main__':

    workbook = client.open_by_key(SHEET_ID)
    contacts_sheet = workbook.worksheet('CONTACTS')
    contacts_service = ContactService(contacts_sheet)
    email_adapter = EmailAdapter(SENDER_EMAIL, SENDER_PASSWORD)
    scheduler = Scheduler(SHEET_ID, contacts_service, email_adapter)
    scheduler.check_tomorrow()
    do_logging()
