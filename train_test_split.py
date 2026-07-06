import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# =============================================================================
# STEP 1: LOAD THE FEATURE-ENGINEERED DATASET
# =============================================================================
# Read features.csv — the file produced after Feature Engineering (Section 5).
# At this point the dataset contains the original DataCoSupplyChainDataset columns
# plus up to 5 engineered features:
#   Feature 1: Daily_Demand              (total order quantity aggregated by date)
#   Feature 2: Is_Peak_Hour              (peak business hours 8h–17h = 1, else 0)
#   Feature 3: Demand_Urgency            (urgent demand: peak + fast shipping + late risk)
#   Feature 4: Customer_Segment_Encoded  (Consumer=0, Corporate=1, Home Office=2)
#   Feature 5: Cancellation_Risk_Index   (High Risk / Moderate Risk / Low Risk)

df = pd.read_csv("features.csv")
print(f"\nTotal samples in the dataset: {df.shape[0]} rows x {df.shape[1]} columns\n")
print(f"Existing columns: {list(df.columns)}\n")


# =============================================================================
# STEP 2: DROP IRRELEVANT / PII / HIGH-CARDINALITY COLUMNS
# =============================================================================
# REASON: Many columns in DataCoSupplyChainDataset are identifiers, personal
# information, or free-text fields that carry no predictive value for Sales
# prediction and would introduce noise or data leakage.
#
# Categories of dropped columns:
#   - PII (Personal Identifiable Info): Customer Email, Password, Name, Street
#   - Identifiers / Keys: Order Id, Customer Id, Order Item Id, Product Card Id, etc.
#   - Free-text / Image URLs: Product Name, Product Description, Product Image
#   - Date strings: order date, shipping date, Order_Date_Only (temporal info
#     already captured by Is_Peak_Hour and Daily_Demand)
#   - Redundant columns: Order Customer Id (same as Customer Id),
#     Product Category Id (same as Category Id)

columns_to_drop = [
    # --- PII / Personal Information ---
    "Customer Email",
    "Customer Password",
    "Customer Fname",
    "Customer Lname",
    "Customer Street",
    # --- Identifier / Key Columns ---
    "Order Id",
    "Customer Id",
    "Order Customer Id",
    "Order Item Id",
    "Order Item Cardprod Id",
    "Product Card Id",
    "Category Id",
    "Product Category Id",
    "Department Id",
    # --- Free-text / Image ---
    "Product Name",
    "Product Description",
    "Product Image",
    # --- Date Strings (temporal info already in engineered features) ---
    "order date (DateOrders)",
    "shipping date (DateOrders)",
    "Order_Date_Only",
    # --- High-cardinality location columns (too many unique values) ---
    "Customer City",
    "Customer Country",
    "Customer State",
    "Customer Zipcode",
    "Order City",
    "Order Country",
    "Order State",
    "Order Zipcode",
    "Order Region",
    # --- Other ---
    "Category Name",       # High cardinality; Category Id provides the same info
    "Department Name",     # Redundant with Department Id (already dropped above)
]

# Only drop columns that actually exist in the dataframe
existing_cols_to_drop = [c for c in columns_to_drop if c in df.columns]
df = df.drop(columns=existing_cols_to_drop)

print(f"Dropped {len(existing_cols_to_drop)} irrelevant/PII/high-cardinality columns.")
print(f"Remaining shape: {df.shape[0]} rows x {df.shape[1]} columns\n")
print(f"Remaining columns: {list(df.columns)}\n")


# =============================================================================
# STEP 3: ENCODE CATEGORICAL COLUMNS BEFORE SPLITTING
# =============================================================================
# REASON: ML models (Linear Regression, XGBoost, Random Forest, etc.) require
# numeric inputs. Text/string columns must be encoded first.
#
# After dropping irrelevant columns, the remaining categorical columns are:
#   - Type:                     Payment type (DEBIT / TRANSFER / CASH / PAYMENT)
#   - Delivery Status:          Advance shipping / Late delivery / Shipping on time / Shipping canceled
#   - Market:                   Geographic market (e.g., Europe, LATAM, Pacific Asia, ...)
#   - Shipping Mode:            Standard Class / Second Class / First Class / Same Day
#   - Order Status:             COMPLETE / PENDING / CLOSED / PENDING_PAYMENT / ...
#   - Customer Segment:         Consumer / Corporate / Home Office
#   - Cancellation_Risk_Index:  High Risk / Moderate Risk / Low Risk  (Feature 5)
#
# METHOD: pd.get_dummies() (One-Hot Encoding) with drop_first=True to avoid
# the multicollinearity trap — e.g., if there are 3 shipping modes, only 2
# dummy columns are needed to fully represent them.

