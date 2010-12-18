try: 
    from setuptools import setup 
except ImportError: 
  from distutils.core import setup

    
setup(
    name = 'django-clean',
    version=__import__('clean').__version__,
    description = 'Clean out files in a django app.',
    author = 'Ash Christopher',
    author_email = 'ash.christopher@gmail.com',
    url = 'http://github.com/ashchristopher/django-clean',
    download_url='http://github.com/ashchristopher/django-clean',
    license='MIT',
    include_package_data=True,
    zip_safe=True, # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Django License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)