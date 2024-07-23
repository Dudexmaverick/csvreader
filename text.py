from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import CharacterTextSplitter

text =""
loader = CSVLoader(file_path="/home/mariaeduarda/chatlang/transcript_table(1).csv")
data = loader.load()
def process_files(loader):
    text = ""

    for loader  in process_files:
        csv = loader.load(loader)
        for csv  in :
            text += loader.extract_text()
    
    return text

def process_files(files):
    text = ""

    for file in files:
        pdf = PdfReader(file)
        for page in pdf.pages:
            text += page.extract_text()
    
    return text
def create_text_chunks(text):

    text_splitter = CharacterTextSplitter(
            separator='/n',
            chunk_size = 500,
            chunk_overlap = 100,
            length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

