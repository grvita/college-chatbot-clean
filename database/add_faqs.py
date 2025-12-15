from backend.database import get_connection

def add_sample_faqs():
    conn = get_connection()
    cursor = conn.cursor()
    
    faqs = [
        ("btech fees, b.tech fees, tuition, fee structure", 
         "What are the B.Tech fees?", 
         "B.Tech fees for 2025-26: ₹1,25,000 per year (first year) + ₹1,00,000 per year (subsequent years). Includes tuition, library, and lab fees. Additional: exam fees ₹5,000/semester, hostel ₹60,000/year.",
         "Fees"),
        
        ("college timings, working hours, college time, schedule", 
         "What are the college timings?", 
         "College timings: 9:00 AM - 5:00 PM (Monday-Saturday). Labs: 9:30 AM - 4:30 PM. Library: 8:00 AM - 6:00 PM. Admin office: 10:00 AM - 4:00 PM.",
         "Timings"),
        
        ("hostel facility, hostel fees, hostel room, accommodation", 
         "Do you have hostel facilities?", 
         "Yes! Separate hostels for boys & girls. Triple-sharing rooms: ₹60,000/year (includes mess). Double-sharing: ₹75,000/year. 500+ capacity each. WiFi, laundry, 24/7 security, gym, and mess available.",
         "Hostel"),
        
        ("contact details, phone number, email, address, contact", 
         "What are the contact details?", 
         "📞 Phone: +91-9876543210 (Admission), +91-9876543211 (Admin)\n📧 Email: admission@mit.edu.in, principal@mit.edu.in\n📍 Address: MIT Campus, Tech Park Road, Bangalore - 560001\n🌐 Website: www.mit.edu.in",
         "Contact"),
        
        ("transport, bus facility, college bus, shuttle service", 
         "Is transport available?", 
         "Yes! 25 AC buses cover Bangalore city areas. Routes: Majestic, Silk Board, Electronic City, Whitefield, Hebbal. Bus pass: ₹25,000/year. Free shuttle within 5km campus radius.",
         "Transport")
    ]
    
    cursor.executemany("""
        INSERT OR IGNORE INTO faqs (keywords, question, answer, category)
        VALUES (?, ?, ?, ?)
    """, faqs)
    
    conn.commit()
    conn.close()
    print("Sample FAQs added successfully!")

if __name__ == "__main__":
    add_sample_faqs()
