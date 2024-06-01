# Domain Services
class ContactService:
    def __init__(self, contacts_sheet):
        self.contacts_sheet = contacts_sheet

    def find_contact(self, name):
        cell = self.contacts_sheet.find(name)
        email = self.contacts_sheet.cell(cell.row, cell.col + 1).value
        return email

    def find_contacts(self):
        emails = self.contacts_sheet.col_values(self.contacts_sheet.find("Mail").col)[1:]
        return emails
