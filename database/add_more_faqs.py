from backend.database import get_connection

def add_more_faqs():
    conn = get_connection()
    cursor = conn.cursor()

    faqs = [
        # ==== Admissions ====
        (
            "admission, eligibility, 12th percentage, pcm",
            "What is the eligibility for B.Tech admission?",
            "For B.Tech admission, you must have passed 12th with PCM and a minimum of 60% aggregate.",
            "Admissions",
        ),
        (
            "admission process, how to apply, application form",
            "How can I apply for admission?",
            "You can apply online through the college admission portal and upload the required documents.",
            "Admissions",
        ),

        # ==== Exams ====
        (
            "exam, internal, semester, midterm",
            "How are internal exams conducted?",
            "Internal exams include assignments, quizzes, and mid-semester tests conducted during the semester.",
            "Exams",
        ),
        (
            "backlog, supplement, re-exam",
            "What happens if I get a backlog?",
            "If you get a backlog, you can clear it in the supplementary exam conducted by the university.",
            "Exams",
        ),

        # ==== Library ====
        (
            "library timing, library hours, books, reading hall",
            "What are the library timings?",
            "The library is usually open from morning till evening on all working days.",
            "Library",
        ),
        (
            "library card, membership, book issue",
            "How can I issue books from the library?",
            "You can use your student ID to get library membership and issue books as per the rules.",
            "Library",
        ),

        # ==== Placement ====
        (
            "placement, companies, package, highest salary",
            "What about placements at the college?",
            "Top IT and core companies visit campus for placements, with good average and highest packages.",
            "Placement",
        ),
        (
            "internship, training, industry exposure",
            "Does the college provide internships?",
            "The college helps students get internships through its training and placement cell.",
            "Placement",
        ),
    ]

    cursor.executemany(
        """
        INSERT INTO faqs (keywords, question, answer, category)
        VALUES (?, ?, ?, ?)
        """,
        faqs,
    )

    conn.commit()
    print(f"Inserted {cursor.rowcount} new FAQ rows.")
    count = cursor.execute("SELECT COUNT(*) FROM faqs").fetchone()[0]
    print("Total FAQs in database:", count)
    conn.close()

if __name__ == "__main__":
    add_more_faqs()
