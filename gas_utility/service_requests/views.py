from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import ServiceRequest
from .forms import ServiceRequestForm
from django.utils.timezone import now

@login_required
def submit_request(request):
    if request.method == "POST":
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user
            service_request.save()
            return redirect('track_requests')
    else:
        form = ServiceRequestForm()
    return render(request, 'service_requests/submit_request.html', {'form': form})

@login_required
def track_requests(request):
    requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'service_requests/track_requests.html', {'requests': requests})

@login_required
def resolve_request(request, request_id):
    if request.user.is_staff:
        service_request = ServiceRequest.objects.get(id=request_id)
        service_request.status = 'Resolved'
        service_request.resolved_at = now()
        service_request.save()
        return redirect('admin:service_requests_servicerequest_changelist')
    return redirect('track_requests')
