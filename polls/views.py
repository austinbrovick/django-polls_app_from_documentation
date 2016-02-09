from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse


from .models import Question, Choice




def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)



def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #returns object or 404 error
    return render(request, 'polls/detail.html', {'question': question}) #if there is no error, render template


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #get object or return a 404 error
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice']) # get the choice id from the form, 'choice' is the name of the input
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1 # modifies the votes
        selected_choice.save() # and then saves the modified vote total
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,))) # this is similar to a redirect and it passes a question.id arg with a comma for future args



def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question}) # renders template with question dictionary
