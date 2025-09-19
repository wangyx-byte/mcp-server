from src.conversationalAI.api.api import ConversationalaiAPI
from mcp.server.fastmcp import FastMCP
from .note import note
import json


def create_mcp_server():
    service = ConversationalaiAPI()
    mcp = FastMCP(
        name="对话式 AI MCP",
        instructions="""
      ## MCP Invocation Method Guide
      - For task decomposition, it is necessary to use the mcp tool.
      - The first step requires invoking the `get_note` function to obtain the parameter description.
      - Subsequently, the corresponding method should be called to retrieve the data.
        豆包实时通话同款音视频服务，整合 LLM、VLM、ASR、TTS、以及音视频处理/传输能力，快速实现用户与大模型间流畅、自然、真人感的实时对话功能
      """,
    )

    @mcp.tool()
    def guide():
        """
        ## MCP Invocation Method Guide
        - For task decomposition, it is necessary to use the mcp tool.
        - The first step requires invoking the `get_note` function to obtain the parameter description.
        - Subsequently, the corresponding method should be called to retrieve the data.
        """
        return """use  `guide` description to get how to use Mcp Server"""

    @mcp.tool()
    def get_note(func_name: str) -> str:
        """
        获取参数描述

        Args:
            func_name: 函数名

        """
        return note.get(func_name)

    @mcp.tool()
    def start_voice_chat(params: dict, body: dict) -> str:
        """
        在实时音视频场景中，你可以调用此接口在房间内引入一个智能体进行 AI 实时交互。
        RTC 提供语音识别（ASR）、语音合成（TTS）、大模型（LLM） 一站式接入，同时也支持通道服务，即可使用此接口灵活接入第三方大模型/Agent。
        Call steps:
        1. Pass "start_voice_chat" as an input parameter to invoke the `get_note` method to obtain the parameter description.
        2. After obtaining the parameter description, invoke  start_voice_chat
        """
        reqs = service.mcp_post(
            "Conversational_aiMcpStartVoiceChat", params, json.dumps(body)
        )

        return reqs

    @mcp.tool()
    def update_voice_chat(params: dict, body: dict) -> str:
        """
        在实时音视频通话场景中，若你需要对智能体进行操作，比如在智能体进行语音输出时进行打断，可以通过调用此接口实现。
        Call steps:
        1. Pass "update_voice_chat" as an input parameter to invoke the `get_note` method to obtain the parameter description.
        2. After obtaining the parameter description, invoke  update_voice_chat
        """
        reqs = service.mcp_post(
            "Conversational_aiMcpUpdateVoiceChat", params, json.dumps(body)
        )

        return reqs

    @mcp.tool()
    def stop_voice_chat(params: dict, body: dict) -> str:
        """
        在实时音视频通话场景中，若你需要结束智能体的语音聊天服务，可以通过调用此接口实现。
        Call steps:
        1. Pass "stop_voice_chat" as an input parameter to invoke the `get_note` method to obtain the parameter description.
        2. After obtaining the parameter description, invoke  stop_voice_chat
        """
        reqs = service.mcp_post(
            "Conversational_aiMcpStopVoiceChat", params, json.dumps(body)
        )

        return reqs

    return mcp
