from setuptools import find_packages, setup


setup(
    name='django-cms-scaffold',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',
    description='django-cms-scaffold',
    url='https://www.example.com/',
    author='Marcin Skiba',
    author_email='marcin@coding.buzz',
    classifiers=[
        'Framework :: Django :: X.Y',
    ],
    test_suite='tests',
    tests_require=[
        'mock'
    ]
)
