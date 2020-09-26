from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .forms import LinkForm
from shorter.models import Link
# Create your views here.

def index(request):
    form = LinkForm
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            url = request.POST.get('url')
            if Link.objects.filter(url=url).exists():
                link = Link.objects.get(url=url)
            else:
                link = form.save()
            messages.info(request, f"Your URL was successfully created!")
            context['url'] = request.build_absolute_uri() + link.code
        else:
            messages.error(request, 'An error occured')

    return render(request, 'shorter/index.html', context)


def link_redir(request, code):
    link = get_object_or_404(Link, code=code)
    return redirect(f'{link.url}')
