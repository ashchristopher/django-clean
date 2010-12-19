import os
import re
from optparse import make_option    # in the future, use argparse
from django.core.management.base import BaseCommand
from django.conf import settings



default_clean_types = [
    r'^.+\.pyc$',
]


class Command(BaseCommand):
    requires_model_validation = False
    can_import_settings = True
    help = "Cleans up files and directories in a Django project which match given regular expressions."
    
    
    project_path = getattr(settings, 'PROJECT_PATH', None)
    clean_types = getattr(settings, 'CLEAN_TYPES', default_clean_types)
    
    option_list = BaseCommand.option_list  + (
        make_option('-f', '--force', action="store_true", default=False, dest='force', help='Force the cleanup without user interaction.'),
    )
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        if not self.project_path:
            print "Please define PROJECT_PATH in your settings file."
            exit(1)
    
    def handle(self, force, **kwargs):
        print "Cleaning..."
        for dirname, dirnames, filenames in os.walk(self.project_path):
            for filename in filenames:
                # check against a regex to determine whether to delete file or not
                full_path = os.path.join(dirname, filename)
                for pattern in self.clean_types:
                    if re.search(pattern, full_path):
                        if force:
                            self.remove_asset(full_path)
                        else:
                            confirm_action = raw_input("Do you want to delete '%s'? [y/N]  " % full_path)
                            if confirm_action == 'y':
                                self.remove_asset(full_path)    

    def remove_asset(self, asset):
        if os.path.isfile(asset):
            os.remove(asset)
        elif os.path.isdir(asset):
            os.rmdir(asset)
        