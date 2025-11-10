#!/bin/bash

# Azure App Service startup script for Streamlit application

# Create .streamlit directory if it doesn't exist
mkdir -p ~/.streamlit/

# Create Streamlit config file
echo "\
[server]
headless = true
port = 8000
enableCORS = false
address = 0.0.0.0

[browser]
gatherUsageStats = false
" > ~/.streamlit/config.toml

# Start Streamlit application
python -m streamlit run app.py --server.port=8000 --server.address=0.0.0.0
