from setuptools import setup, find_packages

__author__ = 'midhatstam@gmail.com'

try:
    long_description = open('README.md').read()
except IOError:
    long_description = ''

setup(
    name='yahoo-finance',
    use_scm_version=True,
    setup_requires=['setuptools_scm'],

    author='midhat',
    author_email='midhatstam@gmail.com',
    packages=find_packages(),
    url='',
    description='',
    long_description=long_description,
    include_package_data=True,
    keywords='',
    zip_safe=False,
    license='',
    platforms=['any'],
    install_requires=[
        'Django==3.2.5',
        'djangorestframework==3.12.4',
        'django-environ==0.4.5',
        'feedparser==6.0.8',
        'gunicorn==20.1.0',
        'django-filter==2.4.0',

        # tasks
        'celery==5.1.2',  # celery-task
        'django-celery-beat==2.2.1',
        'django-celery-results==2.2.0',

        # db
        'psycopg2-binary==2.9.1',
        'xmltodict==0.12.0',

        # other
        'django-safedelete==1.0.0',
        'drf-yasg==1.20.0',  # swagger

        # test
        'pytest-django==4.4.0',
        'tox==3.24.0',
        'pytest==6.2.4',
        'coverage==5.5',
    ]
)
