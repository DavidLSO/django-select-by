# django-select-by [This project is under development]

## Description
Project, which brings a widget, which has the function of loading a select list from another select list.

## Requirements
1. This project was made for Django projects.
2. The two fields involved must be linked to by forekeys.

## Step by step
1. To install you should use the command `pip install django_select_by`
2. In your `form.py` file you must import the `django_select_by` lib and used in the field to be populated, it must be of type `ModelChoiceField` using the `SelectBy` widget (select_by = 'bank') passing the parent.
```
fromt django_select_by.widget import SelectBy

class MyForm(forms.Form):
   
    banco = forms.ModelChoiceField(label='Banco', required=CADASTRAL, widget=forms.Select(),
                                   queryset=Banco.objects.all())
    agencia = forms.ModelChoiceField(label='Agência', required=CADASTRAL, widget=SelectBy(select_by='banco'),
                                     queryset=Agencia.objects.all())
```
3. In your template you must include the file `select_by.js` and use in your change method of the parent field the` select_by` method
```
{% include 'django_select_by/select_by.html' %}

(function($)
{
    $('#id_banco').change(function()
    {
        var agencia = $('#id_agencia').val();

        if($(this).val() && $(this).val() > 0)
            select_by('id_agencia', $(this).val());

        $('#id_agencia').val(agencia);
    })
    .trigger('change');
})
(jQuery);
```
