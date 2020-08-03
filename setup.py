from setuptools import setup, find_packages

setup(
    name='stockSharesAnalysis',
    version='0.1.0',
    packages=find_packages(),
    url='',
    license='Apache',
    author='Victor Valero',
    author_email='',
    description='Shares Analysis',

    install_requires = ['pandas>=0.24', 'numpy>=1.15',
                        'requests>=2.20', 'multitasking>=0.0.7'],

)
