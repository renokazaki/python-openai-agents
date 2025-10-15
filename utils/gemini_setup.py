"""Gemini設定の共通モジュール"""
import os
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel
from dotenv import load_dotenv

load_dotenv(override=True)

GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"

def get_gemini_api_key():
    """Gemini APIキーを取得"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY が .env ファイルに設定されていません")
    return api_key

def create_gemini_model(model_name="gemini-2.5-flash-preview-05-20"):
    """Geminiモデルを作成"""
    api_key = get_gemini_api_key()
    client = AsyncOpenAI(base_url=GEMINI_BASE_URL, api_key=api_key)
    return OpenAIChatCompletionsModel(model=model_name, openai_client=client)

def check_api_keys():
    """APIキーの存在確認"""
    keys = {
        "GEMINI_API_KEY": os.getenv("GEMINI_API_KEY"),
        # "GOOGLE_API_KEY": os.getenv("GOOGLE_API_KEY"),
        # "OPENAI_API_KEY": os.getenv("OPENAI_API_KEY"),
        # "SENDGRID_API_KEY": os.getenv("SENDGRID_API_KEY"),
        # "DEEPSEEK_API_KEY": os.getenv("DEEPSEEK_API_KEY"),
        # "GROQ_API_KEY": os.getenv("GROQ_API_KEY"),
    }
    
    for key_name, key_value in keys.items():
        if key_value:
            print(f"✓ {key_name}: 設定済み ({key_value[:8]}...)")
        else:
            print(f"✗ {key_name}: 未設定")