from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request
from realator.db import get_db, execute
from realator.validate import validate_field, render_errors
from realator.validate import NAME_RE, INT_RE, DATE_RE


def forrent(conn):
    return execute(conn, "SELECT * FROM Rent")

def lowtohigh(conn):
    return execute(conn, "SELECT * FROM Rent ORDER BY rentprice" )

def hightolow(conn):
    return execute(conn, "SELECT * FROM Rent ORDER BY rentprice DESC" )

def rentstatus(conn, home_id, status):
    return execute(conn, f"UPDATE Rent SET status='{status}' WHERE home_id='{home_id}'")


def views(bp):
    @bp.route("/rent")
    def _rent():
        with get_db() as conn:
            rows = forrent(conn)
        return render_template("table2.html", name="Homes For Rent", rows=rows)

    @bp.route("/rentsort")
    def _rentsort():
        with get_db() as conn:
            rows = lowtohigh(conn)
        return render_template("table2.html", name="Sorted Prices Low to High (For Rent)", rows=rows)
    
    @bp.route("/rentsort2")
    def _rentsort2():
        with get_db() as conn:
            rows = hightolow(conn)
        return render_template("table2.html", name="Sorted Prices High to Low (For Rent)", rows=rows)
    
    
 

