from config.settings import settings

WHATSAPP_CONFIG = {
    "phone_number_id": settings.WHATSAPP_PHONE_NUMBER_ID,
    "access_token": settings.WHATSAPP_ACCESS_TOKEN,
    "verify_token": settings.WHATSAPP_VERIFY_TOKEN,
    "webhook_url": settings.WHATSAPP_WEBHOOK_URL,
    "api_version": "v18.0",
    "base_url": "https://graph.facebook.com"
}

# Message templates
MESSAGE_TEMPLATES = {
    "welcome": {
        "en": "Welcome to {clinic_name}! I'm your AI health concierge. How can I help you today?",
        "ar": "مرحباً بك في {clinic_name}! أنا مساعدك الصحي الذكي. كيف يمكنني مساعدتك اليوم؟"
    },
    "appointment_confirmation": {
        "en": "Your appointment has been confirmed for {date} at {time}. We'll send you a reminder 24 hours before.",
        "ar": "تم تأكيد موعدك في {date} في {time}. سنرسل لك تذكيراً قبل 24 ساعة."
    },
    "follow_up": {
        "en": "Hi! How are you feeling after your recent treatment? Please let us know if you have any questions.",
        "ar": "مرحباً! كيف تشعر بعد العلاج الأخير؟ يرجى إعلامنا إذا كان لديك أي أسئلة."
    }
}