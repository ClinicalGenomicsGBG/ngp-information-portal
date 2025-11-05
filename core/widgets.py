
from django import forms

class CustomDateTimePicker(forms.DateTimeInput):
    REQUIRED_FORMAT = "%Y-%m-%d, %H-%M"
    def __init__(self, attrs : dict = {}, format = None) -> None:
        attrs.update({
            "class" : "form-control",
            "type" : "datetime-local"
        })
        self.format = format or self.REQUIRED_FORMAT
        super().__init__(attrs, format = self.format)

class CustomDatePicker(forms.DateInput):
    REQUIRED_FORMAT = "%Y-%m-%d"
    def __init__(self, attrs : dict = {}, format = None) -> None:
        attrs.update({
            "class" : "form-control",
            "type" : "date"
        })
        self.format = format or self.REQUIRED_FORMAT
        super().__init__(attrs, format = self.format)

class CustomTimePicker(forms.TimeInput):
    REQUIRED_FORMAT = "%H-%M"
    def __init__(self, attrs : dict = {}, format = None) -> None:
        attrs.update({
            "class" : "form-control",
            "type" : "time"
        })
        self.format = format or self.REQUIRED_FORMAT
        super().__init__(attrs, format = self.format)