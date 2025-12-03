# app/handlers/__init__.py
from .start import router as start_router
from .kpi import router as kpi_router
from .monitoring import router as monitoring_router

__all__ = ["start_router", "kpi_router", "monitoring_router"]