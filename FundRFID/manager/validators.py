from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import math


def validate_pawsid(value):
    if count_digits(value) is not 6:
        print('value: {}'.format(value))
        print('num_digits: {}'.format(count_digits(value)))
        raise ValidationError(
            _('Your PAWS ID should be 6 digits')
        )


def count_digits(val):
    return int(math.log10(val)) + 1
