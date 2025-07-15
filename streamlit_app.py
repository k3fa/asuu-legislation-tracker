import os
from dotenv import load_dotenv

from sqlalchemy import or_
from database import SessionLocal
import models
import streamlit as st
from datetime import date
load_dotenv()


# Initialize database session

def get_items(search=None, type_filter=None, status_filter=None):
    db = SessionLocal()
    try:
        query = db.query(models.Legislation)
        if search:
            like = f"%{search}%"
            query = query.filter(or_(models.Legislation.title.ilike(like), models.Legislation.summary.ilike(like)))
        if type_filter:
            query = query.filter(models.Legislation.type == type_filter)
        if status_filter:
            query = query.filter(models.Legislation.status == status_filter)
        return query.order_by(models.Legislation.introduced_date.desc()).all()
    finally:
        db.close()


def create_item(data):
    db = SessionLocal()
    try:
        item = models.Legislation(**data)
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    finally:
        db.close()


def main():
    st.title("ASUU Legislation Tracker")

    st.sidebar.header("Filters")
    search = st.sidebar.text_input("Search")
    type_filter = st.sidebar.selectbox("Type", ["", "Senate", "Assembly", "Joint"], index=0)
    status_filter = st.sidebar.text_input("Status")

    items = get_items(search=search or None, type_filter=type_filter or None, status_filter=status_filter or None)

    st.subheader("Legislation List")
    if items:
        for item in items:
            with st.expander(item.title):
                st.write(f"**Type:** {item.type}")
                st.write(f"**Status:** {item.status}")
                if item.summary:
                    st.write(item.summary)
                if item.document_url:
                    st.markdown(f"[Document]({item.document_url})")
    else:
        st.write("No legislation found")

    st.subheader("Add New Legislation")
    with st.form("new_legislation"):
        title = st.text_input("Title")
        leg_type = st.selectbox("Type", ["Senate", "Assembly", "Joint"])
        status = st.text_input("Status")
        introduced = st.date_input("Introduced Date", value=None)
        passed = st.date_input("Passed Date", value=None)
        summary = st.text_area("Summary")
        document_url = st.text_input("Document URL")
        submitted = st.form_submit_button("Create")
        if submitted:
            data = {
                "title": title,
                "type": leg_type,
                "status": status,
                "introduced_date": introduced if isinstance(introduced, date) else None,
                "passed_date": passed if isinstance(passed, date) else None,
                "summary": summary or None,
                "document_url": document_url or None,
            }
            create_item(data)
            st.success("Legislation created")
            st.experimental_rerun()

if __name__ == "__main__":
    main()
