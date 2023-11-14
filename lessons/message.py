"""Operators Overloads."""


class Email:

    to: str
    message: str
    important: bool

    def __init__(self, recipient: str | int, message_text: str, important_flag: bool):
        """Constructor of email."""
        self.to = recipient
        self.message = message_text
        self.important = important_flag

    def __str__(self) -> str:
        """Printing email."""
        m_string: str = f"To:{self.to} \n"
        m_string += f"Important? {self.important}\n"
        m_string += f'"{self.message}'
        return m_string
    
    def __mul__(self, factor: int):
        """Multipler."""
        self.message *= factor
 

email_to_keira: Email = Email("Keira", "Let's get wine drunk", False)
# email_to_keira * 100
print(email_to_keira)
email_to_sarah: Email = Email("Sarah", "I want my green jacket back!", False)
print(email_to_sarah)
