import tkinter as tk
import smtplib

def send_email():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(user_entry.get(), pass_entry.get())
        server.sendmail(from_entry.get(), to_entry.get(),
                        message_entry.get(1.0, tk.END))
        server.quit()
        result_label.config(text="E-mail enviado com sucesso!", fg='green')
    except Exception as e:
        result_label.config(text="Erro ao enviar e-mail: " + str(e), fg='red')

app = tk.Tk()
app.title("Envio de E-mail")
app.geometry("500x400")

user_label = tk.Label(text="Usuário:")
user_label.pack()
user_entry = tk.Entry()
user_entry.pack()

pass_label = tk.Label(text="Senha:")
pass_label.pack()
pass_entry = tk.Entry(show="*")
pass_entry.pack()

from_label = tk.Label(text="De:")
from_label.pack()
from_entry = tk.Entry()
from_entry.pack()

to_label = tk.Label(text="Para:")
to_label.pack()
to_entry = tk.Entry()
to_entry.pack()

message_label = tk.Label(text="Mensagem:")
message_label.pack()
message_entry = tk.Text()
message_entry.pack()

send_button = tk.Button(text="Enviar", command=send_email)
send_button.pack()

result_label = tk.Label(text="")
result_label.pack()

app.mainloop()
