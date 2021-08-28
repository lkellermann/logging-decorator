import setuptools

with open("README.md","r", encoding='utf-8') as f:
    long_description=f.read()
    
setuptools.setup(
    name="logging-decorator",
    version="1.0.1",
    author="Leandro Kellermann de Oliveira",
    author_email="kellermann@alumni.usp.br",
    description="A simple method decorator to generate logs easily.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lkellermann/logging-decorator",
    project_urls={
        "Status":"https://github.com/lkellermann/logging-decorator/blob/main",
        "Pull requests":"https://github.com/lkellermann/logging-decorator/pulls",
        "Issues":"https://github.com/lkellermann/logging-decorator/issues",
        "License":"https://github.com/lkellermann/logging-decorator/blob/main/license",
        
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6"
)
    