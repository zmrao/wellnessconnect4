from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import PlainTextResponse
import json
import logging
from typing import Dict, Any

from config.whatsapp_config import WHATSAPP_CONFIG
from src.services.whatsapp_service import WhatsAppService
from src.core.ai_assistant import AIAssistant

router = APIRouter()
logger = logging.getLogger(__name__)


@router.get("/whatsapp")
async def verify_webhook(request: Request):
    """Verify WhatsApp webhook"""
    params = request.query_params
    
    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")
    
    if mode == "subscribe" and token == WHATSAPP_CONFIG["verify_token"]:
        logger.info("WhatsApp webhook verified successfully")
        return PlainTextResponse(challenge)
    else:
        logger.warning("WhatsApp webhook verification failed")
        raise HTTPException(status_code=403, detail="Verification failed")


@router.post("/whatsapp")
async def handle_webhook(request: Request):
    """Handle incoming WhatsApp messages"""
    try:
        body = await request.json()
        logger.info(f"Received webhook: {json.dumps(body, indent=2)}")
        
        # Process webhook data
        if "entry" in body:
            for entry in body["entry"]:
                if "changes" in entry:
                    for change in entry["changes"]:
                        if change.get("field") == "messages":
                            await process_message(change["value"])
        
        return {"status": "success"}
    
    except Exception as e:
        logger.error(f"Error processing webhook: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


async def process_message(message_data: Dict[str, Any]):
    """Process incoming WhatsApp message"""
    try:
        if "messages" not in message_data:
            return
        
        whatsapp_service = WhatsAppService()
        ai_assistant = AIAssistant()
        
        for message in message_data["messages"]:
            phone_number = message["from"]
            message_text = message.get("text", {}).get("body", "")
            message_type = message.get("type", "text")
            
            if message_type == "text" and message_text:
                # Process message with AI assistant
                response = await ai_assistant.process_message(
                    phone_number=phone_number,
                    message=message_text
                )
                
                # Send response back to user
                await whatsapp_service.send_message(
                    phone_number=phone_number,
                    message=response
                )
    
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")