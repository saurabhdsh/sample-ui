import os
import sys
import time
from colorama import Fore, Style, init
from tqdm import tqdm
from pipeline import RAGPipeline
from model_selector import ModelSelector
from utils import Utils
from prompt_customizer import PromptCustomizer  # Import PromptCustomizer

# Initialize colorama
init(autoreset=True)

def main():
    print(Fore.CYAN + Style.BRIGHT + "Welcome to the RAG Pipeline CLI!")
    print(Fore.CYAN + "=====================================")

    # Check for OpenAI API key
    try:
        Utils.check_openai_key()
        print(Fore.GREEN + "OpenAI API key found.")
    except EnvironmentError as e:
        print(Fore.RED + str(e))
        return

    # Initialize the RAG pipeline
    pipeline = RAGPipeline()

    # Prompt for document type
    print(Fore.YELLOW + "\nDocument Ingestion:")
    input_type = input(Fore.CYAN + "Do you want to ingest (1) PDF documents or (2) an external database? ")

    if input_type == "1":
        pdf_path = input(Fore.CYAN + "Enter the path to the PDF file: ")
        
        # Tiny animation for loading the PDF
        print(Fore.YELLOW + "Loading PDF file...")
        for _ in tqdm(range(10), desc="Processing", bar_format="{l_bar}{bar} [Elapsed: {elapsed}]"):
            time.sleep(0.1)
        pipeline.load_pdf(pdf_path)

        # Database selection
        db_choice = input(Fore.CYAN + "Select the database to store embeddings (1 for ChromaDB, 2 for MongoDB): ")
        if db_choice == "2":
            db_uri = input(Fore.CYAN + "Enter the MongoDB URI: ")
            db_name = input(Fore.CYAN + "Enter the MongoDB database name: ")
            pipeline.connect_to_db("mongodb", db_uri, db_name)
        else:
            print(Fore.GREEN + "Defaulting to ChromaDB...")
            pipeline.connect_to_db("chroma", db_uri=None)

    elif input_type == "2":
        db_type = input(Fore.CYAN + "Enter the database type (e.g., MongoDB, Chroma): ")
        db_uri = input(Fore.CYAN + "Enter the database URI: ")
        db_name = input(Fore.CYAN + "Enter the database name (for MongoDB): ") if db_type.lower() == "mongodb" else None
        pipeline.connect_to_db(db_type, db_uri, db_name)
    else:
        print(Fore.RED + "Invalid input type selected.")
        return

    # Model selection
    model_name = input(Fore.CYAN + "Select the model (OpenAI, Llama, etc.): ")
    pipeline.select_model(model_name)
    print(Fore.GREEN + f"Model '{model_name}' selected.")

    # Customize prompt using PromptCustomizer
    custom_prompt = input(Fore.CYAN + "Enter a custom prompt (optional): ")
    question = input(Fore.CYAN + "Enter a question to ask (optional): ")
    prompt_customizer = PromptCustomizer(base_prompt=custom_prompt or "Default prompt")
    prompt = prompt_customizer.customize_prompt(question=question)

    # Run the RAG process with a progress bar
    print(Fore.YELLOW + "\nRunning the RAG process...")
    for _ in tqdm(range(10), desc="Running", bar_format="{l_bar}{bar} [Elapsed: {elapsed}]"):
        time.sleep(0.1)
    pipeline.run(prompt)  # Only pass the customized prompt

    print(Fore.GREEN + "\nProcess completed successfully!")

if __name__ == "__main__":
    main()
