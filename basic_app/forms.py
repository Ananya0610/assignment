from django import forms
from .models import Person,Country,State,City

class PersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=('name','bdate','country','state','district','city')

        def __init__(self,*args,**kwargs):
            super().___init__(*args, **kwargs)
            self.fields['state'].queryset=State.objects.none()

            if 'country' in self.data:
                try:
                     country_id=int(self.data.get('country'))
                     self.fields['state'].queryset=State.objects.filter(country_id=country_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['state'],queryset=self.instance.country.state_set.order_by('name')

            self.fields['district'].queryset = District.objects.none()

            if 'state' in self.data:
                try:
                    state_id = int(self.data.get('state'))
                    self.fields['district'].queryset = District.objects.filter(state_id=state_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['district'].queryset = self.instance.state.district_set.order_by('name')

                self.fields['city'].queryset =City.objects.none()

            if 'district' in self.data:
                try:
                    city_id = int(self.data.get('city'))
                    self.fields['district'].queryset = District.objects.filter(city_id=city_id).order_by('name')
                except (ValueError, TypeError):
                    pass
            elif self.instance.pk:
                self.fields['city'].queryset = self.instance.district.city_set.order_by('name')
