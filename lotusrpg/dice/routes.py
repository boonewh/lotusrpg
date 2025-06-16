from flask import Blueprint, render_template, jsonify
import random


dice = Blueprint("dice", __name__, template_folder="templates")

@dice.route("/dice")
def dice_roller():
    return render_template("dice.html")


@dice.route("/api/roll/double10")
def roll_double10():
    total = 0
    rolls = []

    # --- First roll ---
    first_roll = [random.randint(1, 10), random.randint(1, 10)]
    rolls.append(first_roll.copy())
    total += sum(first_roll)

    if first_roll[0] == 10 and first_roll[1] == 10:
        # Double 10s: trigger explosion loop
        while True:
            new_roll = [random.randint(1, 10), random.randint(1, 10)]
            rolls.append(new_roll.copy())
            total += sum(new_roll)

            # Check if we keep exploding
            if 10 in new_roll:
                if new_roll[0] == 10 and new_roll[1] == 10:
                    continue  # both explode again
                elif new_roll[0] == 10 or new_roll[1] == 10:
                    # only one 10: reroll just that one
                    reroll = 0 if new_roll[0] == 10 else 1
                    while new_roll[reroll] == 10:
                        explode_roll = random.randint(1, 10)
                        rolls[-1][reroll] += explode_roll
                        total += explode_roll
                        if explode_roll != 10:
                            break
                    break
                else:
                    break
            else:
                break

    return jsonify({
        "total": total,
        "rolls": rolls
    })
