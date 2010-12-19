import os
import re
from django.core.management.base import NoArgsCommand
from django.conf import settings

default_clean_types = [
    r'^.+\.pyc$',
]

class Command(NoArgsCommand):
    requires_model_validation = False
    can_import_settings = True
    project_path = getattr(settings, 'PROJECT_PATH', None)
    clean_types = getattr(settings, 'CLEAN_TYPES', default_clean_types)
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        if not self.project_path:
            print "Please define PROJECT_PATH in your settings file."
            exit(1)
    
    def handle_noargs(self, **kwargs):
        print "Cleaning..."
        for dirname, dirnames, filenames in os.walk(self.project_path):
            for filename in filenames:
                # check against a regex to determine whether to delete file or not
                full_path = os.path.join(dirname, filename)
                for pattern in self.clean_types:
                    if re.search(pattern, full_path):
                        if os.path.isfile(full_path):
                            os.remove(full_path)
                        elif os.path.isdir(full_path):
                            os.rmdir(full_path)