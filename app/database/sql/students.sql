-- name: insert_student
INSERT INTO students (first_name, last_name, status)
VALUES (?, ?, ?);

-- name: get_student_by_id
SELECT student_id, first_name, last_name, status
FROM students
WHERE student_id = ?;

-- name: get_all_students
SELECT student_id, first_name, last_name, status
FROM students
ORDER BY student_id ASC;

-- name: search_students
SELECT student_id, first_name, last_name, status
FROM students
WHERE first_name LIKE ?
   OR last_name LIKE ?
ORDER BY student_id ASC;

-- name: update_student
UPDATE students
SET first_name = ?,
    last_name = ?,
    status = ?
WHERE student_id = ?;

-- name: deactivate_student
UPDATE students
SET status = 'INACTIVE'
WHERE student_id = ?;

-- name: activate_student
UPDATE students
SET status = 'ACTIVE'
WHERE student_id = ?