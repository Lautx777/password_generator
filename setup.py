from setuptools import setup, find_packages

setup(
    name="password_generator",
    version="0.1",
    description="Una descripción breve de tu proyecto",
    author="Tu Nombre",
    author_email="tu@email.com",
    packages=find_packages(),
    install_requires=[
        "cryptography==3.4.7"
    ],
    entry_points={
        'console_scripts': [
            'generator = password_generator.generator:main'
        ],
    },
)
