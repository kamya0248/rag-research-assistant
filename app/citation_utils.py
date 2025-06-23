
def generate_apa_citation(title, authors, date, pdf_link):
    # Format authors: "First A., Second B., & Third C."
    author_list = [name.strip() for name in authors.split(",")]
    if len(author_list) == 1:
        formatted_authors = author_list[0]
    elif len(author_list) == 2:
        formatted_authors = f"{author_list[0]} & {author_list[1]}"
    else:
        formatted_authors = ", ".join(author_list[:-1]) + f", & {author_list[-1]}"

    # Extract year only
    year = str(date)[:4] if date else "n.d."

    citation = f"{formatted_authors} ({year}). *{title}*. Retrieved from {pdf_link}"
    return citation
