
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from data_models import AppData
from utils import format_currency, calculate_time_remaining, get_status_color

# Set page config
st.set_page_config(
    page_title="RadFlow Pro - Radiology Workflow Management",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1f2937;
        margin-bottom: 1rem;
    }
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 0.5rem;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        border-left: 4px solid #3b82f6;
    }
    .metric-value {
        font-size: 2rem;
        font-weight: 700;
        color: #1f2937;
    }
    .metric-label {
        font-size: 0.875rem;
        color: #6b7280;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .status-badge {
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
    }
    .status-open { background-color: #fef3c7; color: #92400e; }
    .status-active { background-color: #dbeafe; color: #1e40af; }
    .status-filled { background-color: #dcfce7; color: #166534; }
    .bidding-card {
        background: linear-gradient(135deg, #fff7ed 0%, #fed7aa 100%);
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 2px solid #fb923c;
    }
    .smart-card {
        background: linear-gradient(135deg, #f0f9ff 0%, #bae6fd 100%);
        padding: 1.5rem;
        border-radius: 0.75rem;
        border: 2px solid #0ea5e9;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = 'Dashboard'

# Initialize data
app_data = AppData()

# Sidebar Navigation
with st.sidebar:
    st.markdown("# 🏥 RadFlow Pro")
    st.markdown("### Radiology Workflow Management")

    # User profile
    st.markdown("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("👨‍⚕️")
    with col2:
        st.markdown("**Dr. Sarah Chen**")
        st.markdown("*Neuroradiology*")
        st.markdown("🟢 Online")
    st.markdown("---")

    # Navigation menu
    pages = [
        "📊 Dashboard",
        "📅 Call Schedule",
        "🏷️ Bidding Dashboard", 
        "🏥 Multi-Location Tracker",
        "💬 Case Consultation",
        "✉️ Secure Messaging",
        "🎓 Credential Tracking",
        "📈 Analytics & Reports",
        "⚙️ Settings"
    ]

    for page in pages:
        if st.button(page, key=page, use_container_width=True):
            st.session_state.current_page = page.split(" ", 1)[1]

# Main content area
current_page = st.session_state.current_page

if current_page == "Dashboard":
    st.markdown('<h1 class="main-header">📊 Dashboard Overview</h1>', unsafe_allow_html=True)

    # Key metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">3</div>
            <div class="metric-label">Upcoming Calls</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">2</div>
            <div class="metric-label">Open Shifts</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1</div>
            <div class="metric-label">Active Bidding</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <div class="metric-value">1</div>
            <div class="metric-label">Credentials Due</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Recent activity and quick actions
    col1, col2 = st.columns([2, 1])

    with col1:
        st.subheader("📋 Recent Activity")
        activities = [
            "🔄 Dr. Rodriguez bid $2850 on Weekend Night shift",
            "✅ Weekend Day shift auto-assigned to Dr. Johnson",
            "⚠️ Dr. Rodriguez credential expires in 90 days",
            "💬 New consultation request: Vascular malformation case"
        ]
        for activity in activities:
            st.markdown(f"• {activity}")

    with col2:
        st.subheader("⚡ Quick Actions")
        if st.button("🎯 Auto-Fill Open Shifts", use_container_width=True):
            st.success("Smart distribution algorithm activated!")
        if st.button("📨 Send Shift Reminders", use_container_width=True):
            st.info("Reminder notifications sent to all radiologists")
        if st.button("📊 Generate Weekly Report", use_container_width=True):
            st.info("Weekly analytics report generated")

elif current_page == "Call Schedule":
    st.markdown('<h1 class="main-header">📅 Call Schedule Management</h1>', unsafe_allow_html=True)

    # Mode selector
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        assignment_mode = st.selectbox(
            "🎯 Assignment Mode",
            ["Smart Distribution (Recommended)", "Bidding Mode", "Hybrid (Smart First)"],
            help="Choose how open shifts are filled"
        )

    with col2:
        if st.button("🔄 Auto-Fill All Open Shifts"):
            st.success("Smart distribution algorithm processing all open shifts...")

    with col3:
        if st.button("📊 View Assignment Analytics"):
            st.session_state.current_page = "Analytics & Reports"
            st.rerun()

    st.markdown("---")

    # Open shifts
    st.subheader("🎯 Open Shifts Management")

    # Create sample shift data
    shifts_data = [
        {
            "Date": "Sep 7, 2025",
            "Shift": "Weekend Day",
            "Location": "Main Hospital", 
            "Duration": "12 hours",
            "Base Pay": "$2,400",
            "Mode": "Smart Distribution",
            "Status": "Open",
            "Action": "Auto-Assign"
        },
        {
            "Date": "Sep 14, 2025", 
            "Shift": "Weekend Night",
            "Location": "Outpatient Center",
            "Duration": "12 hours", 
            "Base Pay": "$2,600",
            "Mode": "Bidding Mode",
            "Status": "Active Bidding - $2,850",
            "Action": "View Bids"
        },
        {
            "Date": "Sep 21, 2025",
            "Shift": "Weekend Day", 
            "Location": "Sports Medicine",
            "Duration": "8 hours",
            "Base Pay": "$1,800", 
            "Mode": "Hybrid",
            "Status": "Smart Failed → Bidding",
            "Action": "Monitor"
        }
    ]

    df_shifts = pd.DataFrame(shifts_data)

    # Display with custom styling
    for idx, shift in df_shifts.iterrows():
        with st.container():
            col1, col2, col3, col4 = st.columns([2, 2, 2, 1])

            with col1:
                st.markdown(f"**{shift['Date']} - {shift['Shift']}**")
                st.markdown(f"📍 {shift['Location']} ({shift['Duration']})")

            with col2:
                if "Smart" in shift['Mode']:
                    st.markdown(f'<div class="smart-card">🤖 {shift["Mode"]}<br>💰 {shift["Base Pay"]}</div>', unsafe_allow_html=True)
                else:
                    st.markdown(f'<div class="bidding-card">🏷️ {shift["Mode"]}<br>💰 {shift["Base Pay"]}</div>', unsafe_allow_html=True)

            with col3:
                status_color = "status-open" if "Open" in shift['Status'] else "status-active" if "Bidding" in shift['Status'] else "status-filled"
                st.markdown(f'<span class="status-badge {status_color}">{shift["Status"]}</span>', unsafe_allow_html=True)

            with col4:
                if shift['Action'] == "Auto-Assign":
                    if st.button("🎯 Assign", key=f"assign_{idx}"):
                        st.success("Shift auto-assigned using smart distribution!")
                elif shift['Action'] == "View Bids":
                    if st.button("👀 View", key=f"view_{idx}"):
                        st.session_state.current_page = "Bidding Dashboard"
                        st.rerun()
                else:
                    st.button("📊 Monitor", key=f"monitor_{idx}")

            st.markdown("---")

elif current_page == "Bidding Dashboard":
    st.markdown('<h1 class="main-header">🏷️ Active Bidding Dashboard</h1>', unsafe_allow_html=True)

    # Active bidding shift
    st.subheader("🔥 Currently Active Bidding")

    with st.container():
        st.markdown("""
        <div class="bidding-card">
            <h3>🌙 Weekend Night Shift - September 14, 2025</h3>
            <p><strong>📍 Location:</strong> Outpatient Center</p>
            <p><strong>⏰ Duration:</strong> 12 hours (7 PM - 7 AM)</p>
            <p><strong>🩺 Specialty:</strong> General Radiology</p>
            <p><strong>💰 Base Rate:</strong> $2,600</p>
        </div>
        """, unsafe_allow_html=True)

    # Bidding interface
    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 🏆 Current High Bid")
        st.markdown("**$2,850** by Dr. Michael Rodriguez")
        st.progress(0.7)
        st.markdown("⏰ **18 hours remaining**")

        # Bid history
        st.markdown("### 📜 Bid History")
        bid_history = [
            {"Time": "4:30 PM", "Radiologist": "Dr. James Park", "Amount": "$2,700"},
            {"Time": "4:15 PM", "Radiologist": "Dr. Michael Rodriguez", "Amount": "$2,850"},
        ]

        for bid in bid_history:
            st.markdown(f"• **{bid['Time']}** - {bid['Radiologist']}: **{bid['Amount']}**")

    with col2:
        st.markdown("### 🎯 Place Your Bid")

        current_bid = 2850
        min_bid = current_bid + 50

        # Quick bid buttons
        st.markdown("**Quick Bid Options:**")
        col_a, col_b, col_c = st.columns(3)
        with col_a:
            if st.button(f"${min_bid}", use_container_width=True):
                st.success(f"Bid placed: ${min_bid}")
        with col_b:
            if st.button(f"${min_bid + 100}", use_container_width=True):
                st.success(f"Bid placed: ${min_bid + 100}")
        with col_c:
            if st.button(f"${min_bid + 200}", use_container_width=True):
                st.success(f"Bid placed: ${min_bid + 200}")

        # Custom bid amount
        st.markdown("**Custom Bid Amount:**")
        custom_bid = st.number_input("Enter bid amount", min_value=min_bid, max_value=4000, step=50, value=min_bid)

        if st.button("🚀 Place Custom Bid", use_container_width=True):
            st.success(f"Bid placed: ${custom_bid}")

        # Auto-bid settings
        st.markdown("---")
        st.markdown("**🤖 Auto-Bid Settings:**")
        auto_bid_max = st.number_input("Maximum auto-bid amount", min_value=min_bid, max_value=4000, step=50, value=3000)
        auto_bid_enabled = st.checkbox("Enable auto-bidding for this shift")

        if auto_bid_enabled:
            st.info(f"Auto-bid active up to ${auto_bid_max}")

elif current_page == "Multi-Location Tracker":
    st.markdown('<h1 class="main-header">🏥 Multi-Location Schedule Tracker</h1>', unsafe_allow_html=True)

    # Location selector
    locations = ["All Locations", "Main Hospital", "Outpatient Center", "Sports Medicine Center", "Pulmonary Center"]
    selected_location = st.selectbox("📍 Select Location", locations)

    # Coverage overview
    st.subheader("📊 Coverage Overview")

    coverage_data = [
        {"Location": "Main Hospital", "Day_Coverage": "✅ Full", "Night_Coverage": "✅ Full", "Weekend": "⚠️ 1 Gap", "Staff_Count": 4},
        {"Location": "Outpatient Center", "Day_Coverage": "✅ Full", "Night_Coverage": "➖ N/A", "Weekend": "🔴 Open", "Staff_Count": 2},
        {"Location": "Sports Medicine", "Day_Coverage": "✅ Full", "Night_Coverage": "➖ N/A", "Weekend": "🔴 Open", "Staff_Count": 1},
        {"Location": "Pulmonary Center", "Day_Coverage": "✅ Full", "Night_Coverage": "➖ N/A", "Weekend": "✅ Full", "Staff_Count": 1}
    ]

    df_coverage = pd.DataFrame(coverage_data)
    st.dataframe(df_coverage, use_container_width=True)

    # Schedule grid
    st.subheader("📅 Weekly Schedule Grid")

    # Sample schedule data
    schedule_data = {
        "Shift": ["Monday Day", "Monday Night", "Tuesday Day", "Tuesday Night", "Wednesday Day", "Wednesday Night"],
        "Main Hospital": ["Dr. Chen", "Dr. Park", "Dr. Rodriguez", "Dr. Johnson", "Dr. Chen", "Dr. Park"],
        "Outpatient Center": ["Dr. Johnson", "—", "Dr. Chen", "—", "Dr. Rodriguez", "—"],
        "Sports Medicine": ["Dr. Rodriguez", "—", "Dr. Park", "—", "Dr. Rodriguez", "—"],
        "Pulmonary Center": ["Dr. Johnson", "—", "Dr. Johnson", "—", "Dr. Johnson", "—"]
    }

    df_schedule = pd.DataFrame(schedule_data)
    st.dataframe(df_schedule, use_container_width=True)

    # Quick actions
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🔄 Sync All Locations"):
            st.success("All location schedules synchronized!")
    with col2:
        if st.button("⚠️ Identify Coverage Gaps"):
            st.warning("2 coverage gaps identified across locations")
    with col3:
        if st.button("📱 Send Mobile Updates"):
            st.info("Mobile notifications sent to all radiologists")

elif current_page == "Analytics & Reports":
    st.markdown('<h1 class="main-header">📈 Analytics & Performance Reports</h1>', unsafe_allow_html=True)

    # Mode comparison
    st.subheader("🔄 Assignment Mode Comparison")

    col1, col2 = st.columns(2)

    with col1:
        # Cost comparison chart
        modes = ['Smart Distribution', 'Bidding Mode']
        costs = [2450, 2780]
        fig_cost = px.bar(x=modes, y=costs, title="Average Cost per Shift", 
                         color=modes, color_discrete_map={'Smart Distribution': '#0ea5e9', 'Bidding Mode': '#fb923c'})
        fig_cost.update_layout(showlegend=False)
        st.plotly_chart(fig_cost, use_container_width=True)

    with col2:
        # Time to fill comparison
        times = [2.3, 18.5]
        fig_time = px.bar(x=modes, y=times, title="Average Time to Fill (Hours)",
                         color=modes, color_discrete_map={'Smart Distribution': '#0ea5e9', 'Bidding Mode': '#fb923c'})
        fig_time.update_layout(showlegend=False)
        st.plotly_chart(fig_time, use_container_width=True)

    # Workload distribution
    st.subheader("⚖️ Workload Distribution")

    radiologists = ['Dr. Chen', 'Dr. Rodriguez', 'Dr. Johnson', 'Dr. Park']
    calls_current = [4, 6, 3, 5]
    calls_target = [6, 6, 6, 6]

    fig_workload = go.Figure()
    fig_workload.add_trace(go.Bar(name='Current Month', x=radiologists, y=calls_current, marker_color='#0ea5e9'))
    fig_workload.add_trace(go.Bar(name='Target', x=radiologists, y=calls_target, marker_color='#fb923c'))
    fig_workload.update_layout(title='Calls This Month vs Target', barmode='group')
    st.plotly_chart(fig_workload, use_container_width=True)

    # Financial impact
    st.subheader("💰 Monthly Financial Impact")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Smart Distribution", "$58,800", "↓ $8,640")
    with col2:
        st.metric("Bidding Mode", "$22,240", "↑ $2,240") 
    with col3:
        st.metric("Total Savings", "$8,640", "14.2%")

elif current_page == "Case Consultation":
    st.markdown('<h1 class="main-header">💬 Case Consultation Hub</h1>', unsafe_allow_html=True)

    # Active consultations
    st.subheader("🔥 Active Consultation Requests")

    consultations = [
        {
            "Case ID": "RAD-2025-001",
            "Requesting": "Dr. Sarah Chen",
            "Specialty": "Interventional",
            "Urgency": "🔴 High",
            "Description": "Complex vascular malformation requiring intervention planning",
            "Status": "Awaiting Response"
        },
        {
            "Case ID": "RAD-2025-002", 
            "Requesting": "Dr. Emily Johnson",
            "Specialty": "Neuroradiology",
            "Urgency": "🟡 Medium",
            "Description": "Unusual white matter lesion pattern in young patient",
            "Status": "Under Review"
        }
    ]

    for consultation in consultations:
        with st.expander(f"{consultation['Case ID']} - {consultation['Specialty']} ({consultation['Urgency']})"):
            col1, col2 = st.columns([2, 1])

            with col1:
                st.markdown(f"**Requesting Physician:** {consultation['Requesting']}")
                st.markdown(f"**Description:** {consultation['Description']}")
                st.markdown(f"**Status:** {consultation['Status']}")

            with col2:
                if st.button("🩺 Provide Consultation", key=f"consult_{consultation['Case ID']}"):
                    st.success("Consultation response submitted!")
                if st.button("📤 Forward to Expert", key=f"forward_{consultation['Case ID']}"):
                    st.info("Case forwarded to subspecialty expert")

    # New consultation request
    st.subheader("➕ Request New Consultation")

    with st.form("new_consultation"):
        case_id = st.text_input("Case ID", value="RAD-2025-003")
        specialty_needed = st.selectbox("Specialty Needed", 
                                       ["Neuroradiology", "Musculoskeletal", "Chest Imaging", "Interventional", "General"])
        urgency = st.selectbox("Urgency Level", ["🔴 High", "🟡 Medium", "🟢 Low"])
        description = st.text_area("Case Description")

        if st.form_submit_button("📤 Submit Consultation Request"):
            st.success("Consultation request submitted successfully!")

elif current_page == "Secure Messaging":
    st.markdown('<h1 class="main-header">✉️ HIPAA-Compliant Secure Messaging</h1>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("👥 Contacts")

        contacts = [
            {"name": "Dr. Michael Rodriguez", "status": "🟢 Online", "unread": 1},
            {"name": "Dr. Emily Johnson", "status": "🟡 Away", "unread": 0},
            {"name": "Dr. James Park", "status": "🟢 Online", "unread": 2},
            {"name": "All Radiologists", "status": "📢 Group", "unread": 0}
        ]

        selected_contact = None
        for contact in contacts:
            unread_badge = f" ({contact['unread']})" if contact['unread'] > 0 else ""
            if st.button(f"{contact['name']}{unread_badge}", key=contact['name'], use_container_width=True):
                selected_contact = contact['name']

        st.markdown("---")
        st.subheader("🔒 Security Status")
        st.success("🔐 End-to-end encryption active")
        st.info("📋 Audit logging enabled")

    with col2:
        st.subheader("💬 Messages")

        # Sample conversation
        messages = [
            {"sender": "Dr. Michael Rodriguez", "time": "2:45 PM", "message": "Can you cover my weekend shift? Family emergency.", "type": "received"},
            {"sender": "You", "time": "2:50 PM", "message": "Of course! I can take the Saturday shift. Hope everything is okay.", "type": "sent"},
            {"sender": "Dr. Michael Rodriguez", "time": "2:52 PM", "message": "Thank you so much! I'll make it up to you.", "type": "received"}
        ]

        # Message display
        for msg in messages:
            if msg['type'] == 'sent':
                st.markdown(f"""
                <div style="text-align: right; margin: 10px 0;">
                    <div style="background-color: #0ea5e9; color: white; padding: 10px; border-radius: 10px; display: inline-block; max-width: 70%;">
                        {msg['message']}
                    </div>
                    <div style="font-size: 0.8em; color: #666; margin-top: 5px;">
                        {msg['time']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="text-align: left; margin: 10px 0;">
                    <div style="background-color: #f3f4f6; padding: 10px; border-radius: 10px; display: inline-block; max-width: 70%;">
                        <strong>{msg['sender']}</strong><br>
                        {msg['message']}
                    </div>
                    <div style="font-size: 0.8em; color: #666; margin-top: 5px;">
                        {msg['time']}
                    </div>
                </div>
                """, unsafe_allow_html=True)

        # Message input
        with st.form("send_message"):
            new_message = st.text_area("Type your message...")
            col_a, col_b, col_c = st.columns([2, 1, 1])
            with col_a:
                if st.form_submit_button("📤 Send Message"):
                    st.success("Message sent securely!")
            with col_b:
                priority = st.selectbox("Priority", ["Normal", "High", "Urgent"], key="msg_priority")
            with col_c:
                attach_file = st.file_uploader("📎", type=['pdf', 'jpg', 'png'], key="msg_file")

elif current_page == "Credential Tracking":
    st.markdown('<h1 class="main-header">🎓 Credential & Certification Tracking</h1>', unsafe_allow_html=True)

    # Credential overview
    st.subheader("📋 Certification Status Overview")

    credential_data = [
        {"Radiologist": "Dr. Sarah Chen", "Board_Cert": "✅ Valid", "Expiry": "Mar 15, 2026", "CME": "45/50", "Status": "🟡 CME Needed"},
        {"Radiologist": "Dr. Michael Rodriguez", "Board_Cert": "⚠️ Expires Soon", "Expiry": "Nov 30, 2025", "CME": "38/50", "Status": "🔴 Action Required"},
        {"Radiologist": "Dr. Emily Johnson", "Board_Cert": "✅ Valid", "Expiry": "Jan 20, 2027", "CME": "52/50", "Status": "✅ Compliant"},
        {"Radiologist": "Dr. James Park", "Board_Cert": "✅ Valid", "Expiry": "Aug 10, 2026", "CME": "41/50", "Status": "🟡 CME Needed"}
    ]

    df_credentials = pd.DataFrame(credential_data)
    st.dataframe(df_credentials, use_container_width=True)

    # Renewal alerts
    st.subheader("⚠️ Upcoming Renewals & Actions Required")

    alerts = [
        "🔴 Dr. Rodriguez: Board certification expires in 90 days",
        "🟡 Dr. Chen: Needs 5 more CME credits by Dec 31",
        "🟡 Dr. Park: Needs 9 more CME credits by Dec 31",
        "📅 Annual compliance report due in 30 days"
    ]

    for alert in alerts:
        st.warning(alert)

    # Quick actions
    col1, col2, col3 = st.columns(3)

    with col1:
        if st.button("📧 Send Renewal Reminders"):
            st.success("Renewal reminders sent to affected radiologists")

    with col2:
        if st.button("📊 Generate Compliance Report"):
            st.info("Compliance report generated and ready for download")

    with col3:
        if st.button("🔄 Update CME Credits"):
            st.info("CME credit update form opened")

elif current_page == "Settings":
    st.markdown('<h1 class="main-header">⚙️ System Settings & Configuration</h1>', unsafe_allow_html=True)

    # Department settings
    st.subheader("🏥 Department Settings")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Default Assignment Mode**")
        default_mode = st.radio("", ["Smart Distribution", "Bidding Mode", "Hybrid"], key="default_mode")

        st.markdown("**Bidding Rules**")
        min_weekend_bid = st.number_input("Minimum Weekend Day Bid", value=2200, step=50)
        max_bid_limit = st.number_input("Maximum Bid Limit", value=4000, step=100)
        bidding_time_limit = st.number_input("Bidding Time Limit (hours)", value=24, step=1)

    with col2:
        st.markdown("**Notification Settings**")
        email_notifications = st.checkbox("Email Notifications", value=True)
        sms_notifications = st.checkbox("SMS Notifications", value=True)
        push_notifications = st.checkbox("Push Notifications", value=True)

        st.markdown("**Integration Settings**")
        pacs_integration = st.checkbox("PACS Integration", value=True)
        ris_integration = st.checkbox("RIS Integration", value=True)
        emr_integration = st.checkbox("EMR Integration", value=False)

    # Personal preferences
    st.subheader("👤 Personal Preferences")

    max_weekend_calls = st.slider("Maximum Weekend Calls per Month", 1, 6, 2)
    preferred_locations = st.multiselect("Preferred Locations", 
                                        ["Main Hospital", "Outpatient Center", "Sports Medicine Center", "Pulmonary Center"],
                                        default=["Main Hospital"])
    bidding_opt_in = st.checkbox("Participate in Bidding", value=True)
    max_auto_bid = st.number_input("Maximum Auto-bid Amount", value=2800, step=50)

    # Save settings
    if st.button("💾 Save All Settings", use_container_width=True):
        st.success("All settings saved successfully!")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6b7280; font-size: 0.8em;'>
    RadFlow Pro - Advanced Radiology Workflow Management System<br>
    🔒 HIPAA Compliant | 🌐 Multi-Location Support | 🤖 AI-Powered Scheduling
</div>
""", unsafe_allow_html=True)
