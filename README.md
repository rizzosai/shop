# RizzosAI Sales Site

Professional Flask web application for RizzosAI domain packages and training guides.

## Features

- Professional sales page with pricing tiers
- Detailed guide descriptions for each package:
  - STARTER ($29): 5 Essential Success Guides
  - PRO ($99): 13 Advanced Business Guides  
  - ELITE ($249): 20 Elite Strategy Guides
  - EMPIRE ($499): 35 Empire Building Guides
- Responsive design with Australian red, white, blue theme
- Ready for Render deployment

## Deployment

### Deploy to Render

1. Connect this repository to Render
2. Use these settings:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Environment**: Python 3

### Custom Domain Setup

To use `domain.rizzosai.com`:

1. In Render dashboard, go to your service
2. Go to "Settings" > "Custom Domains"
3. Add `domain.rizzosai.com`
4. Update your DNS records to point to Render

## Local Development

```bash
pip install -r requirements.txt
python app.py
```

Visit `http://localhost:5000`

## Project Structure

```
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/         
│   ├── index.html     # Main sales page
│   ├── privacy.html   # Privacy policy
│   └── terms.html     # Terms and conditions
└── static/            # Static assets (CSS, JS, images)
```

## Package Details

Each package includes professional training guides:

- **Expert-written content** by entrepreneurs with $50M+ in revenue
- **Step-by-step instructions** with real-world examples
- **Actionable strategies** for immediate implementation
- **Regular updates** to keep content current
- **Money-back guarantee** for customer confidence