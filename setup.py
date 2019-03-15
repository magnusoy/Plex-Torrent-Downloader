from setuptools import find_packages, setup

setup(
    name='plex-torrent-server',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask',
        'Flask-Mail',
        'flask-marshmallow',
        'Flask-WTF',
        'Flask-SQLAlchemy',
        'marshmallow-sqlalchemy',
       ' PyJWT'
    ],
)