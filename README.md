# ASUU Legislation Tracker Backend

A FastAPI backend for tracking ASUU legislation. Includes endpoints to create, read, update, and delete legislation records.

## 🚀 Setup Instructions

### Local Development
1. Clone the repo and install requirements:
   ```bash
   pip install -r requirements.txt
   ```

2. Create a `.env` file from `.env.example` and fill in your database credentials.

3. Create your database and run:
   ```bash
   psql -h HOST -U USER -d DBNAME -f setup.sql
   ```

4. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

Visit `http://localhost:8000/docs` to view the API.

### Railway Deployment
- Link repo and provision PostgreSQL
- Add env variables from `.env.example`
- Set start command:
  ```bash
  uvicorn main:app --host 0.0.0.0 --port $PORT
  ```
- Done 🎉

### Docker
Build the container image:
```bash
docker build -t asuu-legislation-tracker .
```

Run the container using your `.env` file:
```bash
docker run --env-file .env -p 8000:8000 asuu-legislation-tracker
```
