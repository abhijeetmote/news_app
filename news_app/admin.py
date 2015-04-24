from django.contrib import admin
from news_app.models import Post_news
from django import forms
from news_app.forms import newsForm



""" Creating the NewsAdming class, for customizing the view on admin panel """

class NewsAdmin(admin.ModelAdmin):
    form = newsForm
    filter_horizontal = ("clients",)        
    fieldsets = [
        ('Post Message',     {'fields': ['message']}),
        ('Message Severity', {'fields': ['severity']}),
#        ('Creation Date',    {'fields': ['creation_date']}),
#        ('Updation Date',    {'fields': ['updation_date']}),
#        ('Created By',       {'fields':['created_by']})
        ('Clients',         {'fields' :['clients']}),
    ]
     
    """Used to save the user name who has created the post"""
    def save_model(self, request, obj, form, change):            
        obj.created_by = request.user
        obj.save()

    # Display the view after inserting the data
    list_display = ('id','message','severity','creation_date', 'updation_date','created_by')
    
    # filter by creation date
    list_filter = ['creation_date']
    
    # filter by updation date    
    list_filter = ['updation_date']
    search_fields = ['question']

# Adding the NewsAdmin class to the admin panel
admin.site.register(Post_news,NewsAdmin)
