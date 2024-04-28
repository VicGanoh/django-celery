from celery import shared_task
import sys
from django.core.management import call_command

@shared_task
def bkup():
    sys.stdout = open("db.json", "w")
    call_command("dumpdata", "app3")