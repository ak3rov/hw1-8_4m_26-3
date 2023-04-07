
from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOICES = (
        ('oc.kg', 'oc.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'oc.kg':
            film_parser = parser.parser()
            for i in film_parser:
                models.CinemaKg.objects.create(**i)