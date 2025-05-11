import re


class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def display(self):
        print(f"{self.name.title()} - {self.phone} ")

    def to_dict(self):
        return {"name": self.name, "phone": self.phone}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["phone"])

    @staticmethod
    def normalize_phone_number(raw_phone_number):
        # Remove anything that's not a digit
        digits = re.sub(r"[^\d]", "", raw_phone_number)

        # Remove leading country code if it's +1 or 1
        if digits.startswith("1") and len(digits) == 11:
            digits = digits[1:]

        if len(digits) == 10:
            # Return in 123-456-7890 format
            return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
        else:
            return None
