from app.rag import ask_question


print("AI Document Search")
print("Type 'exit' to stop.\n")


while True:
    query = input('You: ')

    if query.lower() == 'exit':
        print('Goodbye!')
        break

    answer,source = ask_question(query)

    print('\nGemini:')
    print(answer)
    print(f"\nSource: {source}.pdf")
    print()