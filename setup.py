from setuptools import setup

setup(
    name="main",
    version='0.1',
    py_modules=['main', 'db_wrangler', 'tSheet'],
    install_requires=[
        'Click',
        'psycopg2'
    ],
    entry_points='''
    [console_scripts]
    main=main:cli
    ''',
)
