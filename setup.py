from setuptools import setup

with open('README.md', encoding='utf8') as f:
    long_description = f.read()

setup(
    name='powerline-travis-ci',
    description='A Powerline segment for fetching and showing the latest travis-ci build state',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.post1',
    keywords='powerline travis-ci travis ci build state status segment terminal cli',
    license='MIT',
    author='DeepSpace2',
    author_email='deepspace2@gmail.com',
    url='https://github.com/DeepSpace2/powerline-travis-ci',
    packages=['powerline_travis_ci'],
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Terminals'
    ]
)
