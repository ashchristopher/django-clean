from setuptools import setup, find_packages

    
setup(
    name='django-clean',
    version=__import__('clean').__version__,
    description='Clean out files in a django app using regular expressions.',
    long_description=open('README').read(),
    author='Ash Christopher',
    author_email='ash.christopher@gmail.com',
    url='http://github.com/ashchristopher/django-clean',
    download_url='http://github.com/ashchristopher/django-clean/downloads',
    license='BSD',
    include_package_data=True,
    zip_safe=True, # because we're including media that Django needs
    keywords='django clean temporary cleanup pyc',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
        ]
    
)