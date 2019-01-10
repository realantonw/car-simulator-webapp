from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template.loader import get_template
from django.template import Context
from django.views.generic.base import TemplateView
from airapp.models import Car
from django.core import serializers
import os, re, math
import json
from django import forms
#########################

def calc_LuftWiderstand(aS, cw, D, v):
	return float((aS/2) * cw * D * v*v))

def calc_RollWiderstand(Cr, m, g):
	return float((Cr*m*g))

def calc_Fbeschl(m,a):
	return float((m*a))

def calc_v(a, t1, t2,, vo ):
    return float(vo + a*(t2-t1)^2)

def calc_posy (y, a, t2, t1, lw, v):
    return float(0,5*a*(t2-t1)^2+v*(t2-t1)*cos(lw) + y)

def calc_posx (x, a, t2, t1, lw, v):
    return float(0,5*a*(t2-t1)^2+v*(t2-t1)*sin(lw) + x)

def calc_a (gas):
    return (gas/100*7)

def calc_dec (bremse):
    return (bremse/100*10)

#########################

class MyForm(forms.Form):

	windgeschwindigkeit = forms.FloatField(max_length=50)
    rollwiderstandskoeffizient = forms.FloatField(max_length=50)
    masseFahrzeug = forms.FloatField(max_length=50)
    masseInsassen = forms.FloatField(max_length=50)
    stirnflaechefahrzeug = forms.FloatField(max_length=50)
    gas = forms.FloatField(max_length=50)
    bremse = forms.FloatField(max_length=50)
    lenkwinkel = forms.FloatField(max_length=50)

def formview(request):

	# If the form has been submitted...
	if request.method == 'POST':

		# A form bound to the POST data that has fields for user name and user password
		form = MyForm(request.POST)

		# All validation rules pass
		if form.is_valid():

			windgeschwindigkeit = form.cleaned_data['windgeschwindigkeit']
            rollwiderstandskoeffizient = form.cleaned_data['rollwiderstandskoeffizient']
            masseFahrzeug = form.cleaned_data['masseFahrzeug']
            masseInsassen = form.cleaned_data['masseInsassen']
            stirnflaechefahrzeug = form.cleaned_data['stirnflaechefahrzeug']
            gas = form.cleaned_data['gas']
            bremse = form.cleaned_data['bremse']
            lenkwinkel = form.cleaned_data['lenkwinkel']

			# check that codes exists in database
			if (1==1):

				# calculate dist bet the airports from their latitudes and longitudes

				mygas = calc_a(gas)

				# render out.html, a page telling the user the distance
				return render(request, 'carsimulator/out.html', {'distance':mygas})

			# if not, go to "fail" page
			else:
				# Redirect to fail page after POST
				return HttpResponseRedirect('/carsimulator/fail/')

	else:
		# An unbound form
		form = MyForm()

	# pass variables: form
	return render(request, 'carsimulator/formtemplate.html', {'form': form})

def failview(request):
	'''A view to send user to the fail page if he enters the wrong airport codes'''

	return render(request, 'carsimulator/fail.html')

#def getnamesview(request):
#	'''This view is for autocompleting - see tutorial at
#	http://flaviusim.com/blog/AJAX-Autocomplete-Search-with-Django-and-jQuery/'''
#
#	if request.is_ajax():
#		q = request.GET.get('term', '')
#		simulations = simulation.objects.filter(longname__icontains = q )[:20]
#		results = []
#		for airport in airports:
#			airport_json = {}
#			airport_json['id'] = airport.code
#			airport_json['label'] = airport.longname
#			airport_json['value'] = airport.code
#			results.append(airport_json)
#		data = json.dumps(results)
#	else:
#		data = 'fail'
#	mimetype = 'application/json'
#	return HttpResponse(data, mimetype)
