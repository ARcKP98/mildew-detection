# Quick Start: Deploy to Azure

This is a quick reference guide for deploying the Mildew Detection app to Azure. For detailed instructions, see [AZURE_DEPLOYMENT.md](AZURE_DEPLOYMENT.md).

## Prerequisites
- Azure account with active subscription
- Azure CLI installed (optional)

## Option 1: Azure Portal (Easiest)

### Step 1: Create App Service
1. Go to [Azure Portal](https://portal.azure.com)
2. Create a new **Web App**
3. Configuration:
   - **Runtime**: Python 3.11
   - **OS**: Linux
   - **Plan**: B1 or higher

### Step 2: Configure
1. In App Service → **Configuration** → **General settings**
2. Set **Startup Command**: `bash startup.sh`
3. Click **Save**

### Step 3: Deploy
**Using GitHub Actions (Recommended):**
1. In App Service → **Deployment Center** → Select **GitHub**
2. Choose this repository and `main` branch
3. Download **Publish Profile** from App Service Overview
4. In GitHub → Repository **Settings** → **Secrets**
5. Add secret: `AZURE_WEBAPP_PUBLISH_PROFILE`
6. Update `AZURE_WEBAPP_NAME` in `.github/workflows/azure-deploy.yml`
7. Push to trigger deployment

**Using Local Git:**
```bash
git remote add azure <Your-Azure-Git-URL>
git push azure main
```

### Step 4: Access
Your app will be available at: `https://your-app-name.azurewebsites.net`

## Option 2: Azure CLI

```bash
# Login
az login

# Create resource group
az group create --name mildew-rg --location eastus

# Create app service plan
az appservice plan create --name mildew-plan --resource-group mildew-rg --sku B1 --is-linux

# Create web app
az webapp create --resource-group mildew-rg --plan mildew-plan --name <unique-name> --runtime "PYTHON:3.11"

# Set startup command
az webapp config set --resource-group mildew-rg --name <your-app-name> --startup-file "bash startup.sh"

# Deploy
az webapp deployment source config-local-git --name <your-app-name> --resource-group mildew-rg
git remote add azure <Git-Clone-URL>
git push azure main
```

## Troubleshooting

### App doesn't start
- Check logs: App Service → **Log stream**
- Verify startup command: `bash startup.sh`
- Check Python version: 3.11

### Deployment fails
- Verify GitHub secret is configured
- Check workflow logs in GitHub Actions

### Need help?
See the full [AZURE_DEPLOYMENT.md](AZURE_DEPLOYMENT.md) guide for detailed troubleshooting and advanced options.

## Configuration Files

- `startup.sh` - Configures Streamlit for Azure
- `.github/workflows/azure-deploy.yml` - Automated deployment
- `azure-config.json` - App configuration metadata
- `requirements.txt` - Python dependencies

## Important Notes

1. **Port**: App runs on port 8000 (Azure default)
2. **Python**: Version 3.11 (as per .python-version)
3. **Cost**: Start with Free/Basic tier, scale as needed
4. **Security**: HTTPS is enabled by default

## Next Steps

1. Deploy the app
2. Test functionality
3. Set up custom domain (optional)
4. Enable Application Insights for monitoring
5. Configure auto-scaling if needed

For questions or issues, see [AZURE_DEPLOYMENT.md](AZURE_DEPLOYMENT.md) or open a GitHub issue.
