from django import forms
from news_app.models import Post_news

""" Creating form widget - TextArea """

class newsForm(forms.ModelForm): 
    """ TO set the default value manually """
    def __init__(self, *args, **kwargs):
        super(newsForm, self).__init__(*args, **kwargs)
        # assign a (computed, I assume) default value to the choice field
        self.initial['severity'] = 'Low'                    
        
    class Meta:
        # Adding model to the form
        model = Post_news
        
        # Creating the widget TextArea with rows and columns
        widgets = {'message': forms.Textarea(attrs={'cols': 80, 'rows': 5})}            

    