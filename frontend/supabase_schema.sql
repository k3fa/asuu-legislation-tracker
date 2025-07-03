create table if not exists public.legislation (
  id serial primary key,
  title text not null,
  type varchar(50) not null,
  status varchar(50) not null,
  introduced_date date,
  passed_date date,
  summary text,
  document_url text
);
