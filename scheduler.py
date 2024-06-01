import datetime

from config import SHEET_ID, client
from log import logger
from utils import reverse_format_date, months

class Scheduler:
    def __init__(self, sheet_id, contacts_service, email_adapter):
        self.sheet_id = sheet_id
        self.contacts_service = contacts_service
        self.email_adapter = email_adapter

    def check_tomorrow(self):

        # set up dates needed
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        current_month = today.month
        current_month = months['0'+str(current_month) if current_month<10 else str(current_month)].upper() # need to transform to capital french
        current_year = str(today.year)[-2:] # just last 2 nums
        current_month_string = current_month + ' ' + current_year

        workbook = client.open_by_key(SHEET_ID)

        current_month = workbook.worksheet(current_month_string)
        contacts = workbook.worksheet('CONTACTS')

        cell = current_month.find(reverse_format_date(tomorrow)[0])
        if not cell:
            cell = current_month.find(reverse_format_date(tomorrow)[1])
        morning_person = current_month.cell(cell.row + 1, cell.col).value
        evening_person = current_month.cell(cell.row + 2, cell.col).value

        if morning_person:
            self.send_reminder(morning_person, 'morning')
            print(f'sent reminder to {morning_person} for the morning')
        if evening_person:
            self.send_reminder(evening_person, 'evening')
            print(f'sent reminder to {evening_person} for the evening')
        if not evening_person or not morning_person:
            print('careful theres a gap tomorrow')
            self.send_gap_reminder()

    def send_reminder(self, name, time_of_day):
        contact_email = self.contacts_service.find_contact(name)
        if contact_email:
            body = f"Cot Cot {name[:-2]},\n\nNe nous oublies pas ! Tu es programmé à venir nous voir demain {time_of_day}.\n\nBien cot cotrdialement,\n\nLes cocottes de chaville"
            subject = "Rappel Cocot"
            self.email_adapter.send_email(contact_email, subject, body)
            logger.info(f"Email reminder sent to {contact_email}")

    def send_gap_reminder(self):
        contact_list = self.contacts_service.find_contacts()
        if contact_list:
            body = f"Cot Cot tous le monde,\n\nNe nous oubliez pas ! Attention il y a une case vide dans le calendrier demain!,\n\nLes cocottes de chaville"
            subject = "Rappel Cocot"
            self.email_adapter.send_email(contact_list, subject, body)
            logger.info(f"Email reminder sent to all contacts")
