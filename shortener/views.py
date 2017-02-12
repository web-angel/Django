from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from .forms import SubmitUrlForm
from .models import KirrURL
# Create your views here.

class HomeView(View):
	def get(self, request, *args, **kwargs):
		form = SubmitUrlForm()
		context = {
			"title": "SUbmit your url",
			"form": form
		}
		return render(request, "shortener/home.html", context)

	def post(self, request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)

		context = {
			"title": "SUbmit your url",
			"form": form
		}

		template = "shortener/home.html"

		if form.is_valid():
			print(form.cleaned_data)
			new_url = form.cleaned_data.get("url")
			obj, created = KirrURL.objects.get_or_create(url=new_url)
			context = {
				"object": obj,
				"created": created,
			}

			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		
		return render(request, template, context)


def kirr_redirect_view(request,  shortcode=None, *args, **kwargs):
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	# return HttpResponse("hello {shortcode}".format(shortcode=obj.url))
	return HttpResponseRedirect(obj.url)


class KirrCBView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		# print(args)
		# print(kwargs)
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		# return HttpResponse("Hello again")
		return HttpResponseRedirect(obj.url)

	def post(self, request, *args, **kwargs):
		return HttpResponse()


'''
def kirr_redirect_view(request,  shortcode=None, *args, **kwargs):
	# print(args)
	# print(kwargs)
	# print(shortcode)

	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	obj_url = obj.url
	#first way
	# try:
	# 	obj = KirrURL.objects.get(shortcode=shortcode)
	# except:
	# 	obj = KirrURL.objects.all().first()

	#secondway
	# obj_url = None
	# qs = KirrURL.objects.filter(shortcode__iexact=shortcode.upper())
	# if qs.exists() and qs.count() == 1:
	# 	obj = qs.first()
	# 	obj_url = obj.url

	return HttpResponse("hello {shortcode}".format(shortcode=obj_url))
'''