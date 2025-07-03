# ASUU Legislation Tracker Backend

A FastAPI backend for tracking ASUU legislation. Includes endpoints to create, read, update, and delete legislation records. The `GET /legislation` endpoint now supports basic search and filtering.

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

### Filtering and Search

The `GET /legislation` endpoint accepts optional query parameters:

- `q` – search text matched against the title and summary
- `type` – filter by legislation type (e.g. `Senate`, `Assembly`, `Joint`)
- `status` – filter by current status

There are also convenience routes for each type:

- `GET /legislation/senate`
- `GET /legislation/assembly`
- `GET /legislation/joint`

Each of these accepts the same `q` and `status` parameters.

### Railway Deployment
- Link the repo and provision a PostgreSQL database.
- In the project settings add a `DATABASE_URL` variable with the connection string from the Railway database. This replaces the local values in `.env.example`.
- Set the start command:
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

## Next.js Frontend (Supabase & Vercel)
A minimal frontend is provided in the `frontend/` directory. It uses Next.js with Supabase for data storage and Tailwind CSS for styling.

### Setup
1. Create a free Supabase project and add the table using `frontend/supabase_schema.sql`.
2. Copy the Supabase URL and anon key into a `.env.local` file inside `frontend/`:
   ```bash
   NEXT_PUBLIC_SUPABASE_URL=your-url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your-key
   ```
3. Install dependencies and run the development server:
   ```bash
   cd frontend
   npm install
   npm run dev
   ```
4. Deploy the frontend to Vercel and add the same environment variables.

This example provides basic listing and creation of legislation items and can be extended to match additional Notion features.
