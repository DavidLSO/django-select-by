# django-select-by

in your form.py
class MyForm(forms.Form):
   
    banco = forms.ModelChoiceField(label='Banco', required=CADASTRAL, widget=forms.Select(),
                                   queryset=Banco.objects.all())
    agencia = forms.ModelChoiceField(label='Agência', required=CADASTRAL, widget=SelectParent(select_by='banco'),
                                     queryset=Agencia.objects.all())

in your template
<script src="{% static 'js/select_by.js' %}"></script>
(function($)
{
    $('#id_banco').change(function()
    {
        var agencia = $('#id_agencia').val();

        if($(this).val() && $(this).val() > 0)
            hide_or_not_options('id_agencia', $(this).val());

        $('#id_agencia').val(agencia);
    })
    .trigger('change');
})
(jQuery);

                                     
                                     
