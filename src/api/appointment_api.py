from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Optional
from datetime import datetime, date

from config.database import get_db
from src.models.appointment import Appointment, AppointmentCreate, AppointmentUpdate
from src.core.appointment_scheduler import AppointmentScheduler

router = APIRouter()


@router.post("/", response_model=dict)
async def create_appointment(
    appointment_data: AppointmentCreate,
    db: AsyncSession = Depends(get_db)
):
    """Create a new appointment"""
    try:
        scheduler = AppointmentScheduler(db)
        appointment = await scheduler.create_appointment(appointment_data)
        return {"status": "success", "appointment_id": appointment.id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/", response_model=List[dict])
async def get_appointments(
    date_from: Optional[date] = None,
    date_to: Optional[date