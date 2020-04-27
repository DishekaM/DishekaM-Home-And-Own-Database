from collections import namedtuple

from flask import g
from flask import escape
from flask import render_template
from flask import request

from realator.db import get_db, execute
from realator.validate import validate_field, render_errors
from realator.validate import NAME_RE, INT_RE, DATE_RE



def add_homesale(conn, status, price, address, beds, baths, size, mortgage, agent_id):
    return execute(conn, f"INSERT INTO Sale(status, price, address, beds, baths, size, mortgage, agent_id) VALUES ('{status}', '{price}', '{address}', '{beds}', '{baths}', '{size}', '{mortgage}', '{agent_id}')")


def add_homerent(conn, status, rentprice, address, beds, baths, size, agent_id):
    return execute(conn, f"INSERT INTO Rent(status, rentprice, address, beds, baths, size, agent_id) VALUES ('{status}', '{rentprice}', '{address}', '{beds}', '{baths}', '{size}', '{agent_id}')")



def views(bp):
    @bp.route("/list/sale")
    def addlistsalepage():
        return render_template("listsale.html", name="List A Home For Sale")

    @bp.route("/list/sale", methods=["POST", "GET"])
    def _listsale():
        if request.method == "POST":
            with get_db() as conn:
                status = request.form["status"]
                price = request.form["price"]
                address = request.form["address"]
                beds = request.form["beds"]
                baths = request.form["baths"]
                size = request.form["size"]
                mortgage = request.form["mortgage"]
                agent_id = request.form["agent-id"]
                add_homesale(conn,status, price, address, beds, baths, size, mortgage, agent_id)
                
                return "SUCCESS"
        else:
            return "ERROR! PLEASE TRY AGAIN."
    
    @bp.route("/list/rent")
    def addlistrentpage():
        return render_template("listrent.html", name="List A Home For Rent")

    @bp.route("/list/rent", methods=["POST", "GET"])
    def _listrent():
        if request.method == "POST":
            with get_db() as conn:
                status = request.form["status"]
                rentprice = request.form["rentprice"]
                address = request.form["address"]
                beds = request.form["beds"]
                baths = request.form["baths"]
                size = request.form["size"]
                agent_id = request.form["agent-id"]
                add_homerent(conn,status, rentprice, address, beds, baths, size, agent_id)
                
                return "SUCCESS"
        else:
            return "ERROR! PLEASE TRY AGAIN."
    
