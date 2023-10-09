from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Event, EventDate, UserProfile, EventParticipant
from .forms import EventForm, UserProfileForm

@login_required
def home(request):
    if not request.session.get("first_access"):
        request.session["first_access"] = True
    
    try:
        if request.user.userprofile.display_name == None:
            return redirect('settings')
    except:
        return redirect('settings')

    # 自分が主催のイベントをデータベースから取得
    events = Event.objects.filter(event_organizer=request.user)

    return render(request, 'home.html', {'events': events})

@login_required
def settings(request):
    if not request.session.get("first_access"):
        return redirect("home")
    
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
        messages.success(request, 'Settings saved successfully. Your display_name is ' + request.POST.get('display_name'))
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'settings.html', {'form': form})
    
@login_required
def organizer(request):
    if not request.session.get("first_access"):
        return redirect("home")
    
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            # フォームから提供されたデータを使用してイベントを作成
            event = form.save(commit=False)
            event.event_organizer = request.user  # ログインユーザーを主催者として設定

            # イベントを一時保存し、IDを取得
            event.save()

            # カンマ区切りの日付文字列をリストに分割して処理
            event_date_list = request.POST.get('event_dates', '').split(',')  # カンマ区切りの日付文字列を分割してリストにする

            # 分割した日付をEventDateモデルに追加
            for date_str in event_date_list:
                date = EventDate(date=date_str.strip())  # スペースを削除して日付を作成
                date.save()
                event.event_dates.add(date)

            event.save()
            
            return redirect('published_event', event_code=event.event_code)
    else:
        form = EventForm()

    return render(request, 'organizer.html', {'form': form})

@login_required
def participant(request):
    if not request.session.get("first_access"):
        return redirect("home")
    
    if request.method == 'POST':
        event_code = request.POST.get('event_code')
        try:
            event = Event.objects.get(event_code=event_code)
            return redirect('published_event', event_code=event.event_code)
        except Event.DoesNotExist:
            error_message = 'Event with this code does not exist.'
            return render(request, 'participant.html', {'error_message': error_message})
    else:
        return render(request, 'participant.html')

@login_required
def published_event(request, event_code):
    if not request.session.get("first_access"):
        request.session["first_access"] = True

    event = get_object_or_404(Event, event_code=event_code)
    event_dates = event.event_dates.all()
    participant, created = EventParticipant.objects.get_or_create(user=request.user, event=event)

    if request.method == 'POST':
        availability_dates = request.POST.getlist('availability')
        participant.available_dates.set(availability_dates)
        participant.save()

    context = {
        'event': event,
        'event_dates': event_dates,
        'participant': participant, 
    }

    return render(request, 'published_event.html', context)