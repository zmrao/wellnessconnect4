# WellnessConnect - AI-Powered Health Concierge Platform

WellnessConnect is a WhatsApp-based AI health concierge that pre-qualifies leads, schedules appointments, and provides personalized wellness recommendations for healthcare clinics.

## Features

- **AI Chatbot Integration**: WhatsApp Business integration with Claude AI assistant
- **Smart Lead Qualification**: Automatic categorization by treatment type and urgency
- **Personalized Content Delivery**: Targeted wellness content in English/Arabic
- **Automated Follow-up**: Post-treatment care reminders and wellness plan delivery
- **White-label Ready**: Scalable solution for multiple clinics

## Quick Start

1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Copy `.env.example` to `.env` and configure your settings
4. Run database setup: `python scripts/setup_database.py`
5. Start the application: `python main.py`

## Project Structure

- `/src/api/` - API endpoints and webhooks
- `/src/core/` - Core business logic
- `/src/models/` - Database models
- `/src/services/` - External service integrations
- `/src/utils/` - Utility functions
- `/config/` - Configuration files
- `/database/` - Database migrations
- `/templates/` - HTML templates
- `/tests/` - Test files

## Documentation

- [API Documentation](docs/api_documentation.md)
- [Deployment Guide](docs/deployment_guide.md)
- [White Label Setup](docs/white_label_setup.md)

## License

Proprietary - The Wellness London