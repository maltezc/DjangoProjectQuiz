from django.shortcuts import render
from django.views import generic
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages

from django.http import Http404

from . import models
from . import forms

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class QuestionList(generic.ListView):
    model = models.Question
    select_related = ("user", "group")


class QuestionDetail(generic.DetailView):
    model = models.Question

    # suggested take out from stack overflow. no reason given.
    # def get_queryset(self):
    #     queryset = super().get_queryset()


class UserQuestions(generic.ListView):
    model = models.Question
    template_name = "Questions/user_question_list.html"

    # suggested take out from stack overflow. no reason given.
    # def get_queryset(self):
    #     try:
    #         self.question_user = User.objects.prefetch_related("questions").get(
    #             username__iexact=self.kwargs.get("username")
    #         )
    #     except User.DoesNotExist:
    #         raise Http404
    #     else:
    #         return self.question_user.questions.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["question_user"] = self.question_user
        return context


class CreateQuestion(generic.CreateView):
    model = models.Question
    # form = QuestionForm
    fields = ('question', 'answer')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


class DeleteQuestion(generic.DeleteView):
    model = models.Question
    success_url = reverse_lazy('questions:all')

    #suggested take out from stack overflow. no reason given.
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     return queryset.filter(user_id=self.request.user.id)

    def delete(self, *args, **kwargs):
        messages.success(self.request, "Question Deleted")
        return super().delete(*args, **kwargs)



