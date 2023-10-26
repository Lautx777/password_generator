from setuptools import setup, find_packages

setup(
    name="password_generator",
    version="0.1",
    description="A simple encrypted password generator.",
    author="Lautx777",
    author_email="lpoggi2003@gmail.com",
    packages=find_packages(),
    package_dir={},
    install_requires=[
        "cryptography==3.4.7"    
    ],
    entry_points={
        'console_scripts': [
            'generator = password_generator.generator:main',
            'decrypt = password_generator.decrypt:main',    
        ],
    },
)