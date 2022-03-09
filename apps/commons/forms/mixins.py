from django import forms


class ControlModelFormMixin(forms.ModelForm):
    def form_valid(self, form):

        if form.non_field_errors():
            return super().form_invalid()

        if not self.object:
            form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user

        return super().form_valid(form)


class SoftControlControlModelFormMixin(ControlModelFormMixin):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['live'].widget = forms.HiddenInput()


class HardControlControlModelFormMixin(ControlModelFormMixin):
    pass
