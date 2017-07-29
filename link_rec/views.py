from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
from link_rec.forms import SignUpForm
from .models import Profile
import ast
from link_rec.link_new.temp_jobtitle_classifier import nb_classification




#@login_required(login_url='login/')
def personal_view(request):
#    if request.method == 'GET':
    return render(request, 'button.html')


def parse_to_list(form_input):
    l = ast.literal_eval(form_input)
    l = [i.strip() for i in l]
    return l


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.name = form.cleaned_data.get('name')
            current_school = form.cleaned_data.get('school')
            school_program = form.cleaned_data.get('school_program')
            school_of_interest = form.cleaned_data.get('school_of_interest')
            industry_of_interest = form.cleaned_data.get('industry_of_interest')
            # print(industry_of_interest)  # ['software', 'data_science', 'research']
            li_industry = nb_classification.recommend_industry(industry_of_interest)
            user.profile.current_school = current_school
            user.profile.school_program = school_program
            user.profile.school_of_interest = school_of_interest
            user.profile.industry_of_interest = industry_of_interest
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            request.session['current_user'] = li_industry
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login/')
def home(request):
    current_user = request.session.get('current_user')
    profile_info = [nb_classification.get_profile_info(id) for id in current_user]
    # industry_of_interest = current_user.industry_of_interest
    # li_industry = nb_classification.recommend_industry(industry_of_interest)
    # return render(request, "home.html")
    return render(request, "home.html", {'industry_recommend': profile_info})



#def ind(request):
    # if request.method == 'POST':
    #     form = AuthorForm(request.POST)
    #     if form.is_valid():
    #         y = form.save()
    #         print(form.cleaned_data.get('title'))
    #         return redirect('home')
    # else:
    #     form = AuthorForm()
#    if request.method == 'POST':
#        form = FormForm(request.POST)
#        if form.is_valid():
#            print(form['e'])
#            return redirect('home')
#    else:
#        form = FormForm()
#    return render(request, 'index.html', {'form': form})
#

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=user.username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})


