from django.core.exceptions import ValidationError

def MinPagesValidator(value):
    if value < 1 :
        raise ValidationError("Too short")

def ISBNValidator(value):
    if len(str(value)) != 10 or len(str(value)) !=13 :
        raise ValidationError('Wrong ISBN')