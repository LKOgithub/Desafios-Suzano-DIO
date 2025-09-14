from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Pacote de Processamento de Imagens com Python",
    version="0.0.1",
    author="Lucas_Oshiro",
    author_email="lucaskoshiro@gmail.com",
    description="Made this program for education issue",
    long_description=page_description,
    long_description_content_type="Programa feito para processamento de imagem simples de combinação",
    url="https://github.com/LKOgithub/Desafios-Suzano-DIO"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)