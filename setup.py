
import os
from setuptools import setup, find_packages

def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

setup(
    name="Data-Sharing-Site",
    version="0.1",
    author="AnuTech",
    author_email="casecarey@gmail.com",
    description="Sample project",
    long_description=(read('README')),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: GeoNode',
        'License :: OSI Approved :: BSD',
    ],
    license="BSD",
    keywords="geonode django",
    url='https://github.com/AnuTech/Data-Sharing-Site',
    scripts = [
               'scripts/Data-Sharing-Site',
              ],
    packages=find_packages('.'),
    include_package_data=True,
    zip_safe=False,
)
