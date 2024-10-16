from django.http import (
    HttpResponseRedirect, HttpResponse, HttpResponseNotFound, Http404, StreamingHttpResponse, FileResponse,
    JsonResponse)
from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy, reverse
from django.template.loader import get_template, render_to_string
from django.template.response import TemplateResponse

from .models import Bb, Rubric
from .forms import BbForm


def index(request):
    # template = loader.get_template('bboard/index.html')
    # bbs = Bb.objects.all()
    # rubrics = Rubric.objects.all()
    # context = {'bbs': bbs, 'rubrics': rubrics}
    # return render(request, 'bboard/index.html', context)

    # resp = HttpResponse('Here will be announcements',
    #                     content_type='text/plain; charset=utf-8')
    # resp.write(' about')
    # resp.writelines((' all', ' things'))
    # resp['keywords'] = 'Python, Django'
    # return resp
    # bbs = Bb.objects.all()
    # rubrics = Rubric.objects.all()
    # context = {'bbs': bbs, 'rubrics': rubrics}
    # template = get_template('bboard/index.html')
    # return HttpResponse(
    #     template.render(context=context, request=request)
        # render_to_string('bboard/index.html', context=context, request=request)
    # )
    # return TemplateResponse(request, 'bboard/index.html', context=context)
    # resp_content = ('Here', ' will', ' be', ' main',' page')
    # resp = StreamingHttpResponse(resp_content, content_type='text/plain; charset=utf-8')
    # return resp
    data = {'title': 'Bycylce', 'content': 'used', 'price': 10000.0, }
    return JsonResponse(data)
    # filename = r'/Users/beksultanesenkulov/Documents/IT/image.png'
    # return FileResponse(open(filename, 'rb'), as_attachment=True)

def by_rubric(request, rubric_id):

    # current_rubric = get_object_or_404(Rubric, pk=rubric_id)
    rubrics = Rubric.objects.all()
    current_rubric = Rubric.objects.get(pk=rubric_id)
    bbs = Bb.objects.filter(rubric=rubric_id)
    context = {'bbs': bbs, 'rubrics': rubrics, 'current_rubric': current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context


# def add(request):
#     bbf = BbForm
#     context = {'form': bbf}
#     return render(request, 'bboard/create.html', context)
#
#
# def add_save(request):
#     bbf = BbForm(request.POST)
#     if bbf.is_valid():
#         bbf.save()
#         return HttpResponseRedirect(reverse('by_rubric', kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
#     else:
#         context = {'form': bbf}
#         return render(request, 'bboard/create.html', context)


def add_and_save(request):
    if request.method == 'POST':
        bbf = BbForm(request.POST)
        if bbf.is_valid():
            bbf.save()
            return HttpResponseRedirect(reverse('by_rubric',
                                                kwargs={'rubric_id': bbf.cleaned_data['rubric'].pk}))
        else:
            context = {'form': bbf}
            return render(request, 'bboard/create.html', context)
    else:
        bbf = BbForm
        context = {'form': bbf}
        return render(request, 'bboard/create.html', context)


def detail(request, bb_id):
    try:
        bb = Bb.objects.get(pk=bb_id)
    except Bb.DoesNotExist:
        # return HttpResponseNotFound('This announcement does not exist')
        raise Http404('This announcement does not exist')
    return HttpResponse()
