from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='flask_container',
    version='1.0.5',
    packages=find_packages(),
    include_package_data=True,
    license='MIT',  # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    author='Jose Roberts',  # Type in your name
    author_email='Jose.Roberts@intracitygeeks.org',  # Type in your E-Mail
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoseRoberts87/flask_container",
    zip_safe=False,
    python_requires='>=3.6',
    install_requires=[
        'flask',
        'Flask-RESTful==0.3.7',
        'flask-swagger-ui==3.20.9'
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
