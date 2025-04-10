from django import forms
from .models import Machine, RepairRequest

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ('id','name','serial_number','importance','status')


class RepairRequestForm(forms.ModelForm):
    class Meta:
        model = RepairRequest
        fields = ['machine', 'issue_description', 'status']  # only fields user should input
        widgets = {
            'issue_description': forms.Textarea(attrs={'rows': 4}),
             'status': forms.Select(),
        }

    def __init__(self, *args, **kwargs):
        super(RepairRequestForm, self).__init__(*args, **kwargs)
        self.fields['machine'].queryset = Machine.objects.all()