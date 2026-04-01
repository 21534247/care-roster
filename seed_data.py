import sqlite3

conn = sqlite3.connect("careroster.db")
cursor = conn.cursor()

cursor.execute("""
INSERT INTO participants (full_name, phone, address, support_needs, emergency_contact)
VALUES
('John Smith', '0400000001', 'Perth WA', 'Personal care support', 'Jane Smith'),
('Amandeep Kaur', '0400000002', 'Cannington WA', 'Community access support', 'Harpreet Kaur'),
('Michael Brown', '0400000003', 'Victoria Park WA', 'Daily living assistance', 'Sarah Brown')
""")

conn.commit()
conn.close()

print("Sample participant data added successfully.")
