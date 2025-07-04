#!/bin/bash

# 🎻 Process Mining Dashboard - Complete Setup Script
# Colors for better visual experience
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
PURPLE='\033[0;35m'
CYAN='\033[0;36m'
WHITE='\033[1;37m'
NC='\033[0m' # No Color

# Function to print colored text
print_color() {
    echo -e "${1}${2}${NC}"
}

# Function to print header
print_header() {
    echo
    print_color $PURPLE "═══════════════════════════════════════════════════════════════"
    print_color $WHITE "🎻 $1"
    print_color $PURPLE "═══════════════════════════════════════════════════════════════"
    echo
}

# Function to print step
print_step() {
    print_color $CYAN "🔄 $1"
}

# Function to print success
print_success() {
    print_color $GREEN "✅ $1"
}

# Function to print error
print_error() {
    print_color $RED "❌ $1"
}

# Function to print warning
print_warning() {
    print_color $YELLOW "⚠️  $1"
}

# Function to print info
print_info() {
    print_color $BLUE "ℹ️  $1"
}

# Dataset information
declare -A datasets
datasets["traffic"]="Road Traffic Fine Management Process|https://data.4tu.nl/ndownloader/items/806acd1a-2bf2-4e39-be21-69b8cad10909/versions/1|Road_Traffic_Fine_Management_Process.xes"
datasets["sepsis"]="Sepsis Cases - Event Log|https://data.4tu.nl/ndownloader/items/33632f3c-5c48-40cf-8d8f-2db57f5a6ce7/versions/1|Sepsis Cases - Event Log.xes"
datasets["bpi2012"]="BPI Challenge 2012|https://data.4tu.nl/ndownloader/items/533f66a4-8911-4ac7-8612-1235d65d1f37/versions/1|BPI_Challenge_2012.xes"
datasets["bpi2017"]="BPI Challenge 2017|https://data.4tu.nl/ndownloader/items/34c3f44b-3101-4ea9-8281-e38905c68b8d/versions/1|BPI Challenge 2017.xes"

# Function to check if file exists
file_exists() {
    local filename="$1"
    if [ -f "datasets/raw/$filename" ]; then
        return 0
    else
        return 1
    fi
}

# Function to download dataset
download_dataset() {
    local key="$1"
    local info="${datasets[$key]}"
    local name=$(echo "$info" | cut -d'|' -f1)
    local url=$(echo "$info" | cut -d'|' -f2)
    local filename=$(echo "$info" | cut -d'|' -f3)
    
    print_step "Downloading: $name"
    print_info "URL: $url"
    print_info "Saving as: $filename"
    
    # Create raw directory if it doesn't exist
    mkdir -p datasets/raw
    
    # Download with progress bar
    if wget --progress=bar:force "$url" -O "datasets/raw/$filename" 2>&1 | \
       sed -u 's/.* \([0-9]\+%\)\ \+\([0-9.]\+\ [KMG]B\).*/📥 \1 - \2/'; then
        print_success "Downloaded: $filename"
        return 0
    else
        print_error "Failed to download: $filename"
        return 1
    fi
}

# Function to show dataset menu
show_dataset_menu() {
    echo
    print_color $YELLOW "📂 Available Datasets:"
    echo
    print_color $WHITE "1) 🚗 Road Traffic Fine Management Process"
    print_color $WHITE "2) 🏥 Sepsis Cases - Event Log"  
    print_color $WHITE "3) 💰 BPI Challenge 2012"
    print_color $WHITE "4) 💼 BPI Challenge 2017"
    print_color $WHITE "5) 🌟 Download All Datasets"
    print_color $WHITE "6) ⏭️  Skip Downloads (Use Existing)"
    echo
}

# Function to check dataset status
check_dataset_status() {
    echo
    print_color $CYAN "📋 Dataset Status Check:"
    echo
    
    local all_exist=true
    
    for key in "${!datasets[@]}"; do
        local info="${datasets[$key]}"
        local name=$(echo "$info" | cut -d'|' -f1)
        local filename=$(echo "$info" | cut -d'|' -f3)
        
        if file_exists "$filename"; then
            local size=$(du -h "datasets/raw/$filename" | cut -f1)
            print_color $GREEN "✅ $name ($size)"
        else
            print_color $RED "❌ $name (Not found)"
            all_exist=false
        fi
    done
    
    if $all_exist; then
        print_success "All datasets are available!"
        return 0
    else
        print_warning "Some datasets are missing."
        return 1
    fi
}

