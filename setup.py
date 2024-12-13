from setuptools import setup

setup(
    name="RAGMine",
    version="0.1.0",
    author="Saurabh Dubey",
    py_modules=["cli", "pipeline", "model_selector", "prompt_customizer", "api", "utils"],  # Explicitly mention the modules
    install_requires=[
        "langchain",
        "openai",
        "chromadb",
        "pymupdf",
        "fastapi",
        "uvicorn",
        "tqdm",
        "pandas",
        "llama-cpp-python",
        "requests",
        "pymongo[srv]",
    ],
    entry_points={
        "console_scripts": [
            "ragmine=cli:main",  # This points to the main function in cli.py
        ],
    },
    description="A prebuilt RAG pipeline framework for GenAI solutions",
)
