# utils.py

import os
import re
import fitz  # pymupdf
from pymongo import MongoClient

class Utils:
    @staticmethod
    def check_openai_key():
        """
        Checks if the OPENAI_API_KEY environment variable is set.
        """
        if not os.getenv("OPENAI_API_KEY"):
            raise EnvironmentError("Please set the OPENAI_API_KEY environment variable.")
    
    @staticmethod
    def read_pdf(file_path):
        """
        Extracts text from a PDF file using PyMuPDF (fitz).
        """
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text

    @staticmethod
    def connect_mongo(db_uri, db_name):
        """
        Connects to MongoDB using the provided URI and database name.
        """
        try:
            client = MongoClient(db_uri)
            db = client[db_name]
            return db
        except Exception as e:
            raise ConnectionError(f"Could not connect to MongoDB: {e}")

    @staticmethod
    def get_vector_database_connection(db_uri):
        """
        Placeholder method for connecting to vector databases like ChromaDB.
        """
        # This can be extended to return a vector DB connection
        # Code for initializing ChromaDB or another vector DB goes here
        return None

    @staticmethod
    def clean_text(text):
        """
        Cleans the input text by removing non-alphanumeric characters except spaces.
        Ensures the input is a string.
        """
        if not isinstance(text, str):
            raise TypeError(f"Expected a string, got {type(text)}")
        return re.sub(r'[^a-zA-Z0-9\s]', '', text)
