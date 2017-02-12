from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import KirrURL
# Create your views here.
def kirr_redirect_view(request,  shortcode=None, *args, **kwargs):
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	return HttpResponse("hello {shortcode}".format(shortcode=obj.url))


class KirrCBView(View):
	def get(self, request, shortcode=None, *args, **kwargs):
		# print(args)
		# print(kwargs)
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		return HttpResponse("Hello again")

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