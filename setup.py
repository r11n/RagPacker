from distutils.core import setup
setup(
    name='RagPacker',
    packages=['ragpacker'],
    version='0.0.1',
    license='MIT',
    description='A readymade solution for integrating webpack into django based applications.',
    author='r11n',
    author_email='nekkanti.raghavendra2@gmail.com',
    url='https://github.com/r11n/ragpacker',
    download_url='https://github.com/r11n/ragpacker/archive/0.0.1.tar.gz',
    keywords=['webpack', 'django-webpack'],
    # TODO: add install requires
    requires=['pyyaml']
    # TODO: add classifiers
)