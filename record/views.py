from django.shortcuts import render, redirect  
from record.forms import RecordForm  
from record.models import Record  

# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = RecordForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = RecordForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    records = Record.objects.all()  
    return render(request,"show.html",{'records':records})  
def edit(request, id):  
    record = Record.objects.get(id=id)  
    return render(request,'edit.html', {'record':record})  
def update(request, id):  
    record = Record.objects.get(id=id)  
    form = RecordForm(request.POST, instance = record)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'record': record})  
def destroy(request, id):  
    record = Record.objects.get(id=id)  
    record.delete()  
    return redirect("/show")  