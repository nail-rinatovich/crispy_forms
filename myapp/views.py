from django.shortcuts import render, redirect
from .forms import ContactForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_GET

def homePageView(request):
    return redirect('index')

def index(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            # Return form errors in JSON format
            errors = form.errors.as_json()
            return JsonResponse({'success': False, 'errors': errors}, status=400)
    else:
        form = ContactForm()
    return render(request, 'index.html', {'form': form})

@require_GET
def robots_txt(request):
    lines = [
        "User-Agent: *",
        "Disallow: /private/",
        "Disallow: /junk/",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")
