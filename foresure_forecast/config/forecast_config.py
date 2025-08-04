# forecast_config.py

"""
Forecast configuration generator for ForeSure-Forecast.
Automatically sets forecast parameters per SKU using smart default logic.
"""

def generate_forecast_config(sku_history, lead_time_days=7, reorder_cycle_days=7, category=None):
    """
    Generate forecast configuration for a given SKU using smart defaults.

    Parameters:
        sku_history (pd.DataFrame): Must contain 'qty_sold' and 'day_key'
        lead_time_days (int): Supplier lead time in days
        reorder_cycle_days (int): Days between planned reorders
        category (str): Optional product category to infer seasonality

    Returns:
        dict: Forecast configuration
    """

    # --- Forecast Grain (based on sales velocity) ---
    total_days = sku_history["qty_sold"].count()
    days_with_sales = sku_history["qty_sold"].gt(0).sum()
    velocity = days_with_sales / total_days if total_days > 0 else 0

    if velocity > 0.7:
        forecast_grain = "daily"
    elif velocity > 0.2:
        forecast_grain = "weekly"
    else:
        forecast_grain = "monthly"

    # --- Forecast Horizon (lead time + reorder buffer) ---
    horizon_days = lead_time_days + reorder_cycle_days

    # --- Seasonal Periods (based on category defaults) ---
    seasonal_defaults = {
        "grocery": 7,
        "apparel": 30,
        "toys": 90
    }
    seasonal_periods = seasonal_defaults.get(str(category).lower(), 7)

    # --- Allow TES if sufficient history exists ---
    allow_TES = len(sku_history) >= 2 * seasonal_periods

    # --- Allow DES by default ---
    allow_DES = True

    # --- Minimum Observations Required ---
    min_obs_required = {
        "SES": 5,
        "DES": 10,
        "TES": 2 * seasonal_periods
    }

    return {
        "forecast_grain": forecast_grain,
        "horizon_days": horizon_days,
        "seasonal_periods": seasonal_periods,
        "allow_TES": allow_TES,
        "allow_DES": allow_DES,
        "min_obs_required": min_obs_required
    }
