from django.shortcuts import render
from .forms import DataForm

# Create your views here.

def contact_view(request):
    submitted=False
    if request.method=='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            #form.save()
            submitted=True
    else:
        form=DataForm()
    return render(request,'contact.html',{'form':form,'submitted':submitted})
