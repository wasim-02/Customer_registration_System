from django import forms
from connections.models import Consumer, Zone, Division, SubDivision

class PersonCreationForm(forms.ModelForm):
    class Meta:
        model = Consumer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['division'].queryset = Division.objects.none()
        self.fields['subdivision'].queryset = SubDivision.objects.none()

        if 'zone' in self.data:
            try:
                zone_id = int(self.data.get('zone'))
                self.fields['division'].queryset = Division.objects.filter(zone_id=zone_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty division queryset

        if 'division' in self.data:
            try:
                division_id = int(self.data.get('division'))
                self.fields['subdivision'].queryset = SubDivision.objects.filter(division_id=division_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Subdivision queryset

        elif self.instance.pk:
            self.fields['division'].queryset = self.instance.zone.division_set.order_by('name')
            self.fields['subdivision'].queryset = self.instance.division.subdivision_set.order_by('name')