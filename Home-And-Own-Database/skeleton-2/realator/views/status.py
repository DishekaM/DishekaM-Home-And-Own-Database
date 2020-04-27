from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from realator.db import get_db, execute
from realator.validate import validate_field, render_errors
from realator.validate import NAME_RE, INT_RE, DATE_RE


def forsale(conn):
    return execute(conn, "SELECT * FROM Sale")

def forrent(conn):
    return execute(conn, "SELECT * FROM Rent")

def salestatus(conn, home_id, status):
    return execute(conn, f"UPDATE Sale SET status='{status}' WHERE home_id='{home_id}'")

def rentstatus(conn, home_id, status):
    return execute(conn, f"UPDATE Rent SET status='{status}' WHERE home_id='{home_id}'")



def views(bp):
    @bp.route("/sale/status")
    def salestatuspage():
        with get_db() as conn:
            rows = forsale(conn)
        return render_template("salestatus.html", name="Change Status (For Sale)", rows=rows)

    @bp.route("/sale/status", methods=["POST", "GET"])
    def _salestatus():
        if request.method == "POST":
            with get_db() as conn:
                home_id = request.form["home-id"]
                status = request.form["status"]
                salestatus(conn,home_id, status)
                return "SUCCESS"
        else:
            return "ERROR! PLEASE TRY AGAIN."
    
    @bp.route("/rent/status")
    def rentstatuspage():
        with get_db() as conn:
            rows = forrent(conn)
        return render_template("rentstatus.html", name="Change Status (For Rent)", rows=rows)

    @bp.route("/rent/status", methods=["POST", "GET"])
    def _rentstatus():
        if request.method == "POST":
            with get_db() as conn:
                home_id = request.form["home-id"]
                status = request.form["status"]
                rentstatus(conn,home_id, status)
                return "SUCCESS"
        else:
            return "ERROR! PLEASE TRY AGAIN."
                