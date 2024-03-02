message: TextField to store the email message.
sender: EmailField with a default value of 'your_email@example.com', representing the sender's email address.
recipient: EmailField to store the recipient's email address.
sent_at: DateTimeField with auto_now_add=True to automatically record the timestamp when the email is sent.

The function then attempts to send the email using Django's send_mail function, using the provided subject, message, and recipient's email. If successful, it creates a SentEmail instance to store information about the sent email.