# Azure Deployment Guide

This guide provides step-by-step instructions for deploying the Mildew Detection application to Azure App Service.

## Prerequisites

- An Azure account with an active subscription
- Azure CLI installed (optional, for command-line deployment)
- GitHub account (for automated deployments)

## Deployment Methods

You can deploy this application to Azure using one of the following methods:

### Method 1: Azure Portal (Recommended for beginners)

#### Step 1: Create Azure App Service

1. Log in to the [Azure Portal](https://portal.azure.com)
2. Click "Create a resource" → "Web App"
3. Fill in the following details:
   - **Subscription**: Select your subscription
   - **Resource Group**: Create new or use existing
   - **Name**: Choose a unique name (e.g., `mildew-detection-app`)
   - **Publish**: Code
   - **Runtime stack**: Python 3.11
   - **Operating System**: Linux
   - **Region**: Choose nearest region
   - **Pricing Plan**: Choose appropriate plan (B1 or higher recommended)
4. Click "Review + Create" → "Create"

#### Step 2: Configure Startup Command

1. Navigate to your App Service in Azure Portal
2. Go to "Configuration" → "General settings"
3. Set **Startup Command**: `bash startup.sh`
4. Click "Save"

#### Step 3: Deploy Code

**Option A: Using GitHub Actions (Recommended)**

1. In your App Service, go to "Deployment Center"
2. Choose "GitHub" as the source
3. Authorize Azure to access your GitHub account
4. Select:
   - **Organization**: Your GitHub username
   - **Repository**: mildew-detection
   - **Branch**: main
5. Azure will automatically create a workflow file
6. Alternatively, use the provided `.github/workflows/azure-deploy.yml` file:
   - Update `AZURE_WEBAPP_NAME` with your app name
   - In Azure Portal, download the Publish Profile:
     - Go to your App Service → Overview → "Get publish profile"
   - In GitHub, go to repository Settings → Secrets and variables → Actions
   - Add a new secret: `AZURE_WEBAPP_PUBLISH_PROFILE` with the downloaded profile content
7. Push to the main branch to trigger deployment

**Option B: Using Local Git**

1. In your App Service, go to "Deployment Center"
2. Choose "Local Git" as the source
3. Copy the Git Clone URL
4. In your local repository:
   ```bash
   git remote add azure <Git Clone URL>
   git push azure main
   ```

**Option C: Using ZIP Deploy**

1. Create a ZIP file of your project (excluding .git, venv, and other unnecessary files)
2. Use Azure CLI:
   ```bash
   az webapp deployment source config-zip --resource-group <resource-group-name> --name <app-name> --src <path-to-zip>
   ```

#### Step 4: Configure Application Settings (Optional)

1. Go to "Configuration" → "Application settings"
2. Add any required environment variables
3. Click "Save"

#### Step 5: Verify Deployment

1. Go to your App Service "Overview"
2. Click the URL to open your application
3. The Streamlit dashboard should load

### Method 2: Azure CLI Deployment

#### Prerequisites
Install Azure CLI: https://docs.microsoft.com/en-us/cli/azure/install-azure-cli

#### Commands

```bash
# Login to Azure
az login

# Create a resource group (if needed)
az group create --name mildew-detection-rg --location eastus

# Create an App Service plan
az appservice plan create --name mildew-detection-plan --resource-group mildew-detection-rg --sku B1 --is-linux

# Create a web app
az webapp create --resource-group mildew-detection-rg --plan mildew-detection-plan --name <your-unique-app-name> --runtime "PYTHON:3.11"

# Configure startup command
az webapp config set --resource-group mildew-detection-rg --name <your-app-name> --startup-file "bash startup.sh"

# Deploy code from local git
az webapp deployment source config-local-git --name <your-app-name> --resource-group mildew-detection-rg

# Or deploy using ZIP
az webapp deployment source config-zip --resource-group mildew-detection-rg --name <your-app-name> --src app.zip
```

### Method 3: Using Azure DevOps Pipelines

1. Create an Azure DevOps project
2. Set up a pipeline using the azure-pipelines.yml template
3. Configure service connection to your Azure subscription
4. Run the pipeline

## Configuration Files

The following files are configured for Azure deployment:

- **startup.sh**: Startup script for Azure App Service
- **.github/workflows/azure-deploy.yml**: GitHub Actions workflow for automated deployment
- **azure-config.json**: Azure configuration metadata
- **requirements.txt**: Python dependencies

## Troubleshooting

### Application doesn't start

1. Check logs in Azure Portal:
   - Go to your App Service → "Log stream"
   - Or download logs from "Diagnose and solve problems"
2. Verify startup command is set: `bash startup.sh`
3. Check if all dependencies are installed correctly

### Deployment fails

1. Check Python version matches (3.11)
2. Verify all files are included in deployment
3. Check build logs in "Deployment Center"

### Out of memory errors

1. Upgrade to a higher pricing tier (App Service Plan)
2. Optimize model loading in code
3. Consider using Azure Container Instances or AKS for larger applications

### Port issues

The application is configured to run on port 8000, which is the default for Azure App Service Linux Python apps.

## Cost Optimization

- Start with the Free (F1) or Basic (B1) tier for testing
- Scale up to Standard (S1) or Premium for production
- Use deployment slots for staging/production separation
- Enable auto-scaling based on load

## Security Best Practices

1. Enable HTTPS only
2. Set up custom domain with SSL certificate
3. Configure CORS settings in Azure Portal if needed
4. Use Azure Key Vault for sensitive configuration
5. Enable Application Insights for monitoring

## Monitoring

1. Enable Application Insights:
   - Go to your App Service → "Application Insights"
   - Click "Turn on Application Insights"
2. View metrics, logs, and performance data
3. Set up alerts for critical issues

## Additional Resources

- [Azure App Service Documentation](https://docs.microsoft.com/en-us/azure/app-service/)
- [Deploy Python apps to Azure](https://docs.microsoft.com/en-us/azure/app-service/quickstart-python)
- [Streamlit on Azure](https://docs.streamlit.io/knowledge-base/tutorials/deploy/azure)

## Support

For issues specific to this application, please open an issue on the GitHub repository.
For Azure-specific issues, consult Azure support or documentation.
