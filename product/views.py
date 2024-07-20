import random2
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *
from django.views import View
# Create your views here.
def index(request):
    fruits = product.objects.all()
    vegitables = product.objects.filter(category="vg")
    allft = product.objects.filter(category = "ft")
    bread = product.objects.filter(category = "bd")
    meat = product.objects.filter(category = "mt")

    return render(request,"index.html", {'fruits' : fruits, 'vegitables': vegitables, 'allft': allft, 'bread':bread, 'meat':meat,})

def four(request):
    return render(request, "404.html")

def cart(request):
    return render(request, "cart.html")

def chackout(request):
    return render(request, "chackout.html")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        Data = contactform(name=name, email=email, message=message)
        Data.save()

    return render(request, "contact.html")

def shop_detail(request):
    return render(request, "shop-detail.html")

def shop(request):
    return render(request, "shop.html")

def test(request):
    return render(request, "testimonial.html")

def registration(request):
    return render(request,'Registration.html')

def fetchregister(request):
    if request.method == 'POST':
        username = request.POST.get('uname')
        email = request.POST.get('uemail')
        mobile = request.POST.get('uphone')
        city = request.POST.get('ucity')
        propic = request.FILES.get('propic')
        password = request.POST.get('upassword')

        try:
            checkdata = user.objects.get(email_id=email)
            if checkdata is not None:
                messages.error(request,'User already exists, please choose another email!')
        except:
            checkdata = None

        digitcount = 0
        capitalcount = 0
        specialcount = 0

        if checkdata is None:
            if len(password) >= 8:
                for i in range(0,len(password)):
                    if ord(password[i]) >= 48 and ord(password[i]) <= 57:
                        digitcount = digitcount + 1
                    if ord(password[i]) >= 65 and ord(password[i]) <= 90:
                        capitalcount = capitalcount + 1
                    if ord(password[i]) == 35 or ord(password[i]) == 64 or ord(password[i]) == 36:
                        specialcount = specialcount + 1

                if digitcount >= 1 and specialcount >= 1 and capitalcount >= 1:
                    password_check = True
                else:
                    messages.error(request, 'Please enter at least one digit,capital,small,special characters')
                    password_check = False
                if password_check is True:
                    if propic is not None:
                        insertdetails = user(name=username, email_id=email, mobile_no=mobile,city=city, propic=propic, password=password)
                        insertdetails.save()
                        messages.success(request, "Sign Up is Successfully Completed, Now you can Sing In!")
                        
                        from django.core.mail import send_mail

                        send_mail(
                            'Registration Sucessfully',
                            "Hello "+str(username)+ " Welcome To Registration Our Travaling Website Traveler's Bible\n"
                            "Thank you for choosing Traveler's Bible,\n For Better Experience Please Login Traveler's Bible\n"
                            "Your Login Id & Password Below"
                            "ID : "+str(email)+"\n Password : "+str(password),
                            'rishabhkhatri192@gmail.com',
                            [email],
                            fail_silently=False,
                        ) 
                        return redirect(login)
                    else:
                        insertdetails = user(name=username, email_id=email, mobile_no=mobile, city=city, propic='media/img/avatar.jpg',password=password)
                        insertdetails.save()
                        messages.success(request, "Sign Up is Successfully Completed, Now you can Sing In!")
                        
                        from django.core.mail import send_mail

                        send_mail(
                            'Registration Sucessfully',
                            "Hello "+str(username)+ " Welcome To Registration Our Travaling Website Traveler's Bible"
                            "Thank you for choosing Traveler's Bible,\n For Better Experience Please Login Traveler's Bible"
                            "Your Login Id & Password Below"
                            "ID : "+str(email)+"\n Password : "+str(password),
                            'rishabhkhatri192@gmail.com',
                            [email],
                            fail_silently=False,
                        ) 
                        return redirect(login)
            else:
                messages.error(request,'Password must be 8 characters long!')
        else:
            messages.error(request,'Something went wrong!')
    return render(request,'Registration.html')

def login(request):
    return render(request,'Login.html')

def fetchlogin(request):
    if request.method == 'POST':
        email = request.POST.get('uemail')
        password = request.POST.get('upassword')

        try:
            checkdata = user.objects.get(email_id=email,password=password)
            request.session['logname'] = checkdata.name
            request.session['logid'] = checkdata.id
            request.session.save()
        except:
            checkdata = None

        if checkdata is not None:
            return redirect(index)
        else:
            messages.error(request,'User Not Found, Please Enter Right Email and Password!')

    return render(request,'Login.html')

def logout(request):
    try:
        del request.session['logname']
    except:
        pass
    return render(request, 'Login.html')

def forgot(request):
    return render(request,'reset_password.html')

def forgotpassword(request):
    if request.method == 'POST':
        usernamee = request.POST['email']
        print(usernamee)
        try:
            username = user.objects.get(email_id=usernamee)

        except user.DoesNotExist:
            username = None

        print(username)
        #if user exist then only below condition will run otherwise it will give error as described in else condition.
        if username is not None:
            #################### Password Generation ##########################
            import random
            letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
                       'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
            numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
            symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

            nr_letters = 6
            nr_symbols = 1
            nr_numbers = 3
            password_list = []

            for char in range(1, nr_letters + 1):
                password_list.append(random.choice(letters))

            for char in range(1, nr_symbols + 1):
                password_list += random.choice(symbols)

            for char in range(1, nr_numbers + 1):
                password_list += random.choice(numbers)

            print(password_list)
            random.shuffle(password_list)
            print(password_list)

            password = ""  #we will get final password in this var.
            for char in password_list:
                password += char

            ##############################################################


            msg = "hello here it is your new password  "+password   #this variable will be passed as message in mail

            ############ code for sending mail ########################

            from django.core.mail import send_mail

            send_mail(
                'Your New Password',
                msg,
                'kaushalpanchal612@gmail.com',
                [usernamee],
                fail_silently=False,
            )
            # NOTE: must include below details in settings.py
            # detail tutorial - https://www.geeksforgeeks.org/setup-sending-email-in-django-project/
            # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
            # EMAIL_HOST = 'smtp.gmail.com'
            # EMAIL_USE_TLS = True
            # EMAIL_PORT = 587
            # EMAIL_HOST_USER = 'mail from which email will be sent'
            # EMAIL_HOST_PASSWORD = 'pjobvjckluqrtpkl'   #turn on 2 step verification and then generate app password which will be 16 digit code and past it here

            #############################################

            #now update the password in model
            cuser = user.objects.get(email_id=usernamee)
            cuser.password = password
            cuser.save(update_fields=['password'])

            print('Mail sent')
            messages.info(request, 'mail is sent')
            return redirect(index)

        else:
            messages.info(request, 'This account does not exist')
    return redirect(index)



