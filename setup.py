from setuptools import setup, find_packages

setup(
    name="learntools",
    version="0.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas",
        "numpy",
        "matplotlib",
        "seaborn",
        "scikit-learn",
    ],
)
