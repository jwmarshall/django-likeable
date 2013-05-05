#
# django-likeable
#
# See LICENSE for licensing details.
#

from setuptools import setup, find_packages


setup(
    name='django-likeable',
    version='0.0.3',
    description='Simple Django app to facilitate "liking" of any content type.',
    long_description=open('README.rst', 'rt').read(),
    author='Jonathon Marshall, originally forked from Thane Thomson\'s django-likeable',
    author_email='jwm@fishingfury.com',
    license='Apache',
    url='https://github.com/jwmarshall/django-likeable',
    packages=find_packages(),
    include_package_data=True,
    classifiers = [
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    zip_safe=False,
)

