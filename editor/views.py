from django.shortcuts import redirect
from django.http.response import HttpResponseForbidden

def save_form(request):
	"""Get result from form editor and save it to the database"""
	
	if request.method is not "POST":
		return HttpResponseForbidden("Access Forbidden; No data is sent via POST.")
	
	question_text = []
	helptxt = []
	
	i = 0
	while True:
		question_text.append(request.POST["qtext_%s" % i])
		question_text.append(request.POST["qhelptxt_%s" % i])
		question_text.append(request.POST["formtype_%s" % i])


	
	# TODO add processes to save form in the session.
	return redirect("/editor/process")
	