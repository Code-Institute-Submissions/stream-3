from django.shortcuts import render
from .models import Entertainer
from django.shortcuts import render, get_object_or_404
from .forms import EntertainerForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Main index page
def entertainer_index(request):
	entertainers = Entertainer.objects.all()[:6]
	return render(request, 'index.html', {'entertainers': entertainers,})

# List all entertainers
def entertainer_list(request):
	entertainers = Entertainer.objects.all()
	return render(request, 'entertainer_list.html', {'entertainers': entertainers,})

# Entertainer details
def entertainer_detail(request, pk):
    entertainer = get_object_or_404(Entertainer, pk=pk)
    return render(request, 'entertainer_detail.html', {'entertainer': entertainer})

# Create new entertainer
@login_required(login_url='/login/')
def entertainer_new(request):
    if request.method == "POST":
        form = EntertainerForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect(entertainer_detail, post.pk)
    else:
        form = EntertainerForm()
    return render(request, 'entertainer_new.html', {'form': form})
