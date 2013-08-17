from django.shortcuts import redirect
from django.http.response import HttpResponseForbidden

def save_form(request):
	"""Get result from form editor and save it to the database"""
	
	if request.method is not "POST":
		return HttpResponseForbidden("Access Forbidden; No data is sent via POST.")
	
	question_texts = []
	helptxts = []
	form_types = []
	
	i = 0
	while True:
		question_texts.insert(i, request.POST["qtext_%s" % i])
		helptxts.insert(i, request.POST["qhelptxt_%s" % i])
		form_types.insert(i, request.POST["formtype_%s" % i])

		if form_types[i] == 0: # FormType.Text
			
		elif form_types[i] == 1: # FormType.List
			
	# TODO add processes to save form in the session.
	return redirect("/editor/process")
	