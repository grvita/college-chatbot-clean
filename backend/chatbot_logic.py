from database import get_connection

def find_response(message: str):
    conn = get_connection()
    cursor = conn.cursor()

    text = message.lower().strip()

    # Find matching FAQs by keywords or question text
    cursor.execute(
        """
        SELECT id, question, answer, category
        FROM faqs
        WHERE LOWER(keywords) LIKE ? OR LOWER(question) LIKE ?
        """,
        (f"%{text}%", f"%{text}%"),
    )
    results = cursor.fetchall()

    if not results:
        conn.close()
        return {
            "answer": "Sorry, I couldn't find an answer to that. Try asking about fees, timings, hostel, contact, or transport.",
            "suggestions": [
                "What are the B.Tech fees?",
                "What are the college timings?",
                "Do you have hostel facilities?",
                "What are the contact details?",
                "Is transport available?",
            ],
        }

    # First result = best match
    best = results[0]
    best_id = best["id"]
    best_category = best["category"]
    best_answer = f"<strong>{best['question']}</strong><br><br>{best['answer']}"

    # Collect other suggestions from same category
    suggestions = []
    if best_category:
        cursor.execute(
            """
            SELECT question
            FROM faqs
            WHERE category = ? AND id != ?
            LIMIT 3
            """,
            (best_category, best_id),
        )
        rows = cursor.fetchall()
        suggestions = [row["question"] for row in rows]

    conn.close()

    if not suggestions:
        suggestions = [
            "What are the B.Tech fees?",
            "What are the college timings?",
        ]

    return {
        "answer": best_answer,
        "suggestions": suggestions,
    }
