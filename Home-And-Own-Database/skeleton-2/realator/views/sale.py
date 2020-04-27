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

def lowtohigh(conn):
    return execute(conn, "SELECT * FROM Sale ORDER BY mortgage" )

def hightolow(conn):
    return execute(conn, "SELECT * FROM Sale ORDER BY mortgage DESC" )

def salestatus(conn, home_id, status):
    return execute(conn, f"UPDATE Sale SET status='{status}' WHERE home_id='{home_id}'")


def views(bp):
    @bp.route("/sale")
    def _sale():
        with get_db() as conn:
            rows = forsale(conn)
        return render_template("table1.html", name="Homes For Sale", rows=rows)

    @bp.route("/salesort")
    def _salesort():
        with get_db() as conn:
            rows = lowtohigh(conn)
        return render_template("table1.html", name="Sorted Prices Low to High (For Sale)", rows=rows)

    @bp.route("/salesort2")
    def _salesort2():
        with get_db() as conn:
            rows = hightolow(conn)
        return render_template("table1.html", name="Sorted Prices High to Low (For Sale)", rows=rows)
    
    


        