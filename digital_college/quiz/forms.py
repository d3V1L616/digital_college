from django.forms import ModelForm
from .models import quiz,singlechoice,multiplechoice,matching,truefalse,respo_single,respo_multiple,respo_true,respo_match,answers
from django import forms
from django.contrib.admin import widgets
from djangoformsetjs.utils import formset_media_js
from checkboxselectmultiple.widgets import CheckboxSelectMultiple
# from .forms import 

ANSWER_CHOICES=(
    ('A','A'),
    ('B','B'),
    ('C','C'),
    ('D','D'),
)

ANSWER_TRUE_CHOICES=(
    ('T','True'),
    ('F','False'),
)

TYPE=(
    ('Single Option','Single Option'),
    ('Multiple Option','Multiple Option'),
    ('True False','True False'),
    ('Matching','Matching'),
)


class quiz_detail_form(ModelForm):
    name_of_quiz = forms.CharField( widget = forms.TextInput(attrs={'class':'validate','placeholder':'Enter the name of the quiz'}))
    instructions = forms.CharField( widget = forms.Textarea(attrs={'style':'height:100px','class':'input-fields col s7'}))
    class Meta:
        model=quiz
        fields=['name_of_quiz','instructions','start_time','end_time']

class single_correct_form(ModelForm):
    answer = forms.ChoiceField(choices=ANSWER_CHOICES ,widget=forms.Select(attrs={'name':'group1','type':'radio'}))
    class Meta:
        model=singlechoice
        fields=['question','option1','option2','option3','option4','marks','answer']
        

class multi_correct_form(ModelForm):
    options = forms.CharField(widget=forms.SelectMultiple(choices=ANSWER_CHOICES ))
    class Meta:
        model=multiplechoice
        fields=['question','option1','option2','option3','option4','marks','options']

class answer_form(ModelForm):
    option = forms.CharField(widget=forms.SelectMultiple(choices=ANSWER_CHOICES ))
    class Meta:
        model=answers
        fields=['option']


class matching_form(ModelForm):
    class Meta:
        model=matching
        fields=['question','option1','match1','option2','match2','option3','match3','option4','match4','marks']

class truefalse_form(ModelForm):
    answer = forms.ChoiceField(choices=ANSWER_TRUE_CHOICES ,widget=forms.Select(attrs={'name':'group1','type':'radio'}))
    class Meta:
        model=truefalse
        fields=['question','option1','marks','answer']
    
class response_single_form(ModelForm):
    class Meta:
        model=respo_single
        fields=['selected_option']

class response_multiple_form(ModelForm):
    selected_option=forms.ChoiceField(choices=ANSWER_CHOICES ,widget=forms.Select())
    class Meta:
        model=respo_multiple
        fields=['selected_option']

class response_true_form(ModelForm):
    selected_option=forms.ChoiceField(choices=ANSWER_TRUE_CHOICES,widget=forms.Select())
    class Meta:
        model=respo_true
        fields=['selected_option']

class response_matching_form(ModelForm):
    #selected_option=forms.ChoiceField(choiceswidget=forms.Select())
    class Meta:
        model=respo_match
        fields=['selected_option']

