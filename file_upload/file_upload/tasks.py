from time import sleep

from celery import shared_task

from fileapp.models import File


@shared_task
def load_file(file_id: int):
    print('Celery task load_file started, file_id: ', file_id)
    files_all = File.objects.values()
    file = File.objects.get(id=file_id)
    file.processed = True
    file.save()
    # sleep(10)  # sleep for demo purposes as if hard work is done
    print('Celery task load_file completed, database updated', files_all)
