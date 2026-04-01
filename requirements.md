# Requirements Document

## Functional Requirements
1. The system must allow admin users to log in securely.
2. The system must allow admin to add, edit, and delete participant records.
3. The system must allow admin to add, edit, and delete support worker profiles.
4. The system must allow admin to create shifts with date, time, and location.
5. The system must allow admin to assign support workers to participants.
6. The system must prevent double booking of support workers.
7. The system must allow support workers to update shift status.
8. The system must allow support workers to add case notes after shift completion.
9. The system must generate reports for upcoming and completed shifts.

## Non-Functional Requirements
1. The system should be easy to use.
2. The system should load pages within 3 seconds.
3. The system should protect user login credentials.
4. The system should maintain participant data privacy.
5. The system should be accessible on desktop and mobile browsers.

## Business Rules
- A support worker cannot be assigned to two shifts at the same time.
- A shift must always belong to one participant.
- A shift must be assigned before it can be marked as active.
- Case notes can only be added after shift completion.
