import email_sender
import nist_client
import cve_formatter
import config


def get_receiver_emails():
    with open(config.MAILING_LIST_PATH, 'r') as file:
        emails = [line.strip() for line in file]
    return emails

def send_daily_cves_email():
    cves = nist_client.NistClient.get_nist_cves()
    html = cve_formatter.CVEFormatter.get_cve_html(cves['vulnerabilities'])
    receiver_emails = get_receiver_emails()
    email_sender.EmailSender.send_email('[OSB] Daily NIST Security Report', html, receiver_emails)


if __name__ == "__main__":
    send_daily_cves_email()
