from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import UserLogin, Admin



def home(request):
    admin_details = Admin.objects.last()  

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        qr_image = request.FILES.get('qr')

        user = UserLogin(name=name, email=email, phone=phone, qr_image=qr_image)
        user.save()
        messages.success(request, "User data saved successfully!")

        return render(request, 'index.html', {"admin_details": admin_details})

    
    return render(request, 'index.html', {"admin_details": admin_details})
    return redirect("success")



def success(request):
    return render(request, "success.html")



def admin_dashboard(request):
   
    users = UserLogin.objects.all()
    admin_data = Admin.objects.all()
    return render(request, 'admin_dashboard.html', {'users': users, 'admin_data': admin_data})



def edit_user(request, user_id):
    user = get_object_or_404(UserLogin, id=user_id)
    if request.method == 'POST':
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')
        if 'qr_image' in request.FILES:
            user.qr_image = request.FILES['qr_image']
        user.save()
        messages.success(request, "User updated successfully!")
        return redirect('admin_dashboard')
    return render(request, 'edit_user.html', {'user': user})



def delete_user(request, user_id):
    user = get_object_or_404(UserLogin, id=user_id)
    user.delete()
    messages.success(request, "User deleted successfully!")
    return redirect('admin_dashboard')



def edit_form(request):
    change_details = None  
    if request.method == "POST":
        course_name = request.POST.get("course_name")
        date = request.POST.get("date")
        qr_change = request.FILES.get('qr_change')
        change_details = Admin(course_name=course_name, date=date, qr_change=qr_change)
        change_details.save()
        messages.success(request, "Admin details updated successfully!")

    return render(request, "edit_form.html", {"change_details": change_details})
