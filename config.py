import os
from supabase import create_client, Client # type: ignore

# Substitua com sua URL e API Key do Supabase
url = "https://lhawtmsyqpvghxyzlvep.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImxoYXd0bXN5cXB2Z2h4eXpsdmVwIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0NjQ3OTYxMCwiZXhwIjoyMDYyMDU1NjEwfQ.pX5_3QYLNJayOKVD_yxJY_B0IWxFbalFXOpqMXTyb8A"
supabase: Client = create_client(url, key)
