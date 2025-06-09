from flask import Blueprint, render_template

dice = Blueprint("dice", __name__, template_folder="templates")

@dice.route("/dice")
def dice_roller():
    return render_template("dice.html")