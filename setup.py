from setuptools import setup

setup(
    name='dict-to-protobuf',
    description='A teeny Python library for creating protobuf dicts from '
        'python dict. Useful when need to put dict on socket transmission.' 
        'You can not directly json a protobuf message object, it\'s not hashable'
        ,
    version='0.0.1',
    author='davy zhang',
    author_email='davyzhang@gmail.com',
    url='https://github.com/davyzhang/dict-to-protobuf',
    license='Public Domain',
    keywords=['protobuf', 'dict'],
    install_requires=['protobuf>=2.3.0'],
    package_dir={'':'src'},
    py_modules=['dict-to-protobuf'],
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
