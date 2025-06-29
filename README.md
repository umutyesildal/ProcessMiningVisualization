# 🎻 Process Mining Violin Plot Visualization Dashboard

**Interactive visualization of event type distributions over time using violin charts for comprehensive process mining analysis**

![Process Mining](https://img.shields.io/badge/Process%20Mining-Violin%20Plots-blue)
![Python](https://img.shi### 🔮 Future Enhancements

### 📈 **Planned Features**
- [ ] **Multi-dataset Support**: Easy switching between Traffic Fines, BPI 2012, and Sepsis datasets
- [ ] **Export Functionality**: Save plots and statistical reports
- [ ] **Advanced Filtering**: Date ranges, case attributes, custom event exclusions
- [ ] **Comparison Mode**: Side-by-side dataset comparison
- [ ] **Statistical Testing**: Automated distribution analysis across datasets
- [ ] **Custom Event Filtering**: User-defined event inclusion/exclusion rules

### 🛠️ **Technical Roadmap**
- [ ] **Dynamic Dataset Loading**: Runtime dataset switching
- [ ] **Database Integration**: Direct connection to process mining tools
- [ ] **API Endpoints**: Programmatic access to transformations
- [ ] **Custom Transformations**: User-defined transformation formulas
- [ ] **Batch Processing**: Analyze multiple datasets simultaneouslyPython-3.8+-green)
![Dash](https://img.shields.io/badge/Framework-Dash-red)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)
![Datasets](https://img.shields.io/badge/Datasets-3%20BPI%20Logs-orange)

---

## 📊 Overview

This interactive dashboard transforms process mining event logs into meaningful violin plot visualizations, revealing temporal patterns and distributions in business processes. The dashboard supports **multiple BPI Challenge datasets** and focuses on analyzing event time distributions with advanced filtering and transformation capabilities.

### 🎯 Key Features

- **🎻 Interactive Violin Plots** - Visualize event time distributions with box plots overlay
- **🔄 Multiple Transformations** - 7 different time transformation methods
- **📊 Dynamic Sorting** - Sort events by statistical measures (frequency, mean, median, quartiles)
- **📱 Responsive Design** - Modern, mobile-friendly interface
- **⚡ Real-time Updates** - Instant visualization updates based on user selections
- **🎨 Professional UI** - Clean, dashboard-style interface with visual hierarchy
- **🧹 Smart Filtering** - Automatically excludes case-start events for meaningful temporal analysis

---

## 📈 Multi-Dataset Support

### 🚗 Road Traffic Fine Management Process *(Currently Active)*
Process mining log from Italian traffic fine management system:

| **Metric** | **Value** |
|------------|-----------|
| 📁 **Total Cases** | 150,370 |
| 📊 **Total Events** | 561,470 |
| 🏷️ **Event Types** | 11 unique types |
| ⏱️ **Time Range** | 0 - 4,372 days |
| 📅 **Average Process Duration** | 148 days |
| 📍 **Median Process Duration** | 84 days |

### 🏦 BPI Challenge 2012 *(Available)*
Loan application process from a Dutch financial institute:

| **Metric** | **Value** |
|------------|-----------|
| � **Total Cases** | 13,087 |
| 📊 **Total Events** | ~262K |
| 🏷️ **Event Types** | 23 unique types |
| ⏱️ **Process Focus** | Loan applications |
| 📅 **Temporal Range** | Multi-month processes |

### 🏥 Sepsis Cases *(Available)*
Hospital patient treatment process for sepsis management:

| **Metric** | **Value** |
|------------|-----------|
| 📁 **Total Cases** | 1,050 |
| 📊 **Total Events** | ~15K |
| 🏷️ **Event Types** | 16 unique types |
| ⏱️ **Process Focus** | Medical treatment |
| 📅 **Temporal Range** | Hours to days |

---

## 🔍 Intelligent Event Filtering

### 🚫 **Case Start Event Exclusion**
The dashboard automatically **excludes case-start events** (time = 0) from visualizations:

| **Dataset** | **Excluded Events** | **Reason** |
|-------------|---------------------|-------------|
| **Traffic Fines** | "Create Fine" (150K events) | Always at time 0 |
| **BPI 2012** | "A_SUBMITTED" (13K events) | Case initiation |
| **Sepsis** | "ER Registration" (1K events) | Patient admission |

### 📊 **Focused Analysis Results**
After filtering, the dashboard shows **meaningful temporal events**:

#### 🚗 Traffic Fines - Top Temporal Events
| **Event Type** | **Count** | **Description** |
|----------------|-----------|-----------------|
| 📤 **Send Fine** | 101,093 | Fine notification sent |
| ⚠️ **Add penalty** | 79,860 | Penalty addition |
| 📝 **Insert Fine Notification** | 77,133 | Notification processing |
| 💰 **Payment** | 72,781 | Fine payment received |

---

## 🔄 Transformation Methods

The dashboard supports multiple time transformation approaches to reveal different patterns in the data:

### 📊 **Logarithmic Transformation** *(Default)*
- **Use Case**: Highly skewed data where most events cluster early
- **Best For**: Traffic fines (most payments happen quickly, few very late)
- **Formula**: `log(hours + 1)`
- **Advantage**: Compresses outliers, reveals distribution shape

### 🕐 **Raw Time Transformations**
| **Type** | **Unit** | **Best For** | **Display** |
|----------|----------|--------------|-------------|
| Hours | Original | Short processes | Decimal precision |
| Days | /24 | Multi-day processes | Decimal precision |
| Weeks | /168 | Long processes | 1 decimal place |
| Months | /730.5 | Very long processes | **Whole numbers** |

### ⚗️ **Advanced Transformations**
- **√ Square Root**: Gentler compression than log, preserves moderate skew
- **📏 Min-Max Scaling**: Normalizes to 0-1 range for cross-process comparison

---

## 🔬 Research Approach & Methodology

### 📚 Background
Process mining event logs exhibit distinct temporal characteristics requiring specialized analysis:

#### ⚠️ **The Case Start Problem**
- **Case-start events** (Create Fine, A_SUBMITTED, ER Registration) always occur at `time_since_case_start = 0`
- These events provide **no temporal insights** for time-based analysis
- **Traditional approaches** include these events, creating misleading visualizations

#### 🎯 **Our Solution: Smart Filtering**
1. **Automatic Exclusion**: Remove all events with `time_since_case_start = 0`
2. **Focus on Temporal Events**: Analyze only events that occur *after* case initiation
3. **Meaningful Patterns**: Reveal actual process timing and delays

### 📊 **Temporal Distribution Patterns**
After filtering, remaining events typically show:
- **80-90%** of events cluster in early-to-mid process stages
- **5-10%** represent significant delays or exceptional cases
- **Multi-modal distributions** indicating different process paths

### 🔬 Methodological Innovation
1. **Smart Event Filtering**: Exclude non-temporal case-start events
2. **Multi-transformation Analysis**: Compare how different transformations reveal process patterns
3. **Interactive Exploration**: Real-time switching between transformation methods
4. **Statistical Sorting**: Organize events by meaningful statistical measures
5. **Cross-Dataset Validation**: Test approaches across multiple BPI datasets

### 📊 Analytical Benefits
- **Pattern Recognition**: Identify typical vs. exceptional process timing patterns
- **Process Insights**: Understand bottlenecks and variations in temporal flow
- **Comparative Analysis**: Compare event types across statistical dimensions
- **Multi-Domain Validation**: Test insights across healthcare, finance, and government processes

---

## 🚀 Quick Start

### 📋 Prerequisites
```bash
Python 3.8+
Virtual environment (recommended)
```

### ⚡ Installation & Setup

#### Option 1: One-Command Setup (Recommended)
```bash
# 1. Clone the repository
git clone https://github.com/umutyesildal/ProcessMiningVisualization.git
cd ProcessMiningVisualization

# 2. Complete setup and launch (installs dependencies, processes data, launches dashboard)
python setup_and_run.py
```

#### Option 2: Using Makefile
```bash
# Full setup and run
make setup

# Or step by step:
make install    # Install dependencies
make process    # Process XES files
make run        # Launch dashboard (skip processing)
```

#### Option 3: Manual Step-by-Step
```bash
# 1. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run complete setup
python setup_and_run.py
```

#### Advanced Usage
```bash
# Only process data (don't run dashboard)
python setup_and_run.py --process-data

# Skip data processing, just run dashboard
python setup_and_run.py --skip-processing

# Test installation
make test
```

### 📁 Project Structure
```
pmva_implementation/
├── 📁 src/                              # Source code
│   ├── app.py                           # Main dashboard application
│   ├── __init__.py                      # Package initialization
│   ├── utils/                           # Utility modules
│   │   ├── __init__.py
│   │   └── transformations.py          # Time transformation functions
│   └── data_processing/                 # Data processing modules
│       ├── __init__.py
│       └── data_processing.py           # XES to CSV conversion
├── � datasets/                         # Data storage
│   ├── raw/                             # Original XES files
│   │   ├── BPI_Challenge_2012.xes
│   │   ├── Sepsis Cases - Event Log.xes
│   │   └── Road_Traffic_Fine_Management_Process.xes
│   └── processed/                       # Processed CSV files
│       ├── processed_trafficfines.csv
│       ├── processed_bpi2012.csv
│       └── processed_sepsis.csv
├── 📁 scripts/                          # Analysis and utility scripts
│   ├── README.md
│   └── analysis/                        # Data analysis scripts
├── 📁 docs/                             # Documentation
│   ├── papers/                          # Research papers
│   ├── INSTALL.md                       # Installation guide
│   └── DEVELOPER.md                     # Developer documentation
├── 📁 venv/                             # Virtual environment (git ignored)
├── 🐍 setup_and_run.py                 # Single entry point - setup & launch
├── 📋 Makefile                         # Convenient command shortcuts
├── 📦 requirements.txt                 # Python dependencies
├── 🔧 .gitignore                       # Git ignore rules
└── 📖 README.md                        # Main documentation
```

---

## 💡 How to Use the Dashboard

### 🎛️ **Control Panel** *(Left Sidebar)*

#### 🔄 **Transformation Selection**
Choose how to transform time data:
- **Log Time**: Best for skewed data (default)
- **Raw Hours/Days/Weeks/Months**: For absolute time analysis
- **Square Root**: Moderate compression
- **Min-Max Scaled**: For normalized comparison

#### 📊 **Event Sorting**
Organize event types by:
- **Frequency**: Most common events first
- **Statistical Measures**: Mean, median, min, max
- **Quartiles**: 25th, 75th percentiles

### 📈 **Main Visualization**
- **Violin Shapes**: Show distribution density
- **Box Plots**: Display quartiles and outliers
- **Interactive**: Hover for detailed statistics
- **Responsive**: Adapts to screen size

---

## 🔍 Interpreting Violin Plots

### 📊 **What the Shapes Tell You**

| **Violin Shape** | **Interpretation** | **Business Meaning** |
|------------------|-------------------|---------------------|
| 🏺 **Narrow at top, wide at bottom** | Most events happen quickly | Efficient process start |
| 🎭 **Multiple bulges** | Bi-modal distribution | Different process paths |
| 📏 **Long tail** | Occasional delays | Exceptional cases/appeals |
| 📦 **Box inside violin** | Quartile ranges | Typical timing ranges |

### 🎯 **Process Mining Insights**
- **Send Fine → Payment**: How quickly citizens respond to fine notifications
- **Penalty Addition Patterns**: When late payment penalties are typically added
- **Collection Process Timing**: Long-term debt recovery patterns
- **Multi-Domain Comparison**: Cross-validation across healthcare, finance, government processes

#### 🏥 **Sepsis Process Patterns**
- **ER Registration → Leucocytes Test**: Initial triage to lab work timing
- **Test Sequences**: How quickly different diagnostic tests are ordered
- **Treatment Delays**: Critical care timing patterns

#### 🏦 **BPI 2012 Loan Patterns** 
- **Submission → Validation**: Application processing speed
- **Offer Calls**: Follow-up communication timing
- **Approval Delays**: Decision-making bottlenecks

---

## 🧰 Technical Implementation

### 🏗️ **Architecture**
- **Frontend**: Dash + Plotly (Interactive web components)
- **Backend**: Python data processing
- **Styling**: Custom CSS with responsive design
- **Data Processing**: Pandas + NumPy transformations

### 📦 **Dependencies**
| **Package** | **Purpose** | **Version** |
|-------------|-------------|-------------|
| `dash` | Web framework | Latest |
| `plotly` | Visualization | Latest |
| `pandas` | Data manipulation | Latest |
| `numpy` | Numerical operations | Latest |
| `scikit-learn` | Scaling transformations | Latest |
| `pm4py` | Process mining utilities | Latest |

### 🔧 **Modular Design**
```python
# Easy to extend transformations
from transformations import transform_time_data

# Add new transformation methods in transformations.py
def custom_transformation(data):
    return transformed_data, title, description
```

---

## 📊 Research Applications

### 🎓 **Academic Use Cases**
- **Process Mining Research**: Temporal pattern analysis
- **Business Process Analysis**: Performance measurement
- **Data Visualization Studies**: Transformation method comparison
- **Statistical Analysis**: Distribution shape investigation

### 🏢 **Business Applications**
- **Process Optimization**: Identify bottlenecks and delays
- **Performance Monitoring**: Track process timing metrics
- **Exception Analysis**: Understand unusual case patterns
- **Comparative Studies**: Before/after process improvements

---

## 🔮 Future Enhancements

### 📈 **Planned Features**
- [ ] **Multi-dataset Support**: Easy switching between event logs
- [ ] **Export Functionality**: Save plots and statistical reports
- [ ] **Advanced Filtering**: Date ranges, case attributes
- [ ] **Comparison Mode**: Side-by-side process comparison
- [ ] **Statistical Testing**: Automated distribution analysis

### 🛠️ **Technical Roadmap**
- [ ] **Database Integration**: Direct connection to process mining tools
- [ ] **API Endpoints**: Programmatic access to transformations
- [ ] **Custom Transformations**: User-defined transformation formulas
- [ ] **Mobile App**: Native mobile visualization

---

## 👥 Contributing

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

---

## 📝 License

This project is available for **academic and research use**. For commercial applications, please contact the authors.

---

## 🏆 Acknowledgments

- **Process Mining Community** for methodological foundations
- **Plotly/Dash Teams** for excellent visualization tools
- **Traffic Fine Dataset** from BPI Challenge series
- **Academic Supervisors** for research guidance

---

## 📸 Screenshots

### 🎛️ **Dashboard Interface**
The main dashboard features a clean, professional layout with:
- **Left sidebar**: Transformation and sorting controls
- **Main area**: Interactive violin plot visualization
- **Responsive design**: Works on desktop, tablet, and mobile

### 🔄 **Transformation Comparison**
Different transformation methods reveal different insights:
- **Log transformation**: Shows process patterns clearly
- **Raw time**: Displays absolute durations
- **Months view**: Perfect for long-term process analysis

---

## 🔬 Advanced Usage

### 📊 **Statistical Analysis**
```python
# Access transformation functions programmatically
from transformations import transform_time_data, TRANSFORMATION_DESCRIPTIONS

# Apply transformations to your data
transformed_data, title, description = transform_time_data(your_data, 'log_hours')

# Get transformation documentation
print(TRANSFORMATION_DESCRIPTIONS['log_hours']['description'])
```

### 🎯 **Custom Analysis Workflows**
1. **Start with Log transformation** to see overall patterns
2. **Switch to Raw time** to understand absolute durations  
3. **Use sorting options** to identify process bottlenecks
4. **Compare with Min-Max scaling** for relative analysis

### 📈 **Process Mining Best Practices**
- **Always exclude case-start events** for temporal analysis (time = 0 events)
- **Start with log transformation** for skewed process data
- **Use raw time views** when absolute timing matters
- **Sort by median** to understand typical process behavior
- **Sort by max** to identify processes with high variability
- **Cross-validate insights** across multiple datasets and domains

---

*Last updated: June 2025*
*Version: 2.0 - Enhanced Dashboard with Modular Transformations*
