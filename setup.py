from distutils.core import setup

setup(
    name='mycroft-chatter',
    version='0.0.2',
    packages=['lib', 'client', 'client.ui', 'client.ui.generated'],
    url='',
    license='GPL3',
    author='Chris Rogers',
    author_email='ChristopherRogers1991@gmail.com',
    description='Provides a chat like interface for Mycroft'
)
