import os
from supabase import create_client, Client # type: ignore

# Substitua com sua URL e API Key do Supabase
url = "https://lhawtmsyqpvghxyzlvep.supabase.co"
key = ""
supabase: Client = create_client(url, key)
