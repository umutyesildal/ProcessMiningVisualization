# Figure Instructions for Research Paper

To complete the 10-page paper, you need to add these figures to the `figures/` directory:

## Required Figures

### 1. **violin_chart_example.png**
- **What to capture**: Screenshot of your dashboard showing violin plots
- **Specific requirements**:
  - Show Traffic Fines dataset selected
  - Display 4-6 event types in violin plot format
  - Use logarithmic transformation
  - Sort by "Mean" to show clear ordering
  - Make sure the plot is clearly visible and readable

### 2. **dashboard_interface.png**
- **What to capture**: Full dashboard screenshot
- **Specific requirements**:
  - Include the sidebar with all controls visible
  - Show dataset dropdown, transformation options, sorting options
  - Display the main violin plot area
  - Include the dataset info panel
  - Capture at a good resolution (1920x1080 recommended)

### 3. **system_architecture.png** (Optional but recommended)
- **What to create**: Simple system architecture diagram
- **Content**: 
  - 4 boxes: Data Processing → Transformation → Visualization → UI
  - Show data flow arrows
  - Include technology labels (pm4py, Plotly, Dash, etc.)
  - Can be created in PowerPoint, draw.io, or any diagram tool

## How to Take Screenshots

1. **Run your dashboard**: `python setup_and_run.py`
2. **Open browser**: Go to http://localhost:8050
3. **For violin_chart_example.png**:
   - Select "Traffic Fines" dataset
   - Choose "Logarithmic" transformation
   - Set sort to "Mean"
   - Set events to 6
   - Take screenshot of the main plot area
4. **For dashboard_interface.png**:
   - Make sure sidebar is open
   - Show all controls clearly
   - Take full browser window screenshot

## File Specifications

- **Format**: PNG preferred (JPG acceptable)
- **Resolution**: At least 1200px wide for good quality in PDF
- **File names**: Exactly as specified above
- **Location**: Save in `paper/figures/` directory

## After Adding Figures

1. Uncomment the `\includegraphics` lines in main.tex
2. Remove the placeholder text
3. The figures will automatically be included in the compilation

## Alternative: Use Placeholders

If you don't want to add actual figures right now, the paper will compile with the current placeholder boxes and still reach ~10 pages with all the tables and content I added.

## Expected Page Count

With current content + tables + placeholders: **~9-10 pages**
With actual figures: **~10-11 pages** (you can remove some tables if needed)
