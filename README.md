# 🚗 Process Mining Violin Plot Visualization Dashboard

**Interactive visualization of event type distributions over time using violin charts for process mining analysis**

![Process Mining](https://img.shields.io/badge/Process%20Mining-Violin%20Plots-blue)
![Python](https://img.shields.io/badge/Python-3.8+-green)
![Dash](https://img.shields.io/badge/Framework-Dash-red)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 📊 Overview

This interactive dashboard transforms process mining event logs into meaningful violin plot visualizations, revealing temporal patterns and distributions in business processes. Built specifically for analyzing event time distributions in process mining contexts, with focus on the **Road Traffic Fine Management Process**.

### 🎯 Key Features

- **🎻 Interactive Violin Plots** - Visualize event time distributions with box plots overlay
- **🔄 Multiple Transformations** - 7 different time transformation methods
- **📊 Dynamic Sorting** - Sort events by statistical measures (frequency, mean, median, quartiles)
- **📱 Responsive Design** - Modern, mobile-friendly interface
- **⚡ Real-time Updates** - Instant visualization updates based on user selections
- **🎨 Professional UI** - Clean, dashboard-style interface with visual hierarchy

---

## 📈 Dataset Overview

### Road Traffic Fine Management Process
Our primary dataset contains comprehensive information about traffic fine processing:

| **Metric** | **Value** |
|------------|-----------|
| 📁 **Total Cases** | 150,370 |
| 📊 **Total Events** | 561,470 |
| 🏷️ **Event Types** | 11 unique types |
| ⏱️ **Time Range** | 0 - 4,372 days |
| 📅 **Average Process Duration** | 148 days |
| 📍 **Median Process Duration** | 84 days |

### 📋 Top Event Types (Dashboard Focus)

| **Event Type** | **Count** | **Percentage** | **Description** |
|----------------|-----------|----------------|-----------------|
| 🆕 **Create Fine** | 150,370 | 26.8% | Initial fine creation |
| 📤 **Send Fine** | 103,987 | 18.5% | Fine notification sent |
| 📝 **Insert Fine Notification** | 79,860 | 14.2% | Notification processing |
| ⚠️ **Add penalty** | 79,860 | 14.2% | Penalty addition |

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

## 🎯 Research Approach & Methodology

### 📚 Background
Process mining event logs typically exhibit **extreme temporal skewness**:
- **80-90%** of events occur in the early process stages
- **5-10%** represent significant delays or exceptional cases
- **Raw visualizations** often show uninformative distributions

### 🔬 Methodological Innovation
1. **Multi-transformation Analysis**: Compare how different transformations reveal process patterns
2. **Interactive Exploration**: Real-time switching between transformation methods
3. **Statistical Sorting**: Organize events by meaningful statistical measures
4. **Violin Plot Selection**: Shows both distribution shape and statistical summaries

### 📊 Analytical Benefits
- **Pattern Recognition**: Identify typical vs. exceptional process timing
- **Process Insights**: Understand bottlenecks and variations
- **Comparative Analysis**: Compare event types across statistical dimensions
- **Data-Driven Decisions**: Evidence-based process improvement recommendations

---

## 🚀 Quick Start

### 📋 Prerequisites
```bash
Python 3.8+
Virtual environment (recommended)
```

### ⚡ Installation & Setup
```bash
# 1. Clone/Download the project
cd pmva_implementation

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install pandas plotly dash pm4py numpy scikit-learn

# 4. Run the dashboard
python app.py

# 5. Open in browser
# → http://127.0.0.1:8050
```

### 📁 Project Structure
```
pmva_implementation/
├── 🏠 app.py                    # Main dashboard application
├── 🔄 transformations.py       # Time transformation methods
├── 📊 data_processing.py       # XES to CSV conversion
├── 📈 data/
│   ├── processed_trafficfines.csv     # Main dataset
│   ├── Road_Traffic_Fine_Management_Process.xes
│   ├── BPI_Challenge_2012.xes
│   └── Sepsis Cases - Event Log.xes
├── 📚 archive/                 # Analysis scripts
└── 📖 README.md               # This file
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
- **Create Fine → Send Fine**: How quickly fines are processed
- **Payment Patterns**: When citizens typically pay fines
- **Penalty Additions**: Delay indicators in the process
- **Collection Patterns**: Long-term debt recovery timing

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
- **Always start with log transformation** for skewed process data
- **Use raw time views** when absolute timing matters
- **Sort by median** to understand typical process behavior
- **Sort by max** to identify processes with high variability

---

*Last updated: June 2025*
*Version: 2.0 - Enhanced Dashboard with Modular Transformations*
