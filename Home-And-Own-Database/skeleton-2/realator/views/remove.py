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
    
def removesale(conn, home_id):
    return execute(conn, f"DELETE FROM Sale WHERE home_id = '{home_id}'")


def removerent(conn, home_id):
    return execute(conn, f"DELETE FROM Rent WHERE home_id = '{home_id}'")


def views(bp):
    @bp.route("/remove/sale")
    def removesalepage():
        with get_db() as conn:
            rows = forsale(conn)
        return render_template("removesale.html", name="Remove Home For Sale", rows=rows)

    @bp.route("/remove/sale", methods=["POST", "GET"])
    def _removesale():
        if request.method == "POST":
            with get_db() as conn:
                home_id = request.form["home-id"]
                removesale(conn,home_id)
                return "SUCCESS"
        else:
            return "ERROR! PLEASE TRY AGAIN."
    
    @bp.route("/remove/rent")
    def removerentpage():
        with get_db() as conn:
            rows = forrent(conn)
        return render_template("removerent.html", name="Remove Home For Rent", rows=rows)

    @bp.route("/remove/rent", methods=["POST", "GET"])
    def _removerent():
        if request.method == "POST":
            with get_db() as conn:
                home_id = request.form["home-id"]
                removerent(conn,home_id)
                return "SUCCESS"
        else:
            return "ERROR! PLEASE TRY AGAIN."
                
   
    
