import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ==================================================
# PAGE CONFIG
# ==================================================
st.set_page_config(
    page_title="Local Food Wastage Management Dashboard",
    page_icon="🍲",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================
@st.cache_data
def load_data():

    providers = pd.read_csv("providers_data_cleaned.csv")
    receivers = pd.read_csv("receivers_data_cleaned.csv")
    listings = pd.read_csv("food_listings_data_cleaned.csv")
    claims = pd.read_csv("claims_data_cleaned.csv")

    listings["Expiry_Date"] = pd.to_datetime(
        listings["Expiry_Date"],
        errors="coerce"
    )

    claims["Timestamp"] = pd.to_datetime(
        claims["Timestamp"],
        errors="coerce"
    )

    return providers, receivers, listings, claims


providers, receivers, listings, claims = load_data()

# ==================================================
# SIDEBAR FILTERS
# ==================================================
st.sidebar.title("Filters")

provider_types = st.sidebar.multiselect(
    "Provider Type",
    providers["Type"].unique(),
    default=providers["Type"].unique()
)

food_types = st.sidebar.multiselect(
    "Food Type",
    listings["Food_Type"].unique(),
    default=listings["Food_Type"].unique()
)

claim_status = st.sidebar.multiselect(
    "Claim Status",
    claims["Status"].unique(),
    default=claims["Status"].unique()
)

# Filter datasets
providers_f = providers[
    providers["Type"].isin(provider_types)
]

listings_f = listings[
    listings["Food_Type"].isin(food_types)
]

claims_f = claims[
    claims["Status"].isin(claim_status)
]

# ==================================================
# TITLE
# ==================================================
st.title("🍲 Local Food Wastage Management Dashboard")

# ==================================================
# KPI SECTION
# ==================================================
total_providers = providers_f["Provider_ID"].nunique()
total_receivers = receivers["Receiver_ID"].nunique()
total_listings = listings_f["Food_ID"].nunique()
total_claims = claims_f["Claim_ID"].nunique()

food_quantity = listings_f["Quantity"].sum()

completed_claims = len(
    claims_f[claims_f["Status"] == "Completed"]
)

success_rate = round(
    completed_claims * 100 / total_claims,
    2
) if total_claims else 0

c1, c2, c3, c4, c5, c6 = st.columns(6)

c1.metric("Providers", total_providers)
c2.metric("Receivers", total_receivers)
c3.metric("Listings", total_listings)
c4.metric("Claims", total_claims)
c5.metric("Food Qty", f"{food_quantity:,}")
c6.metric("Success %", f"{success_rate}%")

# ==================================================
# ROW 1
# ==================================================
col1, col2, col3 = st.columns(3)

with col1:

    status_df = (
        claims_f["Status"]
        .value_counts()
        .reset_index()
    )

    status_df.columns = ["Status", "Count"]

    fig = px.pie(
        status_df,
        names="Status",
        values="Count",
        hole=0.6,
        title="Claims Status"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    provider_df = (
        providers_f["Type"]
        .value_counts()
        .reset_index()
    )

    provider_df.columns = ["Type", "Count"]

    fig = px.bar(
        provider_df,
        x="Type",
        y="Count",
        title="Provider Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col3:

    food_df = (
        listings_f["Food_Type"]
        .value_counts()
        .reset_index()
    )

    food_df.columns = ["Food Type", "Count"]

    fig = px.bar(
        food_df,
        x="Food Type",
        y="Count",
        title="Food Category Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==================================================
# ROW 2
# ==================================================
col4, col5, col6 = st.columns(3)

with col4:

    meal_df = (
        listings_f["Meal_Type"]
        .value_counts()
        .reset_index()
    )

    meal_df.columns = ["Meal", "Count"]

    fig = px.pie(
        meal_df,
        names="Meal",
        values="Count",
        title="Meal Type Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col5:

    receiver_df = (
        receivers["Type"]
        .value_counts()
        .reset_index()
    )

    receiver_df.columns = ["Receiver", "Count"]

    fig = px.bar(
        receiver_df,
        x="Receiver",
        y="Count",
        title="Receiver Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col6:

    city_df = (
        providers["City"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    city_df.columns = ["City", "Providers"]

    fig = px.bar(
        city_df,
        x="Providers",
        y="City",
        orientation="h",
        title="Top Provider Cities"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==================================================
# TRENDS
# ==================================================
st.subheader("Trend Analysis")

t1, t2 = st.columns(2)

with t1:

    monthly_claims = (
        claims.groupby("Month")
        .size()
        .reset_index(name="Claims")
        .sort_values("Month")
    )

    fig = px.line(
        monthly_claims,
        x="Month",
        y="Claims",
        markers=True,
        title="Monthly Claims Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

with t2:

    listings_month = listings.copy()

    listings_month["Month"] = (
        listings_month["Expiry_Date"]
        .dt.month
    )

    monthly_listing = (
        listings_month.groupby("Month")
        .size()
        .reset_index(name="Listings")
        .sort_values("Month")
    )

    fig = px.line(
        monthly_listing,
        x="Month",
        y="Listings",
        markers=True,
        title="Monthly Listings Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

# ==================================================
# PERFORMANCE TABLES
# ==================================================
st.subheader("Performance Insights")

p1, p2 = st.columns(2)

with p1:

    top_providers = (
        listings.groupby("Provider_ID")
        .agg(Listings=("Food_ID", "count"))
        .reset_index()
        .sort_values(
            "Listings",
            ascending=False
        )
        .head(10)
    )

    top_providers = top_providers.merge(
        providers[
            ["Provider_ID", "Name"]
        ],
        on="Provider_ID",
        how="left"
    )

    st.markdown("### Top Providers")
    st.dataframe(
        top_providers[
            ["Name", "Listings"]
        ],
        use_container_width=True
    )

with p2:

    top_receivers = (
        claims.groupby("Receiver_ID")
        .agg(Claims=("Claim_ID", "count"))
        .reset_index()
        .sort_values(
            "Claims",
            ascending=False
        )
        .head(10)
    )

    top_receivers = top_receivers.merge(
        receivers[
            ["Receiver_ID", "Name"]
        ],
        on="Receiver_ID",
        how="left"
    )

    st.markdown("### Top Receivers")

    st.dataframe(
        top_receivers[
            ["Name", "Claims"]
        ],
        use_container_width=True
    )

# ==================================================
# FOOD INSIGHTS
# ==================================================
st.subheader("Food Insights")

food_claims = claims.merge(
    listings[
        ["Food_ID", "Food_Name"]
    ],
    on="Food_ID"
)

top_foods = (
    food_claims["Food_Name"]
    .value_counts()
    .head(15)
    .reset_index()
)

top_foods.columns = [
    "Food Item",
    "Claims"
]

fig = px.bar(
    top_foods,
    x="Claims",
    y="Food Item",
    orientation="h",
    title="Most Claimed Food Items"
)

st.plotly_chart(
    fig,
    use_container_width=True
) 