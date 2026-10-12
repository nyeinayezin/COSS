import pytest
from app.domain.student import Student
from app.domain.class_group import ClassGroup
from app.services.enrolment_service import EnrolmentService


def test_student_can_enrol_in_class():
    student = Student(1, "John", "Smith")

    math_class = ClassGroup(
        class_id=101,
        name="Year 7 Mathematics",
        capacity=2
    )

    service = EnrolmentService()

    enrolment = service.enrol_student(student, math_class)

    assert enrolment.is_active()
    assert math_class.current_students == 1


def test_student_cannot_enrol_twice_in_same_class():
    student = Student(2, "Mary", "Jones")

    math_class = ClassGroup(
        class_id=102,
        name="Year 7 Mathematics",
        capacity=2
    )

    service = EnrolmentService()

    service.enrol_student(student, math_class)

    with pytest.raises(
        ValueError,
        match="Student is already enrolled in this class"
    ):
        service.enrol_student(student, math_class)


def test_student_cannot_enrol_when_class_is_full():
    student1 = Student(3, "Alex", "Brown")
    student2 = Student(4, "Sam", "Green")

    small_class = ClassGroup(
        class_id=103,
        name="Small Mathematics Class",
        capacity=1
    )

    service = EnrolmentService()

    service.enrol_student(student1, small_class)

    with pytest.raises(ValueError, match="Class is full"):
        service.enrol_student(student2, small_class)

    assert small_class.current_students == 1


def test_cancelling_enrolment_frees_class_place():
    student = Student(5, "Taylor", "Lee")

    small_class = ClassGroup(
        class_id=104,
        name="Small Mathematics Class",
        capacity=1
    )

    service = EnrolmentService()

    enrolment = service.enrol_student(student, small_class)

    service.cancel_enrolment(enrolment)

    assert not enrolment.is_active()
    assert small_class.current_students == 0