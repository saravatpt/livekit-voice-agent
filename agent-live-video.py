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
            instructions="You are a helpful voice assistant with live video input from your user.",
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

# room=ctx.room,
# room="my-room",


    await ctx.connect()

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
