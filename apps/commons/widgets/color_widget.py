from django.forms import TextInput


class ColorWidget(TextInput):
    input_type = 'color'
    # template_name = 'myapp/forms/widgets/color.html'