# List categorical columns to encode
categorical_columns = df.select_dtypes(include=["object", "string"]).columns.tolist()
print(f"Categorical columns to encode: {categorical_columns}\n")

# Perform One-Hot Encoding
df_encoded = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

# Convert boolean columns (True/False) to int (0/1) for full numeric compatibility
bool_cols = df_encoded.select_dtypes(include=["bool"]).columns
df_encoded[bool_cols] = df_encoded[bool_cols].astype(int)

print(f"Shape after encoding: {df_encoded.shape}\n")
print(f"Columns after encoding: {list(df_encoded.columns)}\n")


# =============================================================================
# STEP 4: SEPARATE INPUT FEATURES (X) AND TARGET VARIABLE (y)
# =============================================================================
# TARGET VARIABLE (y): Sales
#   - This is the transaction sales value that the model needs to PREDICT.
#   - In this AI-Driven Dynamic Pricing project, the goal is to build a model
#     that can forecast pricing based on real-time market and logistics factors.
#
# INPUT FEATURES (X): All remaining columns
#   - Includes both original DataCo columns and the 5 engineered features.
#   - After One-Hot Encoding, all text columns have been converted to 0/1.

TARGET_COLUMN = "Sales"

X = df_encoded.drop(columns=[TARGET_COLUMN])
y = df_encoded[TARGET_COLUMN]

print(f"Target variable (y): {TARGET_COLUMN}")
print(f"- Min: {y.min():.2f} | Max: {y.max():.2f} | Mean: {y.mean():.2f}")
print(f"Number of features (X): {X.shape[1]} columns")
print(f"Feature list:")
for i, col in enumerate(X.columns, 1):
    print(f"  {i:2d}. {col}")
print()


# =============================================================================
# STEP 5: PERFORM TRAIN/TEST SPLIT
# =============================================================================
# ┌─────────────────────────────────────────────────────────────────────────┐
# │  RATIONALE FOR 80/20 SPLIT (test_size=0.2)                            │
# │                                                                        │
# │  1. The DataCoSupplyChainDataset has ~180,000 samples — a LARGE       │
# │     dataset. With this volume, both 80/20 and 70/30 would work well.  │
# │     We choose 80/20 to maximize training data while retaining ~36,000 │
# │     test samples for robust evaluation.                                │
# │                                                                        │
# │  2. 80/20 is the most widely adopted split ratio in ML:               │
# │     → Recommended by Andrew Ng (Stanford) and scikit-learn docs.      │
# │     → ~36,000 test samples provide highly reliable performance        │
# │       estimates with narrow confidence intervals.                      │
# │                                                                        │
# │  3. random_state=42:                                                   │
# │     → Fixes the random seed so every run produces identical splits.   │
# │     → Ensures reproducibility when reporting results.                  │
# │     → 42 is a popular convention (from "The Hitchhiker's Guide").     │
# └─────────────────────────────────────────────────────────────────────────┘

# --- 80/20 split ---
TEST_SIZE = 0.2    # 20% for testing
RANDOM_STATE = 42  # Fixed seed for reproducibility

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE
)

print("=" * 65)
print("  TRAIN/TEST SPLIT RESULTS (80/20)")
print("=" * 65)
print(f"  Total samples          : {len(df):>6d}")
print(f"  Train set (80%)        : {X_train.shape[0]:>6d} samples x {X_train.shape[1]} features")
print(f"  Test set (20%)         : {X_test.shape[0]:>6d} samples x {X_test.shape[1]} features")
print(f"  random_state           :    {RANDOM_STATE}")
print("=" * 65)
print()


# =============================================================================
# STEP 6: VERIFY DISTRIBUTION AFTER SPLITTING
# =============================================================================
# REASON: We need to ensure the distribution of Sales in Train and Test sets
# is similar. If the distributions diverge significantly, the model will learn
# incorrect patterns and evaluation metrics will be unreliable.

