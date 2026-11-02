# Exercise 8-10: Memindahkan pesan ke list terkirim.
def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Mengirim: {current_message}")
        sent_messages.append(current_message)

messages = ["Halo!", "Apa kabar?", "Sampai jumpa."]
sent_messages = []
send_messages(messages, sent_messages)
print("List pesan tersisa:", messages)
print("Pesan terkirim:", sent_messages)
