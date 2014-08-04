
from setuptools import setup


# Dynamically calculate the version based on pyganim.VERSION.
version = __import__('pygcurse').__version__


setup(
    name='Pygcurse',
    version=version,
    url='http://inventwithpython.com/pygcurse',
    author='Al Sweigart',
    author_email='al@inventwithpython.com',
    description=('A curses library emulator that runs on top of the Pygame framework, providing an easy way to create text adventures, rougelikes, and console-style applications.'),
    license='BSD',
    packages=['pygcurse'],
    test_suite='tests',
    keywords="pygame curses ncurses console text game 2D graphics",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Win32 (MS Windows)',
        'Environment :: X11 Applications',
        'Environment :: MacOS X',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)