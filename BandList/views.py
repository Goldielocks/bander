from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import RequestContext
from BandList.models import Location, Genre, Band, Show, UserProfile
from BandList.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
	context = RequestContext(request)

	profile = UserProfile.objects.get(user = request.user)

	bandList = profile.bands
	showList = profile.shows

	print bandList.all

	return render_to_response('home.html', {"bandList":bandList, "showList":showList}, context)

@login_required
def bands(request):
	context = RequestContext(request)

	profile = UserProfile.objects.get(user = request.user)

	bandList = profile.bands.all()
	totalList = Band.objects.all()

	for item in bandList:
		totalList = totalList.exclude(name = item)


	return render_to_response('bands.html', {"following":bandList, "notfollowing":totalList}, context)

@login_required
def shows(request):
	context = RequestContext(request)

	profile = UserProfile.objects.get(user = request.user)

	showList = profile.shows.all()
	totalList = Show.objects.all()

	for item in showList:
		totalList = totalList.exclude(id = item.id)


	return render_to_response('bands.html', {"following":showList, "notfollowing":totalList}, context)

	return render(request, 'shows.html')

@login_required
def add(request):
	context = RequestContext(request)
	profile = UserProfile.objects.get(user = request.user)

	if request.method == 'GET':
		id = request.GET["id"]
		dataType = request.GET["dataType"]

		if dataType == 'band':
			newData = Band.objects.get(id = id)
			profile.bands.add(newData)
			profile.save()


	return JsonResponse( {"status":"okay"} )

@login_required
def remove(request):
	context = RequestContext(request)
	profile = UserProfile.objects.get(user = request.user)

	if request.method == 'GET':
		id = request.GET["id"]
		dataType = request.GET["dataType"]
		if dataType == 'band':
			newData = Band.objects.get(id = id)
			profile.bands.remove(newData)
			profile.save()
			
	return HttpResponse("Things are good!")


def base(request):
	if not request.user.is_authenticated():
		return render(request, 'base.html')
	else:
		return HttpResponseRedirect('/BandList/home/')

def user_login(request):
	context = RequestContext(request)

	if request.method == 'POST':

		username = request.POST['username']
		password = request.POST['password']

		user = authenticate(username = username, password = password)

		if user:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/BandList/')
			else:
				return HttpResponse("Your account is disabled")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid credentials")

	else:
		return render_to_response('login.html', {}, context)

def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()

			user.set_password(user.password)
			user.save()

			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			registered = True
		else:
			print user_form.errors, profile_form.errors

	else:
		user_form = UserForm()
		profile_form = UserProfileForm()

	return render_to_response(
		'register.html',
		{'user_form':user_form, 'profile_form':profile_form, 'registered':registered},
		context)
