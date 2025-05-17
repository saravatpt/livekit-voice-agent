from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    # openai,
    noise_cancellation,
)
from livekit.plugins import google

load_dotenv()

# Assuming you have GOOGLE_TTS_MODEL and GOOGLE_TTS_VOICE set in your .env file
# from livekit.plugins.google import TTS

class VideoAssistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions='''You are an AI IT Support Agent. Your job is to assist users with troubleshooting technical issues, answering questions about software and hardware, and guiding them through IT-related tasks.
Follow these guidelines:
Communicate clearly and professionally, using simple language.
Ask clarifying questions when the issue is not fully described.
Provide step-by-step instructions where necessary.
When appropriate, suggest preventive tips to avoid future problems.
If a problem cannot be resolved immediately, offer alternative solutions or escalate accordingly.
Act like a real IT helpdesk professional, handling issues such as:
Internet connectivity problems
Printer setup or malfunctions
Email configuration and access issues
Software installation and errors
Password resets and account access
Basic cybersecurity practices
Troubleshooting Windows/Mac OS issues''',
            llm=google.beta.realtime.RealtimeModel(
                voice="Puck",
                temperature=0.8,
            ),
        ) 

# async def entrypoint(ctx: agents.JobContext):
#     session = AgentSession(
#         llm=openai.realtime.RealtimeModel(
#             voice="coral"
#         )
#     )

async def entrypoint(ctx: agents.JobContext):
    await ctx.connect()

    session = AgentSession()

    await session.start(
        agent=VideoAssistant(),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            video_enabled=True,
            # ... noise_cancellation, etc.
        ),
    )
    
    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
