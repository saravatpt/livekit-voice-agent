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


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="You are a helpful voice AI assistant.")


# async def entrypoint(ctx: agents.JobContext):
#     session = AgentSession(
#         llm=openai.realtime.RealtimeModel(
#             voice="coral"
#         )
#     )

async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        llm=google.beta.realtime.RealtimeModel(
            model="gemini-2.0-flash-exp",
            vertexai=True,
            voice="Puck",
            temperature=0.8,
            instructions="You are a helpful voice AI assistant.",
        ),
    )

# room=ctx.room,
# room="my-room",
    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions="Greet the user and offer your assistance."
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
