from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as AuthLogin
from django.contrib.auth.models import User
from .models import Account, Cart
import uuid
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            AuthLogin(request, user)
            return redirect('completeReg')
        else:
            messages.error(
                request, "We are sorry, the entered credentials are invalid.")
            return render(request, 'auth/login.html')
    else:
        return render(request, 'auth/login.html')


def send_mail_after_registration(email, token, user):
    subject = "TrendHaven Email Verification - Please Confirm Your Email Address"
    body = f"""
Dear {user.username},

Thank you for signing up for TrendHaven! To ensure the security and accuracy of your account, we kindly request that you verify your email address.

Please follow the instructions below to complete the email verification process:

Open your browser and paste the below link and you will be redirected to Complete Registration page.
Link: http:127.0.0.1:8000/verify/{token}

Thank you for choosing TrendHaven. We look forward to serve you!

Best regards,
Shaurya Samant
Developer
TrendHaven
https://trendhaven.pythonanywhere.com
Suggestions, if any, are welcome at https://trendhaven.pythonanywhere.com/contact/
    """
    from_email = "shauryasamant365@gmail.com"
    to_emails = [email]
    send_mail(subject, body, from_email, to_emails)


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username, email, password)
        messages.success(
            request, 'A verification email is being sent to you. Open the link to activate your account😉')
        auth_token = str(uuid.uuid4())
        profile_obj = Account.objects.create(user=user, auth_token=auth_token)
        profile_obj.save()
        send_mail_after_registration(email, auth_token, user)
        Cart.objects.create(belongs_to=user)
        return redirect('/token')
    else:
        return render(request, 'auth/signup.html')


def token_send(request):
    return redirect('index')


def verify(request, auth_token):
    try:
        profile_obj = Account.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.is_verified:
                messages.success(
                    request, 'Your account is being already verified.')
                return redirect('index')
            else:
                profile_obj.is_verified = True
                profile_obj.save()
                messages.success(
                    request, 'Your account is being successfully verified. Login and start your shopping & stay trending🤩')
                return redirect('login')
        else:
            messages.success(
                request, 'This request has an invalid token. Please try again or submit a contact.')
            return redirect('index')
    except Exception as e:
        return redirect('index')


@login_required
def completeReg(request):
    if request.method == "POST":
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        request.user.last_name, request.user.first_name = last_name, first_name
        request.user.save()
        messages.success(request, "Your account is created successfully!")
        return redirect("index")
    else:
        return render(request, 'auth/completeReg.html')


@login_required
def signout(request):
    logout(request)
    msg = "You have signed out successfully."
    messages.success(request, msg)
    return redirect("login")


@login_required
def deleteUser(request):
    request.user.delete()
    return redirect("index")


def account(request):
    if request.user.is_authenticated:
        return render(request, "auth/account.html")
    else:
        messages.success(
            request, 'You are logged in. Please login or sign up to view your profile.')
        return redirect('index')


@login_required
def update(request):
    if request.method == 'POST':
        post = request.POST
        request.user.username = post['username']
        request.user.first_name = post['first_name']
        request.user.last_name = post['last_name']
        request.user.email = post['email']
        request.user.account.mobile = post['mobile']

        request.user.save()
        return redirect('account')
