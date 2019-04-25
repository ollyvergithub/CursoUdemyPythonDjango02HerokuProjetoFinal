from django.forms import ModelForm
from .models import Person

class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo' ]
        labels= {
            'first_name': 'Nome',
            'last_name': 'Sobrenome',
            'age': 'Idade',
            'salary': 'Salário',
            'bio': 'Biografia',
            'photo': 'Imagem',
        }
