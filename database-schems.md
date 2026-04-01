# Database Schema

## 👤 Users Table
- user_id (Primary Key)
- full_name
- email
- password
- role

---

## 🧑‍🦽 Participants Table
- participant_id (Primary Key)
- full_name
- phone
- address
- support_needs
- emergency_contact

---

## 👷 Support Workers Table
- worker_id (Primary Key)
- full_name
- phone
- email
- availability
- qualification_status

---

## 📅 Shifts Table
- shift_id (Primary Key)
- participant_id (Foreign Key)
- worker_id (Foreign Key)
- shift_date
- start_time
- end_time
- location
- status

---

## 📝 Case Notes Table
- note_id (Primary Key)
- shift_id (Foreign Key)
- participant_id (Foreign Key)
- worker_id (Foreign Key)
- note_text
- created_at