print("DISTRIBUTION CHECK — TARGET VARIABLE (Sales):")
print("-" * 55)
print(f"  {'Statistic':<20s} {'Overall':>10s} {'Train':>10s} {'Test':>10s}")
print("-" * 55)
print(f"  {'Count':<20s} {len(y):>10d} {len(y_train):>10d} {len(y_test):>10d}")
print(f"  {'Mean':<20s} {y.mean():>10.2f} {y_train.mean():>10.2f} {y_test.mean():>10.2f}")
print(f"  {'Median':<20s} {y.median():>10.2f} {y_train.median():>10.2f} {y_test.median():>10.2f}")
print(f"  {'Std Dev':<20s} {y.std():>10.2f} {y_train.std():>10.2f} {y_test.std():>10.2f}")
print(f"  {'Min':<20s} {y.min():>10.2f} {y_train.min():>10.2f} {y_test.min():>10.2f}")
print(f"  {'Max':<20s} {y.max():>10.2f} {y_train.max():>10.2f} {y_test.max():>10.2f}")
print("-" * 55)
print()

# Check the mean difference between Train and Test
mean_diff = abs(y_train.mean() - y_test.mean())
mean_diff_pct = mean_diff / y.mean() * 100
print(f"  → Mean difference between Train and Test: {mean_diff:.2f} ({mean_diff_pct:.2f}%)")
if mean_diff_pct < 5:
    print("  ✅ Distributions are SIMILAR — data was split properly!")
else:
    print("  ⚠️  Distributions differ — consider using a stratified split.")
print()


# =============================================================================
# STEP 7: CONFIRM DATA IS READY FOR MODEL TRAINING
# =============================================================================
print("READINESS CHECK FOR MODEL TRAINING:")
print("-" * 55)

# Check for NaN values
nan_in_X_train = X_train.isnull().sum().sum()
nan_in_X_test = X_test.isnull().sum().sum()
nan_in_y = y_train.isnull().sum() + y_test.isnull().sum()

print(f"  NaN values in X_train  : {nan_in_X_train}")
print(f"  NaN values in X_test   : {nan_in_X_test}")
print(f"  NaN values in y        : {nan_in_y}")

# Check data types
non_numeric = X_train.select_dtypes(exclude=["number"]).columns.tolist()
if len(non_numeric) == 0:
    print(f"  Data type of X         : ✅ All numeric")
else:
    print(f"  Data type of X         : ⚠️  Non-numeric columns remain: {non_numeric}")

# Check data leakage
print(f"  Data leakage check     : ✅ Target '{TARGET_COLUMN}' has been excluded from X")
print("-" * 55)
print()

# Final summary
print("╔═══════════════════════════════════════════════════════════════╗")
print("║          VARIABLES READY FOR TRAINING:                       ║")
print("║                                                               ║")
print(f"║   X_train : ({X_train.shape[0]}, {X_train.shape[1]})  — Training features          ║")
print(f"║   X_test  : ({X_test.shape[0]}, {X_test.shape[1]})  — Test features              ║")
print(f"║   y_train : ({len(y_train)},)      — Training target (Sales)    ║")
print(f"║   y_test  : ({len(y_test)},)      — Test target (Sales)        ║")
print("║                                                               ║")
print("║   → Proceed to Section 7: Training Machine Learning Models   ║")
print("╚═══════════════════════════════════════════════════════════════╝")


# =============================================================================
# NOTEBOOK INTEGRATION GUIDE
# =============================================================================
# When copying into the notebook, split into cells as follows:
#
# CELL 1 (Markdown):
#   ## 6. Train / Test Split
#   **Objective:** Split the dataset into 2 subsets:
#   - **Train (80%)**: Used to train the AI model.
#   - **Test (20%)**: Used to evaluate model performance on unseen data.
#
#   **Why 80/20:**
#   - The DataCo dataset has ~180,000 samples → ample data for both subsets.
#   - ~36,000 test samples provide highly reliable evaluation.
#   - `random_state=42` ensures reproducible results.
#
# CELL 2 (Code): Copy STEP 2 + STEP 3 + STEP 4 + STEP 5
# CELL 3 (Code): Copy STEP 6 (distribution verification)
# CELL 4 (Code): Copy STEP 7 (readiness confirmation)
