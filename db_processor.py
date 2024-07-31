import os
from dotenv import load_dotenv
from supabase import create_client, Client

#.env 불러오기
load_dotenv()

#환경변수 세팅
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")
supabase : Client = create_client(url, key) #Type Hinting: 데이터타입을 정해주는거임

#[DB]articles 테이블 insert
def insert_into_articles(article):
    print(article)
    response = (
        supabase.table('articles').insert({
            "title": article["title"],
            "link" : article["link"]
        }).execute()
    )

    inserted_row = response.data[0]
    generated_id = inserted_row['id']

    return generated_id