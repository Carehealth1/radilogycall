
"""
Data models and sample data for RadFlow Pro Streamlit application
"""

from dataclasses import dataclass
from typing import List, Dict, Optional
from datetime import datetime, timedelta
import json

@dataclass
class Radiologist:
    id: int
    name: str
    subspecialty: str
    locations: List[str]
    credentials: Dict
    preferences: Dict
    call_history: Dict
    bidding_stats: Dict

@dataclass
class Location:
    name: str
    address: str
    modalities: List[str]
    staffing_requirements: Dict

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
    bid_history: Optional[List[Dict]] = None

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
                    "cme_required": 50
                },
                preferences={
                    "max_weekend_calls": 2,
                    "preferred_locations": ["Main Hospital"],
                    "blackout_dates": ["2025-12-20", "2025-12-27"],
                    "bidding_opt_in": True,
                    "max_auto_bid": 2800,
                    "preferred_assignment_mode": "Smart Distribution"
                },
                call_history={
                    "last_30_days": 4,
                    "year_total": 24
                },
                bidding_stats={
                    "bids_placed": 8,
                    "bids_won": 5,
                    "avg_winning_bid": 2650,
                    "total_bidding_earnings": 13250
                }
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
                    "cme_required": 50
                },
                preferences={
                    "max_weekend_calls": 3,
                    "preferred_locations": ["Sports Medicine Center"],
                    "blackout_dates": ["2025-10-15", "2025-11-22"],
                    "bidding_opt_in": True,
                    "max_auto_bid": 3000,
                    "preferred_assignment_mode": "Either"
                },
                call_history={
                    "last_30_days": 6,
                    "year_total": 32
                },
                bidding_stats={
                    "bids_placed": 12,
                    "bids_won": 7,
                    "avg_winning_bid": 2750,
                    "total_bidding_earnings": 19250
                }
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
                    "cme_required": 50
                },
                preferences={
                    "max_weekend_calls": 2,
                    "preferred_locations": ["Pulmonary Center"],
                    "blackout_dates": ["2025-09-10", "2025-12-25"],
                    "bidding_opt_in": False,
                    "max_auto_bid": 0,
                    "preferred_assignment_mode": "Smart Distribution Only"
                },
                call_history={
                    "last_30_days": 3,
                    "year_total": 18
                },
                bidding_stats={
                    "bids_placed": 0,
                    "bids_won": 0,
                    "avg_winning_bid": 0,
                    "total_bidding_earnings": 0
                }
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
                    "cme_required": 50
                },
                preferences={
                    "max_weekend_calls": 4,
                    "preferred_locations": ["Main Hospital"],
                    "blackout_dates": ["2025-11-15"],
                    "bidding_opt_in": True,
                    "max_auto_bid": 3200,
                    "preferred_assignment_mode": "Bidding Preferred"
                },
                call_history={
                    "last_30_days": 5,
                    "year_total": 28
                },
                bidding_stats={
                    "bids_placed": 15,
                    "bids_won": 9,
                    "avg_winning_bid": 2900,
                    "total_bidding_earnings": 26100
                }
            )
        ]

        self.locations = [
            Location(
                name="Main Hospital",
                address="123 Medical Center Dr",
                modalities=["CT", "MRI", "X-Ray", "Ultrasound", "Nuclear Medicine"],
                staffing_requirements={
                    "weekday_day": 3,
                    "weekday_night": 1,
                    "weekend_day": 2,
                    "weekend_night": 1
                }
            ),
            Location(
                name="Outpatient Center",
                address="456 Healthcare Blvd",
                modalities=["CT", "MRI", "X-Ray"],
                staffing_requirements={
                    "weekday_day": 2,
                    "weekday_night": 0,
                    "weekend_day": 1,
                    "weekend_night": 0
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
                }
            )
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
                status="Open"
            ),
            OpenShift(
                id=2,
                date="2025-09-14",
                shift="Weekend Night",
                location="Outpatient Center",
                subspecialty_required="General",
                duration="12 hours",
                base_compensation=2600,
                assignment_mode="Bidding Mode",
                status="Active Bidding",
                current_high_bid=2850,
                current_high_bidder="Dr. Michael Rodriguez",
                bid_history=[
                    {"radiologist": "Dr. James Park", "amount": 2700, "timestamp": "2025-08-31T14:30:00Z"},
                    {"radiologist": "Dr. Michael Rodriguez", "amount": 2850, "timestamp": "2025-08-31T16:15:00Z"}
                ]
            )
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
                created="2025-08-31T10:30:00Z"
            ),
            Consultation(
                id=2,
                case_id="RAD-2025-002",
                requesting_physician="Dr. Emily Johnson",
                specialty_needed="Neuroradiology",
                urgency="Medium",
                description="Unusual white matter lesion pattern in young patient",
                status="Pending",
                created="2025-08-31T09:15:00Z"
            )
        ]

        self.department_settings = {
            "default_assignment_mode": "Smart Distribution",
            "allow_mode_override": True,
            "bidding_rules": {
                "min_bid_weekend_day": 2200,
                "min_bid_weekend_night": 2400,
                "max_bid_limit": 4000,
                "bid_increment": 50,
                "default_bidding_time": 24,
                "auto_close_if_no_bids": True,
                "cascade_to_bidding": True,
                "cascade_timeout_hours": 12
            },
            "cost_control": {
                "monthly_bidding_budget": 50000,
                "approval_required_over": 3500,
                "cost_alert_threshold": 3000
            }
        }

        self.analytics_data = {
            "monthly_comparison": {
                "smart_distribution": {
                    "shifts_filled": 24,
                    "avg_cost": 2450,
                    "avg_time_to_fill": "2.3 hours",
                    "total_cost": 58800
                },
                "bidding_mode": {
                    "shifts_filled": 8,
                    "avg_cost": 2780,
                    "avg_time_to_fill": "18.5 hours",
                    "total_cost": 22240
                }
            },
            "cost_trends": [
                {"month": "June", "smart_avg": 2420, "bidding_avg": 2650},
                {"month": "July", "smart_avg": 2435, "bidding_avg": 2720},
                {"month": "August", "smart_avg": 2450, "bidding_avg": 2780}
            ],
            "participation_rates": {
                "smart_distribution_acceptance": 92,
                "bidding_participation": 78,
                "hybrid_success_rate": 96
            }
        }

    def get_radiologist_by_name(self, name: str) -> Optional[Radiologist]:
        for rad in self.radiologists:
            if rad.name == name:
                return rad
        return None

    def get_active_bidding_shifts(self) -> List[OpenShift]:
        return [shift for shift in self.open_shifts if "Bidding" in shift.status]

    def get_open_shifts_by_mode(self, mode: str) -> List[OpenShift]:
        return [shift for shift in self.open_shifts if mode.lower() in shift.assignment_mode.lower()]
