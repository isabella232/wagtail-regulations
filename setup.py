from setuptools import find_packages, setup


install_requires = [
    'python-dateutil>=2.8.0',
    'regdown==1.0.2',
    'wagtail>=2.0,<2.9',
    'wagtail-treemodeladmin>=1.1.0',
    'wagtail-copyablemodeladmin>=1.0.0',
]

testing_extras = [
    'coverage>=3.7.0',
    'mock>=2.0.0',
    'model_mommy>=1.6.0',
]

setup(
    name='wagtail-regulations',
    url='https://github.com/cfpb/wagtail-regulations',
    author='CFPB',
    author_email='tech@cfpb.gov',
    description='Building blocks for interactive regulations in Wagtail',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    license='CC0',
    version='1.1.0',
    include_package_data=True,
    packages=find_packages(),
    install_requires=install_requires,
    extras_require={
        'testing': testing_extras,
    },
    classifiers=[
        'Framework :: Django',
        'Framework :: Django :: 2',
        'Framework :: Wagtail',
        'Framework :: Wagtail :: 2',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'License :: Public Domain',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ]
)
