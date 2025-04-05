from langchain_community.document_loaders import YoutubeLoader
from youtube_transcript_api import YouTubeTranscriptApi
from langchain_core.documents import Document

loader = YoutubeLoader.from_youtube_url(
    "https://www.youtube.com/watch?v=sb8VJHNa0oo&t=286s", add_video_info=False
)

transcript_list = YouTubeTranscriptApi.get_transcript(loader.video_id, languages=['en'])
transcript = " ".join([entry['text'] for entry in transcript_list])
docs = [Document(page_content=transcript, metadata=loader._metadata)]

print(docs)
