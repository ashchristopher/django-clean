from django.core.management.base import NoArgsCommand
from django.conf import settings

from commands import getstatusoutput

class Command(NoArgsCommand):
    requires_model_validation = False
    can_import_settings = True
    
    def handle_noargs(self, **kwargs):
        cmd = 'find %s/ -name "*.pyc" -exec rm {} \;' %(settings.PROJECT_PATH)
        print cmd
        (status, output) = getstatusoutput(cmd)
        if not status == 0:
            import sys
            sys.stderr.write("%s\n" %(output))
