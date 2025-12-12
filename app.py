from flask import Flask, request, render_template, redirect
from db import get_connection

app = Flask(__name__)

@app.route("/", methods=["GET"])        # トップページ候補
@app.route("/entries", methods=["GET"])
def account_list():
    conn = get_connection()
    cur = conn.cursor()

    sql = """
    SELECT id, date, type, account, summary, amount
    FROM entries
    ORDER BY date ASC, id ASC;
    """

    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()

    return render_template("entries/index.html", rows=rows)


@app.route("/entries/new", methods=["GET"])
def new_entry():
    return render_template("entries/new.html")


@app.route("/entries", methods=["POST"])
def create_entry():
    date = request.form.get("date")
    type_ = request.form.get("type")
    account = request.form.get("account")
    summary = request.form.get("summary", "")
    amount_str = request.form.get("amount")

    if not date or not type_ or not account or not amount_str:
        return "必須項目が未入力です", 400
    
    try:
        amount = int(amount_str)
    except ValueError:
        return "金額は整数で入力してください", 400
    
    conn = get_connection()
    cur = conn.cursor()

    sql = """
    INSERT INTO entries (date, type, account, summary, amount)
    VALUES (?, ?, ?, ?, ?);
    """

    params = (date, type_, account, summary, amount)
    cur.execute(sql, params)

    conn.commit()
    conn.close()

    return redirect("/entries")


if __name__ == "__main__":
    app.run(debug=True, port=8000)