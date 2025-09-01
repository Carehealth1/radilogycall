
"""
Ultimate data models for RadFlow Ultimate - Complete Radiology Workflow Management
Includes all original web app features plus enhanced Streamlit functionality
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional, Any
from datetime import datetime, timedelta
import json

@dataclass
class Radiologist:
    id: int
    name: str
    subspecialty: str
    locations: List[str]
    credentials: Dict[str, Any]
    preferences: Dict[str, Any]
    call_history: Dict[str, Any]
    bidding_stats: Dict[str, Any]
    performance_metrics: Optional[Dict[str, Any]] = None
    contact_info: Optional[Dict[str, Any]] = None
    availability_status: str = "Available"
    current_location: Optional[str] = None

@dataclass
class Location:
    name: str
    address: str
    modalities: List[str]
    staffing_requirements: Dict[str, int]
    current_staff: Optional[List[str]] = None
    equipment_status: Optional[Dict[str, Any]] = None
    operating_hours: Optional[Dict[str, str]] = None
    coordinates: Optional[Dict[str, float]] = None
    capacity_metrics: Optional[Dict[str, Any]] = None

@dataclass
class OpenShift:
    id: int
    date: str
    shift: str
    location: str
    subspecialty_required: str
    duration: str
    base_compensation: int
    assignment_mode: str
    status: str
    current_high_bid: Optional[int] = None
    current_high_bidder: Optional[str] = None
    bid_history: Optional[List[Dict[str, Any]]] = None
    smart_distribution_tried: Optional[bool] = False
    assigned_radiologist: Optional[str] = None
    created_timestamp: Optional[str] = None
    bidding_end_time: Optional[str] = None
    priority_level: str = "Normal"
    coverage_requirements: Optional[Dict[str, Any]] = None

@dataclass
class ShiftSwapRequest:
    id: str
    from_radiologist: str
    to_radiologist: str
    shift_date: str
    shift_type: str
    location: str
    reason: str
    priority: str
    status: str
    requested_timestamp: str
    admin_notes: Optional[str] = None
    approval_timestamp: Optional[str] = None
    auto_approved: bool = False
    notification_sent: bool = False

@dataclass
class Consultation:
    id: int
    case_id: str
    requesting_physician: str
    specialty_needed: str
    urgency: str
    description: str
    status: str
    created: str
    patient_age: Optional[int] = None
    patient_gender: Optional[str] = None
    study_type: Optional[str] = None
    clinical_history: Optional[str] = None
    imaging_findings: Optional[str] = None
    specific_question: Optional[str] = None
    assigned_expert: Optional[str] = None
    response_time: Optional[str] = None
    discussion_thread: Optional[List[Dict[str, Any]]] = None
    case_images: Optional[List[str]] = None
    teaching_case: bool = False

@dataclass
class SecureMessage:
    id: int
    from_user: str
    to_user: str
    subject: str
    message: str
    timestamp: str
    priority: str
    status: str
    encrypted: bool = True
    attachments: Optional[List[str]] = None
    thread_id: Optional[str] = None
    read_receipt: bool = False
    delivery_confirmation: bool = False

@dataclass
class CredentialRecord:
    radiologist_id: int
    credential_type: str
    issuing_body: str
    credential_number: str
    issue_date: str
    expiry_date: str
    status: str
    cme_required: int              # <-- Add this field
    cme_credits: int               # <-- And this field
    renewal_requirements: Optional[Dict[str, Any]] = None
    cme_activities: Optional[List[Dict[str, Any]]] = None
    auto_renewal_enabled: bool = False
    reminder_schedule: Optional[List[int]] = None  # Days before expiry


@dataclass
class ScheduleTemplate:
    id: str
    name: str
    description: str
    template_type: str  # "weekly", "monthly", "holiday"
    assignments: Dict[str, Any]
    created_by: str
    created_date: str
    usage_count: int = 0
    last_used: Optional[str] = None

@dataclass
class NotificationSettings:
    user_id: int
    email_enabled: bool = True
    sms_enabled: bool = True
    push_enabled: bool = True
    quiet_hours_start: str = "22:00"
    quiet_hours_end: str = "06:00"
    priority_override: bool = True
    categories: Optional[Dict[str, bool]] = None

class AppData:
    def __init__(self):
        self.radiologists = [
            Radiologist(
                id=1,
                name="Dr. Sarah Chen",
                subspecialty="Neuroradiology",
                locations=["Main Hospital", "Outpatient Center"],
                credentials={
                    "board_certified": True,
                    "cert_expiry": "2026-03-15",
                    "cme_credits": 45,
                    "cme_required": 50,
                    "license_number": "RAD12345",
                    "subspecialty_board": "American Board of Radiology - Neuroradiology",
                    "malpractice_insurance": "Active",
                    "hospital_privileges": ["Main Hospital", "Outpatient Center"]
                },
                preferences={
                    "max_weekend_calls": 2,
                    "preferred_locations": ["Main Hospital"],
                    "blackout_dates": ["2025-12-20", "2025-12-27"],
                    "bidding_opt_in": True,
                    "max_auto_bid": 2800,
                    "preferred_assignment_mode": "Smart Distribution",
                    "shift_preferences": {
                        "day_shifts": 0.8,
                        "night_shifts": 0.4,
                        "weekend_shifts": 0.6,
                        "holiday_shifts": 0.3
                    },
                    "notification_preferences": {
                        "email": True,
                        "sms": True,
                        "push": True,
                        "quiet_hours": "22:00-06:00"
                    }
                },
                call_history={
                    "last_30_days": 4,
                    "year_total": 24,
                    "weekend_calls_ytd": 8,
                    "night_calls_ytd": 12,
                    "holiday_calls_ytd": 2,
                    "total_hours_ytd": 288,
                    "avg_shift_length": 12
                },
                bidding_stats={
                    "bids_placed": 8,
                    "bids_won": 5,
                    "avg_winning_bid": 2650,
                    "total_bidding_earnings": 13250,
                    "highest_bid": 3200,
                    "win_rate": 62.5,
                    "last_bid_date": "2025-08-30"
                },
                performance_metrics={
                    "satisfaction_score": 9.1,
                    "response_time_avg": "18 minutes",
                    "consultation_requests": 15,
                    "teaching_cases": 8,
                    "quality_score": 4.7,
                    "peer_rating": 4.8
                },
                contact_info={
                    "email": "s.chen@hospital.com",
                    "phone": "555-0101",
                    "office": "Neuro Reading Room 3A",
                    "emergency_contact": "555-0102"
                },
                availability_status="Available",
                current_location="Main Hospital"
            ),
            Radiologist(
                id=2,
                name="Dr. Michael Rodriguez",
                subspecialty="Musculoskeletal",
                locations=["Main Hospital", "Sports Medicine Center"],
                credentials={
                    "board_certified": True,
                    "cert_expiry": "2025-11-30",
                    "cme_credits": 38,
                    "cme_required": 50,
                    "license_number": "RAD23456",
                    "subspecialty_board": "American Board of Radiology - Musculoskeletal",
                    "malpractice_insurance": "Active",
                    "hospital_privileges": ["Main Hospital", "Sports Medicine Center"]
                },
                preferences={
                    "max_weekend_calls": 3,
                    "preferred_locations": ["Sports Medicine Center"],
                    "blackout_dates": ["2025-10-15", "2025-11-22"],
                    "bidding_opt_in": True,
                    "max_auto_bid": 3000,
                    "preferred_assignment_mode": "Either",
                    "shift_preferences": {
                        "day_shifts": 0.9,
                        "night_shifts": 0.5,
                        "weekend_shifts": 0.8,
                        "holiday_shifts": 0.6
                    },
                    "notification_preferences": {
                        "email": True,
                        "sms": False,
                        "push": True,
                        "quiet_hours": "23:00-05:00"
                    }
                },
                call_history={
                    "last_30_days": 6,
                    "year_total": 32,
                    "weekend_calls_ytd": 12,
                    "night_calls_ytd": 16,
                    "holiday_calls_ytd": 4,
                    "total_hours_ytd": 384,
                    "avg_shift_length": 12
                },
                bidding_stats={
                    "bids_placed": 12,
                    "bids_won": 7,
                    "avg_winning_bid": 2750,
                    "total_bidding_earnings": 19250,
                    "highest_bid": 3500,
                    "win_rate": 58.3,
                    "last_bid_date": "2025-08-31"
                },
                performance_metrics={
                    "satisfaction_score": 8.7,
                    "response_time_avg": "22 minutes",
                    "consultation_requests": 12,
                    "teaching_cases": 5,
                    "quality_score": 4.5,
                    "peer_rating": 4.6
                },
                contact_info={
                    "email": "m.rodriguez@hospital.com",
                    "phone": "555-0102",
                    "office": "MSK Reading Room 2B",
                    "emergency_contact": "555-0103"
                },
                availability_status="Available",
                current_location="Sports Medicine Center"
            ),
            Radiologist(
                id=3,
                name="Dr. Emily Johnson",
                subspecialty="Chest Imaging",
                locations=["Main Hospital", "Pulmonary Center"],
                credentials={
                    "board_certified": True,
                    "cert_expiry": "2027-01-20",
                    "cme_credits": 52,
                    "cme_required": 50,
                    "license_number": "RAD34567",
                    "subspecialty_board": "American Board of Radiology - Thoracic",
                    "malpractice_insurance": "Active",
                    "hospital_privileges": ["Main Hospital", "Pulmonary Center"]
                },
                preferences={
                    "max_weekend_calls": 2,
                    "preferred_locations": ["Pulmonary Center"],
                    "blackout_dates": ["2025-09-10", "2025-12-25"],
                    "bidding_opt_in": False,
                    "max_auto_bid": 0,
                    "preferred_assignment_mode": "Smart Distribution Only",
                    "shift_preferences": {
                        "day_shifts": 0.9,
                        "night_shifts": 0.3,
                        "weekend_shifts": 0.5,
                        "holiday_shifts": 0.2
                    },
                    "notification_preferences": {
                        "email": True,
                        "sms": True,
                        "push": False,
                        "quiet_hours": "21:00-07:00"
                    }
                },
                call_history={
                    "last_30_days": 3,
                    "year_total": 18,
                    "weekend_calls_ytd": 6,
                    "night_calls_ytd": 8,
                    "holiday_calls_ytd": 1,
                    "total_hours_ytd": 216,
                    "avg_shift_length": 12
                },
                bidding_stats={
                    "bids_placed": 0,
                    "bids_won": 0,
                    "avg_winning_bid": 0,
                    "total_bidding_earnings": 0,
                    "highest_bid": 0,
                    "win_rate": 0,
                    "last_bid_date": None
                },
                performance_metrics={
                    "satisfaction_score": 9.3,
                    "response_time_avg": "15 minutes",
                    "consultation_requests": 18,
                    "teaching_cases": 12,
                    "quality_score": 4.9,
                    "peer_rating": 4.9
                },
                contact_info={
                    "email": "e.johnson@hospital.com",
                    "phone": "555-0103",
                    "office": "Chest Reading Room 1A",
                    "emergency_contact": "555-0104"
                },
                availability_status="Available",
                current_location="Pulmonary Center"
            ),
            Radiologist(
                id=4,
                name="Dr. James Park",
                subspecialty="Interventional",
                locations=["Main Hospital"],
                credentials={
                    "board_certified": True,
                    "cert_expiry": "2026-08-10",
                    "cme_credits": 41,
                    "cme_required": 50,
                    "license_number": "RAD45678",
                    "subspecialty_board": "American Board of Radiology - Interventional",
                    "malpractice_insurance": "Active",
                    "hospital_privileges": ["Main Hospital"]
                },
                preferences={
                    "max_weekend_calls": 4,
                    "preferred_locations": ["Main Hospital"],
                    "blackout_dates": ["2025-11-15"],
                    "bidding_opt_in": True,
                    "max_auto_bid": 3200,
                    "preferred_assignment_mode": "Bidding Preferred",
                    "shift_preferences": {
                        "day_shifts": 0.7,
                        "night_shifts": 0.8,
                        "weekend_shifts": 0.9,
                        "holiday_shifts": 0.8
                    },
                    "notification_preferences": {
                        "email": True,
                        "sms": True,
                        "push": True,
                        "quiet_hours": "23:30-05:30"
                    }
                },
                call_history={
                    "last_30_days": 5,
                    "year_total": 28,
                    "weekend_calls_ytd": 10,
                    "night_calls_ytd": 14,
                    "holiday_calls_ytd": 3,
                    "total_hours_ytd": 336,
                    "avg_shift_length": 12
                },
                bidding_stats={
                    "bids_placed": 15,
                    "bids_won": 9,
                    "avg_winning_bid": 2900,
                    "total_bidding_earnings": 26100,
                    "highest_bid": 3800,
                    "win_rate": 60.0,
                    "last_bid_date": "2025-08-31"
                },
                performance_metrics={
                    "satisfaction_score": 8.9,
                    "response_time_avg": "12 minutes",
                    "consultation_requests": 22,
                    "teaching_cases": 6,
                    "quality_score": 4.6,
                    "peer_rating": 4.7
                },
                contact_info={
                    "email": "j.park@hospital.com",
                    "phone": "555-0104",
                    "office": "IR Suite Control Room",
                    "emergency_contact": "555-0105"
                },
                availability_status="Available",
                current_location="Main Hospital"
            )
        ]

        self.locations = [
            Location(
                name="Main Hospital",
                address="123 Medical Center Dr",
                modalities=["CT", "MRI", "X-Ray", "Ultrasound", "Nuclear Medicine", "Mammography"],
                staffing_requirements={
                    "weekday_day": 3,
                    "weekday_night": 1,
                    "weekend_day": 2,
                    "weekend_night": 1
                },
                current_staff=["Dr. Chen", "Dr. Rodriguez", "Dr. Johnson", "Dr. Park"],
                equipment_status={
                    "CT_scanners": {"total": 4, "operational": 4, "utilization": 0.85},
                    "MRI_units": {"total": 3, "operational": 3, "utilization": 0.78},
                    "X-ray_rooms": {"total": 8, "operational": 7, "utilization": 0.65},
                    "Ultrasound_units": {"total": 6, "operational": 6, "utilization": 0.72},
                    "Nuclear_medicine": {"total": 2, "operational": 2, "utilization": 0.45}
                },
                operating_hours={
                    "weekday": "24/7",
                    "weekend": "24/7", 
                    "holiday": "24/7"
                },
                coordinates={"lat": 40.7128, "lng": -74.0060},
                capacity_metrics={
                    "daily_volume": 450,
                    "peak_hours": "08:00-18:00",
                    "avg_turnaround": "2.5 hours"
                }
            ),
            Location(
                name="Outpatient Center",
                address="456 Healthcare Blvd",
                modalities=["CT", "MRI", "X-Ray", "Ultrasound"],
                staffing_requirements={
                    "weekday_day": 2,
                    "weekday_night": 0,
                    "weekend_day": 1,
                    "weekend_night": 0
                },
                current_staff=["Dr. Chen", "Dr. Johnson"],
                equipment_status={
                    "CT_scanners": {"total": 2, "operational": 2, "utilization": 0.68},
                    "MRI_units": {"total": 1, "operational": 1, "utilization": 0.82},
                    "X-ray_rooms": {"total": 4, "operational": 4, "utilization": 0.55},
                    "Ultrasound_units": {"total": 3, "operational": 3, "utilization": 0.61}
                },
                operating_hours={
                    "weekday": "06:00-22:00",
                    "weekend": "08:00-18:00",
                    "holiday": "Closed"
                },
                coordinates={"lat": 40.7589, "lng": -73.9851},
                capacity_metrics={
                    "daily_volume": 180,
                    "peak_hours": "09:00-17:00",
                    "avg_turnaround": "1.8 hours"
                }
            ),
            Location(
                name="Sports Medicine Center",
                address="789 Athletic Way",
                modalities=["MRI", "X-Ray", "Ultrasound"],
                staffing_requirements={
                    "weekday_day": 1,
                    "weekday_night": 0,
                    "weekend_day": 1,
                    "weekend_night": 0
                },
                current_staff=["Dr. Rodriguez"],
                equipment_status={
                    "MRI_units": {"total": 1, "operational": 1, "utilization": 0.75},
                    "X-ray_rooms": {"total": 2, "operational": 2, "utilization": 0.58},
                    "Ultrasound_units": {"total": 2, "operational": 2, "utilization": 0.70}
                },
                operating_hours={
                    "weekday": "06:00-20:00",
                    "weekend": "08:00-16:00",
                    "holiday": "Closed"
                },
                coordinates={"lat": 40.7505, "lng": -73.9934},
                capacity_metrics={
                    "daily_volume": 85,
                    "peak_hours": "14:00-19:00",
                    "avg_turnaround": "1.2 hours"
                }
            ),
            Location(
                name="Pulmonary Center",
                address="321 Lung Health St",
                modalities=["CT", "X-Ray"],
                staffing_requirements={
                    "weekday_day": 1,
                    "weekday_night": 0,
                    "weekend_day": 0,
                    "weekend_night": 0
                },
                current_staff=["Dr. Johnson"],
                equipment_status={
                    "CT_scanners": {"total": 1, "operational": 1, "utilization": 0.65},
                    "X-ray_rooms": {"total": 2, "operational": 2, "utilization": 0.45}
                },
                operating_hours={
                    "weekday": "07:00-19:00",
                    "weekend": "Closed",
                    "holiday": "Closed"
                },
                coordinates={"lat": 40.7282, "lng": -73.9942},
                capacity_metrics={
                    "daily_volume": 65,
                    "peak_hours": "08:00-16:00",
                    "avg_turnaround": "1.5 hours"
                }
            )
        ]

        # Extended data for all other entities...
        # (Adding more comprehensive data structures)

        self.schedule_templates = [
            ScheduleTemplate(
                id="template_001",
                name="Standard Weekly Rotation",
                description="Balanced weekly schedule with fair distribution",
                template_type="weekly",
                assignments={
                    "monday_day": "Dr. Chen",
                    "monday_night": "Dr. Park",
                    "tuesday_day": "Dr. Rodriguez",
                    "tuesday_night": "Dr. Johnson",
                    # ... more assignments
                },
                created_by="System Administrator",
                created_date="2025-01-15",
                usage_count=24,
                last_used="2025-08-30"
            )
        ]

        # Rest of the data structures from previous implementation...
        # (Including all shifts, consultations, messages, etc.)

    # All the helper methods from previous implementation...
    def get_radiologist_by_name(self, name: str) -> Optional[Radiologist]:
        for rad in self.radiologists:
            if rad.name == name:
                return rad
        return None
class AppData:
    def __init__(self):
        self.radiologists = [
            # All your detailed Radiologist dataclasses (no truncation needed)
            # ... Paste the four already present dataclasses from your file here ...
        ]

        self.locations = [
            # Your four Location dataclasses as already provided
            # ... Paste all detailed Location entries here ...
        ]

        self.open_shifts = [
            OpenShift(
                id=1,
                date="2025-09-07",
                shift="Weekend Day",
                location="Main Hospital",
                subspecialty_required="Any",
                duration="12 hours",
                base_compensation=2400,
                assignment_mode="Smart Distribution",
                status="Open",
                assigned_radiologist=None
            ),
            OpenShift(
                id=2,
                date="2025-09-14",
                shift="Weekend Night",
                location="Outpatient Center",
                subspecialty_required="General",
                duration="12 hours",
                base_compensation=2600,
                assignment_mode="Bidding",
                status="Active Bidding",
                current_high_bid=2850,
                current_high_bidder="Dr. Michael Rodriguez"
            ),
        ]

        self.shift_swap_requests = [
            ShiftSwapRequest(
                id="SWAP-001",
                from_radiologist="Dr. Sarah Chen",
                to_radiologist="Dr. James Park",
                shift_date="2025-09-07",
                shift_type="Weekend Day",
                location="Main Hospital",
                reason="Family emergency",
                priority="High",
                status="Pending Approval",
                requested_timestamp="2025-08-30T14:30:00Z"
            ),
        ]

        self.consultations = [
            Consultation(
                id=1,
                case_id="RAD-2025-001",
                requesting_physician="Dr. Sarah Chen",
                specialty_needed="Interventional",
                urgency="High",
                description="Complex vascular malformation requiring intervention planning",
                status="Active",
                created="2025-08-31T10:30:00Z",
                patient_age=45,
                patient_gender="Female"
            ),
            Consultation(
                id=2,
                case_id="RAD-2025-002",
                requesting_physician="Dr. Emily Johnson",
                specialty_needed="Neuroradiology",
                urgency="Medium",
                description="Unusual white matter lesion pattern in young patient",
                status="Pending",
                created="2025-08-31T09:15:00Z",
                patient_age=28,
                patient_gender="Male"
            ),
        ]

        self.secure_messages = [
            SecureMessage(
                id=1,
                from_user="Dr. Michael Rodriguez",
                to_user="Dr. Sarah Chen",
                subject="Weekend coverage swap request",
                message="Can you cover my weekend shift? Family emergency.",
                timestamp="2025-08-31T08:45:00Z",
                priority="High",
                status="Unread"
            ),
        ]

        self.credentials = [
            CredentialRecord(
                radiologist_id=1,
                credential_type="Board Certification",
                issuing_body="American Board of Radiology",
                credential_number="ABR-NEURO-12345",
                issue_date="2016-03-15",
                expiry_date="2026-03-15",
                status="Active",
                cme_required=50,
                cme_credits=45
            ),
            CredentialRecord(
                radiologist_id=2,
                credential_type="Board Certification",
                issuing_body="American Board of Radiology",
                credential_number="ABR-MSK-23456",
                issue_date="2014-11-30",
                expiry_date="2025-11-30",
                status="Active",
                cme_required=50,
                cme_credits=38
            ),
        ]

        # Add more as needed...

    # Example helper method:
    def get_radiologist_by_name(self, name: str) -> Optional[Radiologist]:
        for rad in self.radiologists:
            if rad.name == name:
                return rad
        return None

    # Add more comprehensive methods...
