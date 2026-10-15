from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    url_for,
)

from app.services.student_service import StudentService
import traceback

student_bp = Blueprint("students", __name__, url_prefix="/students")

#list
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

#create
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

#Edit
@student_bp.route("/<int:student_id>/edit", methods=["GET", "POST"])
def edit_student(student_id):
    service = StudentService()

    try:
        student = service.get_student(student_id)

        if student is None:
            flash("Student not found.", "error")
            return redirect(url_for("students.list_students"))

        if request.method == "POST":
            service.update_student(
                student_id,
                request.form.get("first_name", ""),
                request.form.get("last_name", ""),
            )

            flash("Student updated successfully.", "success")
            return redirect(url_for("students.list_students"))

    except ValueError as error:
        flash(str(error), "error")

    except Exception:
        flash("Unable to process student details. Please try again.", "error")
        return redirect(url_for("students.list_students"))

    return render_template(
        "students/edit.html",
        student=student,
    )

#deactivate
@student_bp.route( "/<int:student_id>/deactivate", methods=["POST"])
def deactivate_student(student_id): 
    service = StudentService() 
    try: 
        service.deactivate_student(student_id) 
        flash(
            "Student deactivated successfully.", 
            "success",
            ) 
    except ValueError as error: 
        flash(str(error), "error") 
    except Exception: 
        flash(
            "Unable to deactivate student. Please try again.", 
            "error",
            ) 
    return redirect(url_for("students.list_students"))

@student_bp.route("/<int:student_id>/activate", methods=["POST"])
def activate_student(student_id):
    service = StudentService()

    try:
        service.activate_student(student_id)
        flash("Student activated successfully.", "success")
    except ValueError as error:
        flash(str(error), "error")
    except Exception:
        traceback.print_exc()
        flash("An error occurred while activating the student.", "error")

    return redirect(url_for("students.list_students"))

