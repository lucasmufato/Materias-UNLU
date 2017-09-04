import smtplib

from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

class Mail:

    def __init__(self):
        self.mail = "pepe@gmail.com"
        self.passw  = "pepe"
        #me lo mando a mi mismo
        self.destinatario = self.mail
        self.servidor = "smtp.gmail.com"
        self.puertoServidor = 587

    def mandarMail(self,nuevosConcursos):
        #preparo los datos del mail
        fromaddr = self.mail
        toaddr = self.destinatario
        msg = MIMEMultipart()
        msg['From'] = self.mail
        msg['To'] = self.destinatario
        msg['Subject'] = "[AUTOMATICO] Nuevos Concursos"
        body = "Hay nuevos concursos en la pagina del departamento de Cs. Basicas, estos son: \n \n"
        for nc in nuevosConcursos:
            body+= nc.__str__() + "\n "
        body+= "\n \n MAIL GENERADO AUTOMATICAMENTE MEDIANTE UN SCRIPT."
        #transformo los datos a ascii, primero decodifico y desp codifico
        udata = body.decode("utf-8")
        asciidata = udata.encode("ascii", "ignore")

        msg.attach(MIMEText(asciidata, 'plain'))

        server = smtplib.SMTP(self.servidor, self.puertoServidor)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.mail, self.passw)
        text = msg.as_string()
        rta = server.sendmail(fromaddr, toaddr, text)
        server.quit()
