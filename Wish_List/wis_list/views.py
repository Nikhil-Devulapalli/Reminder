from django.shortcuts import render,redirect
from wis_list.models import List
from .forms import ListForm
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items= List.objects.all
            messages.success(request,("Items has been added!"))
            return render(request,'home.html',{'all_items':all_items})
    else:
        all_items = List.objects.all
        return render(request,'home.html',{'all_items':all_items})




def delete(request,List_id):
    item= List.objects.get(pk=List_id)
    item.delete()
    messages.success(request,("item has deleted"))
    return redirect("home")



def edit(request,List_id):
    if request.method == "POST":
        item= List.objects.get(pk=List_id)
        form=ListForm(request.POST or None,instance=item)
        if form.is_valid():
            form.save()
            messages.success(request,("Item has been edited! "))
            return redirect('home')
    else:
        item=List.objects.get(pk=List_id)
        return render(request,'edit.html',{'item':item})
   
