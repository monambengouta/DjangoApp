from django.core.exceptions import ValidationError
def is_Esprit_Email(value):
    if(not str(value).endswith('esprit.tn')):
        raise ValidationError(
            'Your email must be @esprit.tn',
            params={'value':value})
    return value
        