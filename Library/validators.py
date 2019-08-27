from django.core.exceptions import ValidationError

def MaxYearValidator(value):
    if value > 2019 :
        raise ValidationError("We have now 2019 year, it's not even finished")

def MinYearValidator(value):
    if value < (-3000) :
        raise ValidationError("The oldest letter dates from 3000 B.C., it can't be older")

def MinPagesValidator(value):
    if value < 1 :
        raise ValidationError("Too short")

def ISBN13Validator(type,value):
    if len(value) != 13 and type == 1:
        raise ValidationError("Wrong ISBN-13")

def ISBN10Validator(type,value):
    if len(value) != 10 and type == 0:
        raise ValidationError("Wrong ISBN-10")