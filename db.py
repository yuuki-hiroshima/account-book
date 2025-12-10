"""
SQLite データベースとの接続と、初期化（テーブル作成）を担当するモジュール
"""

import sqlite3
from pathlib import Path

DB_NAME = "ledger.db"

def get_connection():
    """
    ledger.db に接続して、接続オブジェクトを返す。
    row_factory を設定して、行を dict っぽく扱えるようにする。
    """

    db_path = Path(__file__).with_name(DB_NAME) # db.py と同じフォルダ内の DB_NAME(ledger.db)を指す
    conn = sqlite3.connect(db_path)             # SQLite に接続（なければファイルを自動的に作成）
    conn.row_factory = sqlite3.Row              # SELECT の結果を dict 風に扱えるようにする設定
    return conn

def init_db():
    """
    entries テーブルを作成する。
    すでにテーブルが存在する場合は何もしない（IF NOT EXISTS）
    """

    conn = get_connection()
    cur = conn.cursor()

    # entries テーブルを作る SQL
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS entries (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            date    TEXT    NOT NULL,
            type    TEXT    NOT NULL,
            account TEXT    NOT NULL,
            summary TEXT,
            amount  INTEGER NOT NULL
        );
        """
    )

    # 変更を保存
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("✅️ データベースを初期化しました（ledger.db / entries テーブル）。")