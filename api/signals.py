from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import Event
import requests
import environ
from pathlib import Path
import os

env = environ.Env(
    BOT_TOKEN=(str, ''),
    URL_TELEGRAM=(str, ''),
    CHAT_ID=(str, ''),
)

BASE_DIR = Path(__file__).resolve().parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

BOT_TOKEN = env('BOT_TOKEN')
URL_TELEGRAM=env('URL_TELEGRAM')
# URL_MESSAGE = f'{URL_TELEGRAM}/bot{BOT_TOKEN}/sendMessage'
URL_PHOTO = f'{URL_TELEGRAM}/bot{BOT_TOKEN}/sendPhoto'
URL_VIDEO = f'{URL_TELEGRAM}/bot{BOT_TOKEN}/sendVideo'
URL_EDIT_MESSAGE_CAPTION = f'{URL_TELEGRAM}/bot{BOT_TOKEN}/editMessageCaption'
CHAT_ID = int(env('CHAT_ID'))

separator = '\n...\n'

def create_msg_from_instance(instance):
    msg = ''
    if (instance.title):
        msg += instance.title
    msg += f'{separator}{instance.caption}' if msg else instance.caption
    msg += separator
    [_, month, day] = instance.date.__str__().split('-')
    time = instance.time.__str__()[:5]
    msg += f'Когда: {day}.{month} / {time}\n'
    msg += f'Где: {instance.address}\n'
    msg += f'Вход: {instance.price}'
    if (instance.tags):
        msg += separator
        msg += instance.tags

    return msg

def create_event_data(instance):
    current_url = ''
    data = {}

    if bool(instance.video):
        video = instance.video.read()
        current_url = URL_VIDEO
        data['video'] = video
    elif bool(instance.photo):
        photo = instance.photo.read()
        current_url = URL_PHOTO
        data['photo'] = photo
    else:
        return

    msg = create_msg_from_instance(instance)
    params = {'chat_id': CHAT_ID, 'caption': msg}
    return [data, params, current_url]

is_saved = False

def send_event_to_telegram(instance):
    global is_saved
    is_saved = True
    [data, params, current_url] = create_event_data(instance)
    response = requests.post(current_url, params, files=data)
    print('send_event_to_telegram', response.text)
    response_json = response.json()
    result = response_json.get('result')

    message_id = result['message_id']
    instance.message_id = message_id
    instance.save()

def update_telegram_event(instance):
    global is_saved

    if is_saved:
        is_saved = False
        return

    msg = create_msg_from_instance(instance)
    params = {'chat_id': CHAT_ID, 'message_id': instance.message_id, 'caption': msg}
    response = requests.post(URL_EDIT_MESSAGE_CAPTION, params)
    print('update_telegram_event', response.text)

@receiver(post_save, sender=Event)
def event_added(sender, instance, **kwargs):
    if instance.message_id == 0:
        send_event_to_telegram(instance)
    else:
        update_telegram_event(instance)