SERVER = "smtp.office365.com"
FROM = "jepitibabagaris@outlook.com"
TO = ["Fabriziosalis2006@gmail.com"] # must be a list

SUBJECT = "Hello!"
TEXT = "This is a test of emailing through smtp of example.com."

# Prepare actual message
message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail
import smtplib
server = smtplib.SMTP(SERVER)
server.login("MrDoe", "PASSWORD")
server.sendmail(FROM, TO, message)
server.quit()