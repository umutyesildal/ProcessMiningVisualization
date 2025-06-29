# 📊 Dataset Summary - Quick Reference for Presentation

## 🗂️ **Dataset Overview Table**

| **Dataset** | **Domain** | **Cases** | **Events** | **Event Types** | **Time Range** | **Key Characteristic** |
|-------------|------------|-----------|------------|-----------------|----------------|----------------------|
| **Traffic Fines** | Government | 150,370 | 561,470 | 11 | 0-4,372 days | Long-tail citizen processes |
| **BPI 2012** | Finance | 13,087 | 262,000 | 23 | Multi-month | Business workflow stages |
| **Sepsis Cases** | Healthcare | 1,050 | 15,000 | 16 | Hours-days | Time-critical medical care |

## 🔍 **Event Lists by Dataset**

### 🚗 **Traffic Fines Events (After Smart Filtering)**
| **Rank** | **Event Name** | **Count** | **Description** |
|----------|----------------|-----------|-----------------|
| 1 | Send Fine | 101,093 | Fine notification sent to citizen |
| 2 | Add penalty | 79,860 | Late payment penalty added |
| 3 | Insert Fine Notification | 77,133 | Administrative notification processing |
| 4 | Payment | 72,781 | Fine payment received |
| 5 | Send for Credit Collection | 59,013 | Debt collection process initiated |
| 6 | Insert Date Appeal to Prefecture | 4,188 | Appeal submitted to authorities |
| 7 | Send Appeal to Prefecture | 4,141 | Appeal forwarded to prefecture |
| 8 | Receive Result Appeal from Prefecture | 999 | Appeal decision received |
| 9 | Notify Result Appeal to Offender | 896 | Appeal result notification |
| 10 | Appeal to Judge | 555 | Legal appeal to judge |

### 🏦 **BPI 2012 Events (After Smart Filtering)**
| **Rank** | **Event Name** | **Count** | **Description** |
|----------|----------------|-----------|-----------------|
| 1 | W_Completeren aanvraag | 54,850 | Complete application |
| 2 | W_Nabellen offertes | 52,016 | Call about offers |
| 3 | W_Nabellen incomplete dossiers | 25,190 | Call about incomplete files |
| 4 | W_Valideren aanvraag | 20,809 | Validate application |
| 5 | W_Afhandelen leads | 16,566 | Handle leads |
| 6 | A_PARTLYSUBMITTED | 13,087 | Partial submission |
| 7 | A_DECLINED | 7,635 | Application declined |
| 8 | A_PREACCEPTED | 7,367 | Pre-acceptance |
| 9 | O_SENT | 7,030 | Offer sent |
| 10 | W_Beoordelen fraude | 6,900 | Assess fraud |

### 🏥 **Sepsis Events (After Smart Filtering)**
| **Rank** | **Event Name** | **Count** | **Description** |
|----------|----------------|-----------|-----------------|
| 1 | Leucocytes | 3,383 | White blood cell test |
| 2 | CRP | 3,262 | C-reactive protein test |
| 3 | LacticAcid | 1,466 | Lactic acid measurement |
| 4 | Admission NC | 1,182 | Non-critical admission |
| 5 | ER Triage | 1,053 | Emergency room triage |
| 6 | ER Sepsis Triage | 1,049 | Sepsis-specific triage |
| 7 | IV Antibiotics | 823 | Intravenous antibiotics |
| 8 | IV Liquid | 753 | Intravenous fluids |
| 9 | Release A | 671 | Patient release (category A) |
| 10 | Admission IC | 536 | Intensive care admission |

## 🎯 **Key Demo Points by Dataset**

### **Traffic Fines Demo:**
- **Show Filtering Impact**: 561K → 400K events (28.7% reduction)
- **Highlight**: Payment behavior patterns (quick vs delayed payers)
- **Transformation**: Log view shows payment clustering
- **Insight**: Government process efficiency analysis

### **BPI 2012 Demo:**
- **Show Business Process**: Multi-stage loan application workflow
- **Highlight**: Application completion vs validation timing
- **Transformation**: Raw days/weeks for business timeframes
- **Insight**: Process optimization opportunities

### **Sepsis Demo:**
- **Show Medical Urgency**: Time-critical healthcare decisions
- **Highlight**: Lab test ordering patterns
- **Transformation**: Raw hours for critical care timing
- **Insight**: Clinical pathway optimization

## 📈 **Filtering Effectiveness Summary**

| **Process Type** | **Case-Start Event** | **Events Removed** | **Why Filtering Matters** |
|------------------|---------------------|-------------------|---------------------------|
| **Government** | "Create Fine" | 150,370 | Focus on citizen response timing |
| **Finance** | "A_SUBMITTED" | 13,087 | Analyze business process flow |
| **Healthcare** | "ER Registration" | 1,050 | Critical care timing analysis |

## 💡 **Quick Talking Points**

### **Cross-Domain Success:**
- ✅ Government: Long-term citizen interaction patterns
- ✅ Finance: Business process optimization insights  
- ✅ Healthcare: Time-critical medical decision support

### **Technical Innovation:**
- ✅ Smart filtering removes uninformative events
- ✅ 7 transformation methods reveal different patterns
- ✅ Real-time interactive analysis
- ✅ One-command setup for any dataset

### **Research Impact:**
- ✅ First systematic solution to case-start event problem
- ✅ Cross-domain validation across 3 industries
- ✅ Novel application of violin plots to process mining
- ✅ Production-ready open-source tool

---

*Quick Reference for Process Mining Dashboard Presentation*
