#!/bin/bash

echo "Setting up user authentication..."

# Create necessary directories if they don't exist
mkdir -p auth routes

# Download authentication files (replace with actual URLs from your GitHub)
curl -o auth/user_manager.py https://raw.githubusercontent.com/road-complaint-portal/authentication/main/auth/user_manager.py
curl -o routes/auth.py https://raw.githubusercontent.com/road-complaint-portal/authentication/main/routes/auth.py

echo "Authentication setup completed successfully!"
