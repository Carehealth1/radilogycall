
"""
Utility functions for RadFlow Pro Streamlit application
"""

from datetime import datetime, timedelta
import streamlit as st

def format_currency(amount):
    """Format currency values"""
    return f"${amount:,.0f}"

def calculate_time_remaining(end_time_str):
    """Calculate time remaining for bidding"""
    try:
        end_time = datetime.fromisoformat(end_time_str.replace('Z', '+00:00'))
        now = datetime.now()
        remaining = end_time - now

        if remaining.total_seconds() > 0:
            hours = int(remaining.total_seconds() // 3600)
            minutes = int((remaining.total_seconds() % 3600) // 60)
            return f"{hours}h {minutes}m"
        else:
            return "Expired"
    except:
        return "Unknown"

def get_status_color(status):
    """Get color for status badges"""
    status_colors = {
        "open": "#fbbf24",
        "active": "#3b82f6", 
        "filled": "#10b981",
        "expired": "#ef4444"
    }
    return status_colors.get(status.lower(), "#6b7280")

def format_date(date_str):
    """Format date strings for display"""
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%b %d, %Y")
    except:
        return date_str

def calculate_bid_increment(current_bid, increment=50):
    """Calculate next bid increment"""
    return current_bid + increment

def get_urgency_emoji(urgency):
    """Get emoji for urgency levels"""
    urgency_emojis = {
        "high": "🔴",
        "medium": "🟡", 
        "low": "🟢"
    }
    return urgency_emojis.get(urgency.lower(), "⚪")

def format_time_ago(timestamp_str):
    """Format timestamp as time ago"""
    try:
        timestamp = datetime.fromisoformat(timestamp_str.replace('Z', '+00:00'))
        now = datetime.now()
        diff = now - timestamp

        if diff.days > 0:
            return f"{diff.days} days ago"
        elif diff.seconds > 3600:
            hours = diff.seconds // 3600
            return f"{hours} hours ago"
        else:
            minutes = diff.seconds // 60
            return f"{minutes} minutes ago"
    except:
        return "Unknown"

def create_status_badge(status, extra_class=""):
    """Create HTML status badge"""
    color_map = {
        "open": ("🟡", "#fef3c7", "#92400e"),
        "active": ("🔵", "#dbeafe", "#1e40af"),
        "filled": ("🟢", "#dcfce7", "#166534"),
        "expired": ("🔴", "#fecaca", "#991b1b")
    }

    emoji, bg_color, text_color = color_map.get(status.lower(), ("⚪", "#f3f4f6", "#374151"))

    return f"""
    <span style="
        background-color: {bg_color}; 
        color: {text_color}; 
        padding: 0.25rem 0.75rem; 
        border-radius: 9999px; 
        font-size: 0.75rem; 
        font-weight: 600; 
        text-transform: uppercase;
        {extra_class}
    ">
        {emoji} {status}
    </span>
    """

def calculate_workload_balance(radiologists_data):
    """Calculate workload balance metrics"""
    total_calls = sum(rad['call_history']['last_30_days'] for rad in radiologists_data)
    avg_calls = total_calls / len(radiologists_data)

    balance_scores = []
    for rad in radiologists_data:
        calls = rad['call_history']['last_30_days']
        variance = abs(calls - avg_calls) / avg_calls if avg_calls > 0 else 0
        balance_scores.append(1 - variance)

    return sum(balance_scores) / len(balance_scores)

def get_credential_status(expiry_date, cme_current, cme_required):
    """Determine credential status"""
    try:
        expiry = datetime.strptime(expiry_date, "%Y-%m-%d")
        now = datetime.now()
        days_until_expiry = (expiry - now).days

        if days_until_expiry < 90:
            return "🔴 Action Required"
        elif cme_current < cme_required:
            return "🟡 CME Needed"
        else:
            return "✅ Compliant"
    except:
        return "⚠️ Unknown"

def generate_schedule_grid(radiologists, locations, start_date=None):
    """Generate a sample schedule grid"""
    if start_date is None:
        start_date = datetime.now()

    schedule = {}
    shifts = ["Day", "Night"]

    for i in range(7):  # Week view
        date = start_date + timedelta(days=i)
        day_name = date.strftime("%A")

        for shift in shifts:
            shift_key = f"{day_name} {shift}"
            schedule[shift_key] = {}

            for location in locations:
                # Simple round-robin assignment for demo
                rad_index = (i + (1 if shift == "Night" else 0)) % len(radiologists)
                if location['staffing_requirements'].get(f'weekday_{shift.lower()}', 0) > 0:
                    schedule[shift_key][location['name']] = radiologists[rad_index]['name']
                else:
                    schedule[shift_key][location['name']] = "—"

    return schedule

def validate_bid_amount(amount, min_bid, max_bid):
    """Validate bid amount"""
    if amount < min_bid:
        return False, f"Bid must be at least ${min_bid}"
    elif amount > max_bid:
        return False, f"Bid cannot exceed ${max_bid}"
    else:
        return True, "Valid bid amount"

def calculate_cost_savings(smart_avg, bidding_avg, smart_shifts, bidding_shifts):
    """Calculate cost savings between methods"""
    smart_total = smart_avg * smart_shifts
    bidding_total = bidding_avg * bidding_shifts

    # Calculate what bidding shifts would have cost with smart distribution
    potential_smart_cost = smart_avg * bidding_shifts
    actual_savings = bidding_total - potential_smart_cost

    return {
        "smart_total": smart_total,
        "bidding_total": bidding_total,
        "potential_savings": actual_savings,
        "savings_percentage": (actual_savings / bidding_total * 100) if bidding_total > 0 else 0
    }

def get_notification_settings():
    """Get default notification settings"""
    return {
        "email": True,
        "sms": False,
        "push": True,
        "shift_reminders": True,
        "bidding_alerts": True,
        "credential_expiry": True,
        "consultation_requests": True
    }

def format_subspecialty_coverage(radiologists):
    """Format subspecialty coverage matrix"""
    coverage = {}
    for rad in radiologists:
        subspecialty = rad['subspecialty']
        if subspecialty not in coverage:
            coverage[subspecialty] = []
        coverage[subspecialty].append(rad['name'])

    return coverage
