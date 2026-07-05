import streamlit as st
import pandas as pd
# Load dataset
df = pd.read_csv("train.csv")
# Page Configuration
st.set_page_config(
    page_title="Sales Forecasting & Demand Intelligence System",
    page_icon="📊",
    layout="wide"
)

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Home",
        "Dataset Overview",
        "Forecasting",
        "Anomaly Detection",
        "Product Clustering",
        "About"
    ]
)

# ---------------- HOME ----------------

if page == "Home":

    st.title("📊 Sales Forecasting & Demand Intelligence System")

    st.markdown("""
    ### Internship Project

    This dashboard presents the results of an end-to-end sales forecasting and demand intelligence project.

    #### Features
    - Exploratory Data Analysis
    - Sales Forecasting
    - Category & Region Forecasting
    - Anomaly Detection
    - Product Clustering
    """)

# ---------------- DATASET ----------------

elif page == "Dataset Overview":

    st.title("📁 Dataset Overview")

    # KPIs
    total_sales = df["Sales"].sum()
    total_orders = len(df)
    total_products = df["Product Name"].nunique()
    total_categories = df["Category"].nunique()
    total_regions = df["Region"].nunique()

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Total Sales", f"${total_sales:,.2f}")
    col2.metric("Orders", total_orders)
    col3.metric("Products", total_products)
    col4.metric("Categories", total_categories)
    col5.metric("Regions", total_regions)

    st.markdown("---")

    st.subheader("Dataset Preview")

    st.dataframe(df.head(10), use_container_width=True)

# ---------------- FORECASTING ----------------

elif page == "Forecasting":

    st.title("🔮 Sales Forecasting")

    st.markdown("""
    This section compares the forecasting performance of different machine learning and time series models.
    """)

    st.subheader("SARIMA Forecast")

    st.image(
        "charts/sarima_forecast.png",
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("Prophet Forecast")

    st.image(
        "charts/prophet_forecast.png",
        use_container_width=True
    )

    st.markdown("---")

    st.subheader("XGBoost Forecast")

    st.image(
        "charts/xgboost_forecast.png",
        use_container_width=True
    )

# ---------------- ANOMALY ----------------

elif page == "Anomaly Detection":

    st.title("🚨 Sales Anomaly Detection")

    st.markdown("""
    This section identifies unusual sales patterns using two anomaly detection techniques.
    """)

    # Z-Score
    st.subheader("1. Z-Score Based Anomaly Detection")

    st.image(
        "charts/zscore_anomalies.png",
        use_container_width=True
    )

    st.success(
        "The Z-Score method detected extreme monthly sales values that significantly deviate from the overall sales distribution."
    )

    st.markdown("---")

    # Isolation Forest
    st.subheader("2. Isolation Forest Based Anomaly Detection")

    st.image(
        "charts/isolation_forest_anomalies.png",
        use_container_width=True
    )

    st.success(
        "Isolation Forest identified both unusually high and unusually low sales months by isolating observations that differ from the majority of the data."
    )

# ---------------- CLUSTERING ----------------

elif page == "Product Clustering":

    st.title("📦 Product Clustering & Demand Segmentation")

    st.markdown("""
    Products are grouped into different demand segments using the K-Means clustering algorithm.
    """)

    # Elbow Method
    st.subheader("Optimal Number of Clusters (Elbow Method)")

    st.image(
        "charts/elbow_method.png",
        use_container_width=True
    )

    st.info(
        "The elbow curve indicates that **4 clusters** provide a good balance between model complexity and clustering performance."
    )

    st.markdown("---")

    # Cluster Visualization
    st.subheader("K-Means Cluster Visualization")

    st.image(
        "charts/product_clusters.png",
        use_container_width=True
    )

    st.success("""
    **Cluster Summary**

    • Cluster 0 → Low demand products

    • Cluster 1 → Medium demand products

    • Cluster 2 → High demand products

    • Cluster 3 → Premium / Best-selling products
    """)

# ---------------- ABOUT ----------------

elif page == "About":

    st.title("👨‍💻 About This Project")

    st.markdown("""
## End-to-End Sales Forecasting & Demand Intelligence System

### Objective

Develop an intelligent system capable of:

- Forecasting future sales
- Detecting unusual sales patterns
- Segmenting products based on demand
- Presenting insights through an interactive dashboard

---

### Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-Learn
- Statsmodels (SARIMA)
- Prophet
- XGBoost
- Streamlit

---

### Developed By

**Parv Sharma**

AI & Data Science Internship Project
""")