from app.rag import ask_question


def main():
    print("AI Document Search")
    print("Type 'exit' to stop.\n")

    while True:
        query = input("You: ")

        if query.lower() == "exit":
            print("Goodbye!")
            break

        answer, sources = ask_question(query)

        print("\nGemini:")
        print(answer)
        if sources:
            print('\nSources:')
            for source in sources:
                print(f'{source}.pdf')
        print()


if __name__ == "__main__":
    main()