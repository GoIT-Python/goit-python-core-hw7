from setuptools import setup, find_namespace_packages

setup(
    name="clean_folder",
    version="1",
    description="Very useful code",
    url="https://github.com/GoIT-Python/goit-python-core-hw7",
    author="Volodymyr Kurov",
    author_email="mail@mail.com",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["parse", "normalize"],
    entry_points={"console_scripts": ["clean-folder = clean_folder.clean:sort"]},
)
