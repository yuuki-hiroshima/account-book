from db import get_connection

def show_all_entries():

    # 1. DBに接続
    conn = get_connection()
    cur = conn.cursor()

    # 2. SQL文（SELECT）を準備
    sql = """
    SELECT id, date, type, account, summary, amount
    FROM entries
    ORDER BY date ASC, id ASC;
    """

    # 3. SQLを実行
    cur.execute(sql)

    # 4. 結果を1行ずつ取り出して表示
    rows = cur.fetchall()

    print("=== entries テーブルの中身 ===")
    if not rows:
        print("(データがありません)")
    else:
        for row in rows:
            print(
                f"id={row['id']}, "
                f"date={row['date']}, "
                f"type={row['type']}, "
                f"account={row['account']}, "
                f"summary={row['summary']}, "
                f"amount={row['amount']}"
            )

    # 5. 接続を閉じる
    conn.close()

if __name__ == "__main__":
    show_all_entries()