#!/bin/bash

echo "🚀 Starting Edithra AGI..."
echo "🔎 Checking environment variables..."
if [ -z "$API_KEY" ]; then
  echo "⚠️ API_KEY is not set. Running without authentication."
fi

echo "📦 Applying database migrations (if applicable)..."
if [ -f "utils/init_db.py" ]; then
  python utils/init_db.py
fi

echo "🟢 Launching Edithra AGI with Uvicorn..."
uvicorn main:app --host 0.0.0.0 --port 8000
