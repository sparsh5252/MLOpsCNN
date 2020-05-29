import smtplib
session = smtplib.SMTP("smtp.gmail.com", 587)
session.starttls()
session.login("sparsh.17bcon519@jecrcu.edu.in","17BCON519")
msg = "Best model trained!"
session.sendmail("sparsh.17bcon519@jecrcu.edu.in" , "sparsh5252@gmail.com" , msg)
session.quit()
