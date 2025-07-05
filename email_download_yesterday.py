import win32com.client
import pandas as pd
import re
from datetime import datetime, timedelta


class DownloadEmails():
    """
    A class to download and process emails from Outlook.
    Attributes:
        your_name (str): Your full name to check if mentioned in emails.
        internal_domain (str): Your company's email domain to filter internal emails.
        """

    def __init__(self, your_name, internal_domain):
        self.your_name = your_name
        self.internal_domain = internal_domain
        self.outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
        self.inbox = self.outlook.GetDefaultFolder(6)  # 6 refers to inbox
        self.messages = self.inbox.Items # Get all messages in the inbox
        self.messages.Sort("[ReceivedTime]", True)  # sort by latest first
        self.day_count = 1  # Number of days to look back
        self.ignore_sender = ["Kapow.Sourcing@spglobal.com"]

    def fetch_emails(self):

        cut_off_date = datetime.now() - timedelta(days=self.day_count)
        cut_off_date = cut_off_date.date().strftime("%Y-%m-%d")

        data = []
        for message in self.messages:
            try:
                if message.SenderEmailType == "EX":
                    # For Exchange senders (internal colleagues)
                    sender_email = message.Sender.GetExchangeUser().PrimarySmtpAddress
                else:
                    sender_email = message.SenderEmailAddress
                if (sender_email not in self.ignore_sender) & (sender_email is not None) & \
                    (sender_email.endswith(self.internal_domain)):
                    subject = message.Subject
                    body = message.Body
                    date = message.ReceivedTime.strftime("%Y-%m-%d %H:%M:%S")
                    if (date < cut_off_date):
                        break
                    mentioned = "yes" if re.search(rf"\b{self.your_name}\b", body, re.IGNORECASE) else "no"
                    data.append([date, subject, body, sender_email, mentioned])
            except Exception as e:
                continue
        return pd.DataFrame(data, columns=["date", "subject", "body", "sender", "mentioned"])
 
if __name__ == "__main__":
    your_name = "Sachin Verma"
    internal_domain = "@spglobal.com"  # Replace with your company's email domain
    downloader = DownloadEmails(your_name, internal_domain)
    downloader.day_count = 5  # Set the number of days to look back
    df = downloader.fetch_emails()
    print(f"Downloaded {len(df)} emails from the last {downloader.day_count} day(s).")
