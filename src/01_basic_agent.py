"""基本的なエージェントのデモ"""
import asyncio
from agents import Agent, Runner, trace
from utils.gemini_setup import create_gemini_model

async def basic_joke():
    """基本的なジョークエージェント"""
    print("=== 基本的なジョークエージェント ===\n")
    
    # Geminiモデルを作成
    gemini_model = create_gemini_model()
    
    # エージェントを作成
    agent = Agent(
        name="Jokester",
        instructions="あなたはジョークを話すコメディアンです。面白くて知的なジョークを話してください。",
        model=gemini_model
    )
    
    # エージェントを実行
    with trace("Telling a joke"):
        result = await Runner.run(agent, "AIエージェントについてのジョークを話してください")
        print(f"エージェントの回答:\n{result.final_output}\n")
    
    return result.final_output

async def simple_qa():
    """簡単なQ&Aデモ"""
    print("=== 簡単なQ&Aデモ ===\n")
    
    gemini_model = create_gemini_model()
    
    agent = Agent(
        name="QA Agent",
        instructions="あなたは親切で知識豊富なアシスタントです。",
        model=gemini_model
    )
    
    questions = [
        "2+2は？",
        "AIエージェントとは何ですか？",
        "Python でリストと辞書の違いは？"
    ]
    
    for question in questions:
        print(f"質問: {question}")
        result = await Runner.run(agent, question)
        print(f"回答: {result.final_output}\n")

async def main():
    """メイン関数"""
    print("\n" + "="*60)
    print("Lab 1: 基本的なエージェント")
    print("="*60 + "\n")
    
    # 基本的なジョーク
    await basic_joke()
    
    # 簡単なQ&A
    await simple_qa()

if __name__ == "__main__":
    asyncio.run(main())