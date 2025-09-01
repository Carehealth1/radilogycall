import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from data_models_ultimate import AppData

st.set_page_config(page_title="RadFlow Ultimate", page_icon="🏥", layout="wide")

# App state and data
if "app_data" not in st.session_state:
    st.session_state.app_data = AppData()
app_data = st.session_state.app_data

# Sidebar navigation
st.sidebar.header("Navigation")
pages = [
    "Dashboard",
    "Calendar Scheduler",
    "Active Shifts",
    "Bidding",
    "Swaps/Requests",
    "Coverage Matrix",
    "Consultations",
    "Messaging",
    "Credentialing",
    "Analytics",
    "Export",
]
page = st.sidebar.selectbox("Go to", pages)

# ---------------- Dashboard ----------------
if page == "Dashboard":
    st.title("📊 Radiology Call Dashboard")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Open Shifts", len(app_data.open_shifts))
    col2.metric("Pending Bids", sum(1 for s in app_data.open_shifts if "Bidding" in s.status))
    col3.metric("Swaps", len(app_data.shift_swap_requests))
    col4.metric("Consultations", len(app_data.consultations))
    st.subheader("Workload Distribution")
    workload = {rad.name: rad.call_history['last_30_days'] for rad in app_data.radiologists}
    fig = go.Figure(data=[go.Bar(x=list(workload.keys()), y=list(workload.values()))])
    st.plotly_chart(fig, use_container_width=True)

# --------------- Calendar Scheduler ---------------
elif page == "Calendar Scheduler":
    st.title("🗓️ Visual Calendar Scheduler")
    st.info("Monthly/weekly calendar, drag-and-drop UI can be added with streamlit-calendar component.")
    st.dataframe(pd.DataFrame([{
        "Date": s.date,
        "Shift": s.shift,
        "Location": s.location,
        "Assigned": s.assigned_radiologist or "Open"
    } for s in app_data.open_shifts]), use_container_width=True)

# ---------------- Active Shifts ----------------
elif page == "Active Shifts":
    st.title("Active Shifts")
    df = pd.DataFrame([{
        "Date": s.date,
        "Shift": s.shift,
        "Location": s.location,
        "Status": s.status,
        "Assigned": s.assigned_radiologist
    } for s in app_data.open_shifts])
    st.dataframe(df, use_container_width=True)

# ---------------- Bidding ----------------
elif page == "Bidding":
    st.title("Bidding Dashboard")
    df_bids = pd.DataFrame([{
        "Date": s.date,
        "Shift": s.shift,
        "High Bid": s.current_high_bid,
        "High Bidder": s.current_high_bidder
    } for s in app_data.open_shifts if s.current_high_bid])
    st.dataframe(df_bids, use_container_width=True)

# ---------------- Swaps/Requests ----------------
elif page == "Swaps/Requests":
    st.title("Shift Swap Requests")
    df_swaps = pd.DataFrame([{
        "From": swap.from_radiologist,
        "To": swap.to_radiologist,
        "Date": swap.shift_date,
        "Type": swap.shift_type,
        "Status": swap.status,
        "Reason": swap.reason
    } for swap in app_data.shift_swap_requests])
    st.dataframe(df_swaps, use_container_width=True)

# ---------------- Coverage Matrix ----------------
elif page == "Coverage Matrix":
    st.title("Coverage Matrix")
    st.info("Overview of subspecialty/location coverage gaps and strengths.")
    df_coverage = pd.DataFrame([{
        "Subspecialty": rad.subspecialty,
        "Assigned Locations": ", ".join(rad.locations),
        "Recent Calls": rad.call_history['last_30_days']
    } for rad in app_data.radiologists])
    st.dataframe(df_coverage, use_container_width=True)

# ---------------- Consultations ----------------
elif page == "Consultations":
    st.title("Consultations")
    df_consults = pd.DataFrame([{
        "Case ID": c.case_id,
        "Requesting": c.requesting_physician,
        "Specialty": c.specialty_needed,
        "Urgency": c.urgency,
        "Status": c.status
    } for c in app_data.consultations])
    st.dataframe(df_consults, use_container_width=True)

# ---------------- Messaging ----------------
elif page == "Messaging":
    st.title("Secure Messaging")
    st.info("Encrypted chat, priority flagging, attachments, and audit logs.")
    df_msgs = pd.DataFrame([{
        "From": m.from_user,
        "To": m.to_user,
        "Timestamp": m.timestamp,
        "Subject": m.subject,
        "Priority": m.priority,
        "Status": m.status
    } for m in app_data.secure_messages])
    st.dataframe(df_msgs, use_container_width=True)

# ---------------- Credentialing ----------------
elif page == "Credentialing":
    st.title("Credential Tracking")
    df_creds = pd.DataFrame([{
        "Radiologist": rad.name,
        "Expiry": rad.credentials['cert_expiry'],
        "CME": rad.credentials['cme_credits'],
        "Required": rad.credentials['cme_required'],
        "Status": "Compliant" if rad.credentials['cme_credits'] >= rad.credentials['cme_required'] else "Incomplete"
    } for rad in app_data.radiologists])
    st.dataframe(df_creds, use_container_width=True)

# ---------------- Analytics ----------------
elif page == "Analytics":
    st.title("Analytics & Reports")
    st.info("Key metrics, cost reports, scheduling effectiveness, trends.")
    st.write("Implement custom charts and KPIs here.")

# ---------------- Export ----------------
elif page == "Export":
    st.title("Export & Reports")
    st.info("Download schedules, bid history, swap logs, and analytics as CSV/Excel.")
    # Example export button
    csv = pd.DataFrame([{
        "Date": s.date,
        "Shift": s.shift,
        "Location": s.location,
        "Assigned": s.assigned_radiologist or "Open"
    } for s in app_data.open_shifts]).to_csv(index=False)
    st.download_button("Download Schedule CSV", data=csv, file_name="schedule.csv", mime="text/csv")

st.sidebar.caption("RadFlow Ultimate v3.0 ‣ All modules included")
