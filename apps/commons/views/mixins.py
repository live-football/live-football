

class ControlModelViewMinix(object):
    def form_valid(self, form):

        if form.non_field_errors():
            return super().form_invalid()

        if not self.object:
            form.instance.created_user = self.request.user
        form.instance.updated_user = self.request.user

        return super().form_valid(form)
