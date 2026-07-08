from app.services.rag import build_vector_database

count = build_vector_database()

print("=" * 50)
print(f"Vector database created successfully!")
print(f"Total chunks: {count}")
print("=" * 50)