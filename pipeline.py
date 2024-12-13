from langchain.schema import Document
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings  # Updated import as per deprecation
from utils import Utils
from model_selector import ModelSelector
from prompt_customizer import PromptCustomizer

class RAGPipeline:
    def __init__(self):
        self.documents = []
        self.vector_store = None
        self.mongo_db = None
        self.model = None  # Will hold the selected model
        self.prompt_customizer = PromptCustomizer("Please analyze the medical report and summarize relevant details.")
        
    def load_pdf(self, pdf_path):
        """
        Loads a PDF, reads its content, and appends it to the documents list.
        """
        print(f"Loading PDF from {pdf_path}...")
        text = Utils.read_pdf(pdf_path)
        document = Document(page_content=text)
        self.documents.append(document)

    def connect_to_db(self, db_type, db_uri=None, db_name=None):
        """
        Connects to either a vector database or MongoDB based on db_type.
        """
        print(f"Connecting to {db_type} database...")
        
        if db_type.lower() == "chroma":
            embeddings = OpenAIEmbeddings()
            self.vector_store = Chroma.from_documents(self.documents, embeddings)
            print("Connected to Chroma vector database.")
        
        elif db_type.lower() == "mongodb" and db_name:
            self.mongo_db = Utils.connect_mongo(db_uri, db_name)
            print(f"Connected to MongoDB database '{db_name}'.")
        
        else:
            raise ValueError(f"Unsupported database type or missing database name for MongoDB: {db_type}")

    def set_prompt(self, prompt=None):
        """
        Sets a custom prompt using the PromptCustomizer or defaults to the existing one.
        """
        self.prompt_customizer.set_base_prompt(prompt or self.prompt_customizer.base_prompt)

    def select_model(self, model_type="openai"):
        """
        Selects the model based on the input.
        """
        self.model = ModelSelector.select(model_type)
        print(f"Selected model: {model_type}")

    def run(self, query, additional_info=None, context=None):
        """
        Processes the query and retrieves answers from the selected model.
        """
        if not isinstance(query, str):
            raise ValueError(f"Query should be a string, got {type(query)}")

        if not self.vector_store:
            print("No vector store connected.")
            return

        # Clean the query before processing
        query = Utils.clean_text(query)  # Ensure it's a clean string

        # Retrieve similar documents
        results = self.vector_store.similarity_search(query)

        if not results:
            print("No relevant documents found.")
            return

        # Combine results into a single context for model analysis
        combined_content = "\n\n".join([doc.page_content for doc in results])

        # Generate a customized prompt with context and additional information
        full_context = self.prompt_customizer.customize_prompt(
            additional_info=additional_info,
            context=combined_content,
            question=query
        )

        # Generate response using the selected model
        if self.model:
            answer = self.model.generate_response(full_context)
            if answer:
                print("Answer to the query:", answer)
            else:
                print("No answer generated.")
        else:
            print("Model not selected.")