# Function to handle dataset downloads
handle_downloads() {
    while true; do
        check_dataset_status
        
        show_dataset_menu
        
        print_color $YELLOW "👉 Select an option (1-6): "
        read -r choice
        
        case $choice in
            1)
                download_dataset "traffic"
                ;;
            2)
                download_dataset "sepsis"
                ;;
            3)
                download_dataset "bpi2012"
                ;;
            4)
                download_dataset "bpi2017"
                ;;
            5)
                print_step "Downloading all datasets..."
                for key in "${!datasets[@]}"; do
                    local info="${datasets[$key]}"
                    local filename=$(echo "$info" | cut -d'|' -f3)
                    if ! file_exists "$filename"; then
                        download_dataset "$key"
                    else
                        local name=$(echo "$info" | cut -d'|' -f1)
                        print_info "Already exists: $name"
                    fi
                done
                print_success "All downloads completed!"
                break
                ;;
            6)
                print_info "Skipping downloads, using existing datasets..."
                break
                ;;
            *)
                print_error "Invalid choice! Please select 1-6."
                ;;
        esac
        
        echo
        print_color $YELLOW "🔄 Continue with downloads? (y/n): "
        read -r continue_choice
        if [[ $continue_choice =~ ^[Nn]$ ]]; then
            break
        fi
    done
}

# Function to check Python requirements
check_requirements() {
    print_step "Checking Python requirements..."
    
    if ! command -v python3 &> /dev/null; then
        print_error "Python3 is not installed!"
        return 1
    fi
    
    if ! python3 -c "import sys; exit(0 if sys.version_info >= (3, 7) else 1)" 2>/dev/null; then
        print_error "Python 3.7+ is required!"
        return 1
    fi
    
    print_success "Python3 is available"
    
    # Check if requirements.txt exists
    if [ ! -f "requirements.txt" ]; then
        print_error "requirements.txt not found!"
        return 1
    fi
    
    # Create virtual environment if it doesn't exist
    if [ ! -d "venv" ]; then
        print_step "Creating Python virtual environment..."
        if python3 -m venv venv; then
            print_success "Virtual environment created"
        else
            print_error "Failed to create virtual environment"
            return 1
        fi
    else
        print_info "Virtual environment already exists"
    fi
    
    # Activate virtual environment and install requirements
    print_step "Activating virtual environment and installing dependencies..."
    source venv/bin/activate
    
    if pip install -r requirements.txt --quiet; then
        print_success "All dependencies installed in virtual environment"
        return 0
    else
        print_error "Failed to install dependencies"
        return 1
    fi
}

# Function to process datasets
process_datasets() {
    print_step "Processing XES files to CSV format..."
    
    # Activate virtual environment
    source venv/bin/activate
    
    if python setup_and_run.py --process-data; then
        print_success "Dataset processing completed!"
        return 0
    else
        print_error "Dataset processing failed!"
        return 1
    fi
}

# Function to launch dashboard
launch_dashboard() {
    print_step "Launching Process Mining Dashboard..."
    echo
    print_color $GREEN "🎯 Dashboard Features:"
    print_color $WHITE "  • Interactive Violin Plots"
    print_color $WHITE "  • Multiple Dataset Support"
    print_color $WHITE "  • Real-time Transformations"
    print_color $WHITE "  • Statistical Sorting"
    echo
    print_color $CYAN "🌐 Dashboard will be available at: http://127.0.0.1:8050"
    print_color $YELLOW "⚡ Press Ctrl+C to stop the server"
    echo
    
    # Countdown
    for i in {3..1}; do
        print_color $YELLOW "🚀 Starting in $i seconds..."
        sleep 1
    done
    
    # Activate virtual environment and run dashboard
    source venv/bin/activate
    python setup_and_run.py --skip-processing
}

# Main execution
main() {
    # Welcome header
    clear
    print_header "PROCESS MINING DASHBOARD - COMPLETE SETUP"
    
    print_color $GREEN "🎯 This script will:"
    print_color $WHITE "  1. 📥 Download process mining datasets"
    print_color $WHITE "  2. 🔧 Install Python dependencies"
    print_color $WHITE "  3. 📊 Process XES files to CSV"
    print_color $WHITE "  4. 🚀 Launch the dashboard"
    echo
    
    print_color $YELLOW "⚡ Ready to start? (y/n): "
    read -r start_choice
    
    if [[ ! $start_choice =~ ^[Yy]$ ]]; then
        print_info "Setup cancelled by user."
        exit 0
    fi
    
    # Step 1: Handle downloads
    print_header "STEP 1: DATASET MANAGEMENT"
    handle_downloads
    
    # Step 2: Check requirements
    print_header "STEP 2: ENVIRONMENT SETUP"
    if ! check_requirements; then
        print_error "Environment setup failed!"
        exit 1
    fi
    
    # Step 3: Process datasets
    print_header "STEP 3: DATA PROCESSING"
    if ! process_datasets; then
        print_error "Data processing failed!"
        exit 1
    fi
    
    # Step 4: Launch dashboard
    print_header "STEP 4: DASHBOARD LAUNCH"
    launch_dashboard
}

# Check if wget is available
if ! command -v wget &> /dev/null; then
    print_error "wget is required but not installed!"
    print_info "Please install wget and try again."
    exit 1
fi

# Run main function
main "$@"
