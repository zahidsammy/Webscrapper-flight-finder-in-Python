import smtplib

sender_email = "zahidsammy95@gmail.com"
receiver_email = "zahidsammy95@gmail.com"
password = "sender_email_password"

message = "Flights alert: The prices for the flights have changed."

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, receiver_email, message)
server.quit()
