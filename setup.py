"""
The build/compilations setup

>> pip install -r requirements.txt
>> python setup.py install
"""
import pip
import logging
import pkg_resources
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def _parse_requirements(file_path):
    pip_ver = pkg_resources.get_distribution('pip').version
    pip_version = list(map(int, pip_ver.split('.')[:2]))
    if pip_version >= [6, 0]:
        raw = pip.req.parse_requirements(file_path,
                                         session=pip.download.PipSession())
    else:
        raw = pip.req.parse_requirements(file_path)
    return [str(i.req) for i in raw]


# parse_requirements() returns generator of pip.req.InstallRequirement objects
try:
    install_reqs = _parse_requirements("requirements.txt")
except Exception:
    logging.warning('Fail load requirements file, so using default ones.')
    install_reqs = []

setup(
    name='DataExtractionModule',
    version='1.1',
    url='https://github.com/RaihanSabique/Data_Extraction',
    author='Raihan',
    author_email='1305116.mrm@ugrad.cse.buet.ac.bd',
    license='BABL',
    description='Extract metadata from different source file like docx,xml,pdf of DPP,RDPP,ADP,RADP,',
    packages=["dataExtraction","dataExtraction.filereader","dataExtraction.fontconvert","dataExtraction.objectclass","dataExtraction.rulesfile","dataExtraction.extractionstrategy","dataextraction.dppFile","dataextraction.font"],
    install_requires=install_reqs,
    include_package_data=True,
    python_requires='>=3.4',
    long_description="""This is an implementation of "Database Design for Capacity Enhancement of NEC-ECNEC & 
    ordination Wing by Introducing Digital Database and Archive System" a research project by Department of 
    Computer Science and Engineering, BUET..""",
    classifiers=[
        "Development Status :: End to end Production through JSON API",
        "Environment :: python 3.7",
        "Intended Audience :: Research and Development",
        "Intended Audience :: Department of CSE, BUET",
        "Intended Audience :: People's Republic of Bangladesh Government",
        "Intended Audience :: Bangladesh Planning Commission",
        "Intended Audience :: NEC-ECNEC & Co-ordination Wing",
        "License :: Business Accelerate BD Ltd",
        "Natural Language :: Bangla",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Metadata Extraction",
        "Topic :: Scientific/Engineering :: Deep Learning (LSTM)",
        "Topic :: Scientific/Engineering :: Pattern Recognization",
        "Topic :: Scientific/Engineering :: Data Mining",
        "Topic :: Scientific/Engineering :: Natural Language Processing",
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    keywords="Extract metadata from different source file like docx,xml,pdf of DPP,RDPP,ADP,RADP",
)
