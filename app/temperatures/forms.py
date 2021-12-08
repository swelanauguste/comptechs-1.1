from django import forms


from .models import Temperature


class TemperatureCreateForm(forms.ModelForm):
    """
    Temperature create form
    """

    class Meta:
        model = Temperature
        fields = "__all__"
        exclude = ("created_by", "updated_by",)
