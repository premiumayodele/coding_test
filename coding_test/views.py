from django.shortcuts import HttpResponse, render, redirect
from django.views.generic import View
from . app.forms import HyphForm


class HomePageView(View):
    template_name = 'consecutive.html'
    form_class = HyphForm

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            return HttpResponse('On the way to good')
            print('as intended')
            aa = form.cleaned_data['hyphvalue']
            # return redirect('resp')
        #     form.save()
        #     messages.success(request, 'Well done! Fitness Class has been booked for you. If you would like to cancel booked fitness class, please contact our office.')
        #     return HttpResponseRedirect('/')
        else:
            print('the else part')
            # return HttpResponse('Oh snap! Fill/correct all fields and try submitting again.')
            return redirect('resp')
        return render(request, self.template_name, {'form': form, 'resp': aa})
        print('i am not working')

def homepage(request):
    form = HyphForm()

    # question = None
    # if 'submit' in request.POST:
    #     hyphen = request.GET.get('hyphnumber')

    #     # aa = "Making progress"
    #     question = hyphen
    #     print('making headway!')
    #     print(question)
        # context{'resp': request.POST.get('query','')}
    return render(request, 'consecutive.html', {'form': form})
    # print('this is not working')

def resp(request):
    return HttpResponse("I am working as expected")