from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.services.student_service import StudentService


student_bp = Blueprint("students", __name__, url_prefix="/students")


@student_bp.route("/", methods=["GET"])
def list_students():
    service = StudentService()
    search_term = request.args.get("q", "")

    try:
        students = service.search_students(search_term)
    except Exception:
        flash("Unable to load students. Please try again.", "error")
        students = []

    return render_template(
        "students/list.html",
        students=students,
        search_term=search_term,
    )


@student_bp.route("/new", methods=["GET", "POST"])
def create_student():
    if request.method == "POST":
        service = StudentService()

        try:
            service.register_student(
                request.form.get("first_name", ""),
                request.form.get("last_name", ""),
            )
            flash("Student registered successfully.", "success")
            return redirect(url_for("students.list_students"))

        except ValueError as error:
            flash(str(error), "error")

        except Exception:
            flash("Unable to register student. Please try again.", "error")

    return render_template("students/create.html")