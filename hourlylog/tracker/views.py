from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import DayLog, HourLog
from datetime import date as dt_date


from django.contrib.auth.forms import UserCreationForm

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def log_view(request):
    date_str = request.GET.get('date', dt_date.today().isoformat())
    date_obj = dt_date.fromisoformat(date_str)

    day_log, created = DayLog.objects.get_or_create(user=request.user, date=date_obj)

    if request.method == 'POST':
        for hour in range(24):
            content = request.POST.get(f'hour_{hour}', '')
            HourLog.objects.update_or_create(
                day=day_log,
                hour=hour,
                defaults={'content': content}
            )
        return redirect(f'?date={date_str}')

    logs = {log.hour: log.content for log in day_log.logs.all()}
    return render(request, 'log.html', {'date': date_str, 'logs': logs})
