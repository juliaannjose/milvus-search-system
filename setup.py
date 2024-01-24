from setuptools import setup, find_packages

setup(
    name="milvus_search_system",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pyspark==3.3.1",
        "pymilvus==2.2.0",
        "sentence_transformers==2.2.2",
    ],
)
