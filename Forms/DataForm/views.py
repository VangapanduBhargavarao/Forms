from django.shortcuts import render
from .forms import contact_form
from .models import Contact_form
from django.http import HttpResponse

# Create your views here.
def data_stroe(request):
    if request.method=="POST":
        form=contact_form(request.POST)
        if form.is_valid():
            Contact_form.objects.create(
                name=form.cleaned_data["name"],
                email=form.cleaned_data["email"],
                message=form.cleaned_data["feedback"]
            )
            return HttpResponse("success")
    else:
        form=contact_form()
    return render(request,'form.html',{'form':form})

    