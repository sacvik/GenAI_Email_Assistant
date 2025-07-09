__author__ = "Sachin"
__email__ = "sachin.ds@gmail.com"
__version__ = "1.0.0"


import imaplib
import email
from email.header import decode_header
import os
from dotenv import load_dotenv
import logging

class EmailClientConnect:
    """Class to connect to an email server using IMAP and fetch emails."""

    def __init__(self):
        # Load environment variables
        load_dotenv()
        self.email_user = os.getenv('EMAIL_USER')
        self.email_pass = os.getenv('EMAIL_PASS')
        self.imap_servers = [{"gmail": "imap.gmail.com",
                              "yahoo": "imap.mail.yahoo.com",
                              "outlook": "imap-mail.outlook.com",
                              "icloud": "imap.mail.me.com"}]
        self.folder = "INBOX"
        self.connection = None


        def connect(self, service='gmail'):
            """Connect to the email server."""
            try:
                # Connect to the IMAP server
                self.connection = imaplib.IMAP4_SSL(self.imap_servers[0][service])
                self.connection.login(self.email_user, self.email_pass)
                logging.info("Connected to the email server successfully.")
            except imaplib.IMAP4.error as e:
                logging.error(f"Failed to connect: {e}")
                raise

        
        def fetch_emails(self, lookback = 7):
            """ Fetch emails based on the lookback period in days."""

            try:
                
                            