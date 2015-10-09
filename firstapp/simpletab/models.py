from django.db import models
from django.forms import ModelForm

# Create your models here.
class Tab_model(models.Model):
    texts_field = models.CharField(max_length=200)
    decimal_field = models.DecimalField(max_digits=12, decimal_places=3) 

    def __unicode__(self):
        return self.texts_field

class TabForm(ModelForm):
    class Meta:
        model = Tab_model
        fields = ['texts_field', 'decimal_field'] 
