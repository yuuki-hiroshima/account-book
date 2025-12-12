from db import get_connection

def insert_test_record():

    # 1. DBに接続
    conn = get_connection()
    cur = conn.cursor()

    # 2. SQL文（INSERT）を準備
    sql = """
    INSERT INTO entries (date, type, account, summary, amount)
    VALUES (?, ?, ?, ?, ?);
    """

    # 3. 値をセット（2025−03−10 の支出・通信費・12000円）
    params = (
        "2025-03-10",       # date
        "expense",          # type
        "通信費",            # account
        "クラウド利用料",     # summary
        12000               # amount
    )

    # 4. SQL実行
    cur.execute(sql, params)

    # 5. 保存
    conn.commit()

    # 6. 接続を閉じる
    conn.close()

    print("✅️ INSERT 完了しました！")

if __name__ == "__main__":
    insert_test_record()