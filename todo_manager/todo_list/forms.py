from django import forms

from todo_list.models import ToDoItem


class ToDoItemCreateForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ("title", "description", )
        widgets = {"description": forms.Textarea(attrs={"cols": 40, "rows": 5}, ), }

        help_texts = {
            "description": "Some useful help texts",
        }


class ToDoItemUpdateForm(forms.ModelForm):
    class Meta(ToDoItemCreateForm.Meta):
        fields = ("title", "description", "done")
