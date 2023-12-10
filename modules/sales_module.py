# Revenue Growth
def revenue_growth(current_year_total_revenue, last_year_total_revenue):
    return ((current_year_total_revenue - last_year_total_revenue) / last_year_total_revenue) * 100

# Customer Retention Rate (EE)
def customer_retention_rate(current_customers, lost_customers, prior_year_customers):
    return ((current_customers - lost_customers) / prior_year_customers) * 100

# Renewal Rate EN
def renewal_rate_en(renewals_on_time, total_current_customers):
    return (renewals_on_time / total_current_customers) * 100
    
# Growth Rate of New Customers
def en_growth_rate(en_revenue_current_year, en_revenue_prior_year):
    growth_rate = ((en_revenue_current_year - en_revenue_prior_year) / en_revenue_prior_year) * 100
    if growth_rate <= 25:
        return "Growth rate <= 25%", growth_rate
    elif growth_rate <= 50:
        return "Growth rate up to 50%", growth_rate
    else:
        return "Growth rate > 50%", growth_rate
    
# No. of Customers Acquired
def nn_customers_acquired(nn_customers, total_revenue):
    return (nn_customers / total_revenue) * 100

# Renewal Rate
def renewal_rate(renewals_on_time, total_current_customers):
    return (renewals_on_time / total_current_customers) * 100

# Customer Retention Rate
def retention_rate(current_customers, prior_year_customers):
    return (current_customers / prior_year_customers) * 100

# Churn Rate
def churn_rate(customers_lost, prior_year_customers):
    return (customers_lost / prior_year_customers) * 100

# Win Rate
def win_rate(bids_won, bids_submitted):
    return (bids_won / bids_submitted) * 100

# Funnel Quality
def funnel_quality(qualified_pipeline, total_pipeline):
    return (qualified_pipeline / total_pipeline) * 100

# Revenue Conversion Rate
def revenue_conversion_rate(bookings, qualified_pipeline):
    return (bookings / qualified_pipeline) * 100

# Pipeline Quality
def pipeline_quality(qualified_pipeline, total_pipeline):
    return (qualified_pipeline / total_pipeline) * 100

# Bill to Book Ratio
def bill_to_book_ratio(new_revenue_billed, new_revenue_booked):
    return new_revenue_billed / new_revenue_booked

# Average Cost of Sales Staff
def avg_cost_of_sales_staff(sga_cost, total_staff_fte):
    return sga_cost / total_staff_fte

# Anticipated LTV
def anticipated_ltv(total_revenue, total_customers):
    return total_revenue / total_customers

# CAC of EN ROI
def cac_en_roi(en_revenue, en_cac):
    return en_revenue / en_cac

# CAC of NN ROI
def cac_nn_roi(nn_revenue, nn_cac):
    return nn_revenue / nn_cac
