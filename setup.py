from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="psychometric-career-intelligence",
    version="1.0.0",
    author="Psychometric.fyi",
    author_email="info@psychometric.fyi",
    description="Psychometric Career Intelligence is an educational resource exploring the science of psychometric assessments and career decision making.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://psychometric.fyi",
    project_urls={
        "Homepage": "https://psychometric.fyi",
        "GitHub": "https://github.com/Psychometric-fyi/Psychometric-career-intelligence",
        "Documentation": "https://psychometric-career-intelligence.readthedocs.io",
        "PyPI": "https://pypi.org/project/psychometric-career-intelligence",
    },
    py_modules=["career_intel"],
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Education",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords=[
        "psychometric-assessment",
        "career-intelligence",
        "personality-test",
        "cognitive-ability",
        "career-guidance",
        "strength-discovery",
        "psychometric-fyi",
    ],
    entry_points={
        "console_scripts": [
            "psychometric-career=career_intel:main",
        ],
    },
)
